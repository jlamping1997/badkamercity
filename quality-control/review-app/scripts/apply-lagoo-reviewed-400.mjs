import fs from 'node:fs';
const source=JSON.parse(fs.readFileSync('data/lagoo-catalogue.json'));
const snapshot=JSON.parse(fs.readFileSync('.sites-runtime/lagoo-review-snapshot-400.json'));
const checkpoint=snapshot.checkpoints.find(c=>c.name==='Lagoo · 400 producten bekeken');
if(!checkpoint||checkpoint.payload.nextSku!=='N8100CH'||source.products[400].skus[0]!=='N8100CH')throw Error('Checkpoint and catalogue order differ');
const reviews=new Map(snapshot.reviews.map(r=>[r.item,r]));
const approvals={},products=[];
for(const p of source.products.slice(0,400)){
 if(/^LVS[123]$/i.test(p.quality.article))throw Error('Protected set included');
 const images=p.images.filter(i=>{const r=reviews.get(i.key);return r?.payload.status==='correct'&&(!r.payload.selectedImage||r.payload.selectedImage===i.key)&&r.updated<=checkpoint.created});
 approvals[p.skus[0]]={imageKeys:images.map(i=>i.key),appliedThrough:checkpoint.created,status:images.length?'selected':'no-selection'};
 products.push({...p,images,quality:{...p.quality,approvedImageKeys:images.map(i=>i.key),photoSelectionAppliedAt:checkpoint.created},photoImportReady:images.length>0});
}
const scope={checkpoint:checkpoint.name,cutoff:checkpoint.created,products:400,selectedVariants:products.filter(p=>p.images.length).length,photoSelections:products.reduce((n,p)=>n+p.images.length,0),withoutSelection:products.filter(p=>!p.images.length).length,nextSku:'N8100CH',excludedArticles:['LVS1','LVS2','LVS3']};
fs.writeFileSync('data/lagoo-photo-approvals.json',JSON.stringify({scope,approvals}));
fs.writeFileSync('data/lagoo-approved-import.json',JSON.stringify({scope,products}));
console.log(JSON.stringify(scope));
