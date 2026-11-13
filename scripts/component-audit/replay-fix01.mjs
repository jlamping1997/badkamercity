// Reproduce FIX-01 using candidate files plus four explicit, immutable MAIN dependencies.
// No network, credentials, production writes or customer storage.
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {execFileSync} from 'node:child_process';

const here=path.dirname(fileURLToPath(import.meta.url));
const root=path.resolve(here,'../..');
const proof=path.join(root,'docs/repairs/2026-10-31');
const manifest=path.join(proof,'final-source-provenance.json');
const pinned=new Set(['assets/bc-product-switcher.js','assets/bc-porcelanosa-core.js','assets/bc-mobile-listing.js','assets/bc-product-inbouw.js']);
const source=fs.mkdtempSync(path.join(os.tmpdir(),'bc-fix01-'));
const output=path.resolve(process.argv[2]||path.join(source,'results'));
fs.mkdirSync(output,{recursive:true});
try {
  for(const row of JSON.parse(fs.readFileSync(manifest,'utf8')).files){
    const origin=path.join(pinned.has(row.path)?path.join(here,'fixtures/fix01-baseline'):root,row.path);
    const bytes=fs.readFileSync(origin);
    if(crypto.createHash('sha256').update(bytes).digest('hex')!==row.sha256)throw Error('Source mismatch: '+row.path);
    const destination=path.join(source,row.path);fs.mkdirSync(path.dirname(destination),{recursive:true});fs.writeFileSync(destination,bytes);
  }
  for(const name of ['cart-sunshower','filters','wishlist','presentation']){
    execFileSync(process.execPath,[path.join(here,'repair-'+name+'.mjs'),'--source',source,'--manifest',manifest,'--output',path.join(output,name+'.json')],{stdio:'inherit'});
  }
  console.log('All FIX-01 replays completed. Results: '+output);
} finally {
  // With an explicit output directory only our disposable source copy is removed.
  if(process.argv[2])fs.rmSync(source,{recursive:true,force:true});
}
