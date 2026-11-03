import fs from 'node:fs';
import {spawnSync} from 'node:child_process';
// Derive the runtime base; retain the complete original catalogue as private evidence.
const catalogue=JSON.parse(fs.readFileSync('data/lagoo-catalogue.json','utf8'));
const official=JSON.parse(fs.readFileSync('data/lagoo-official.json','utf8'));
for(const product of catalogue.products)if(official.variants[product.key]){product.images=[];product.quality.documents=[];}
fs.writeFileSync('data/lagoo-runtime.json',JSON.stringify(catalogue));
// Vinext shares output paths across build stages; stale hashed chunks must not enter a new Worker.
fs.rmSync('dist',{recursive:true,force:true});
const result=spawnSync(process.execPath,['scripts/run-framework.mjs','build'],{stdio:'inherit'});
process.exit(result.status??1);
