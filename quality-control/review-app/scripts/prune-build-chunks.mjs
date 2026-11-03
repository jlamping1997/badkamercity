import fs from 'node:fs';
import path from 'node:path';
// Vinext can retain chunks from a prior build. Only ship modules reachable from either Worker entry.
const root=path.resolve('dist/server');
const queue=[path.join(root,'index.js'),path.join(root,'ssr/index.js')];
const seen=new Set();
while(queue.length){
 const file=queue.shift();if(seen.has(file)||!fs.existsSync(file))continue;
 seen.add(file);
 const code=fs.readFileSync(file,'utf8');
 for(const match of code.matchAll(/["'`]([^"'`\n]+\.m?js)["'`]/g)){
  if(!match[1].startsWith('.'))continue;
  const target=path.resolve(path.dirname(file),match[1]);
  if(target.startsWith(root+path.sep)){if(!fs.existsSync(target))throw Error('Missing built module: '+target);queue.push(target);}
 }
}
function files(dir){return fs.readdirSync(dir,{withFileTypes:true}).flatMap(e=>e.isDirectory()?files(path.join(dir,e.name)):[path.join(dir,e.name)]);}
let removed=0;
for(const file of files(root)){
 const generated=path.relative(root,file).includes('_next/static/');
 if(generated&&((/\.m?js$/.test(file)&&!seen.has(file))||/^\..*\.js\./.test(path.basename(file)))){fs.unlinkSync(file);removed++;}
}
const bytes=files(root).reduce((n,f)=>n+fs.statSync(f).size,0);
if(bytes>50*1024*1024)throw Error('Worker output exceeds 50 MiB after stale-chunk cleanup');
console.log(JSON.stringify({reachableWorkerModules:seen.size,staleBuildFilesRemoved:removed,workerOutputBytes:bytes}));
