import fs from 'node:fs';
import {createHash} from 'node:crypto';
const [sourcePath,assetsPath,filesPath,suggestionsPath,targetPath,verificationPath]=process.argv.slice(2);
if(!targetPath)throw Error('Usage: import-lagoo source assets files suggestions target-receipt');
const source=JSON.parse(fs.readFileSync(sourcePath)),assets=JSON.parse(fs.readFileSync(assetsPath)),owned=JSON.parse(fs.readFileSync(filesPath)),suggestions=JSON.parse(fs.readFileSync(suggestionsPath)),target=JSON.parse(fs.readFileSync(targetPath));
if(source.products.length!==211||source.failures.length||owned.shop!=='fpa9hu-i3.myshopify.com')throw Error('Incomplete or wrong source');
const verification=verificationPath?JSON.parse(fs.readFileSync(verificationPath)):null;if(verification&&(!verification.complete||verification.summary.verified_owned_pdf_urls!==251))throw Error('PDF integrity verification incomplete');
const pdfProof=new Map((verification?.items||[]).map(x=>[x.source_url,x]));
const hash=x=>createHash('sha256').update(JSON.stringify(x)).digest('hex').slice(0,24);
const ownByTag=new Map(owned.files.map(f=>[f.alt?.split(' ').at(-1),f]));
const ownBySource=new Map(assets.map(a=>[a.source_url,ownByTag.get(a.alt.split(' ').at(-1))]));
const catalog=JSON.parse(fs.readFileSync('data/catalogue.json'));
if(!fs.existsSync('.sites-runtime'))fs.mkdirSync('.sites-runtime');
if(!fs.existsSync('.sites-runtime/catalogue-before-lagoo.json'))fs.copyFileSync('data/catalogue.json','.sites-runtime/catalogue-before-lagoo.json');
const original=catalog.products.filter(p=>p.vendor!=='Lagoo');
const oldItems=catalog.items.filter(i=>!i.key.startsWith('product:lagoo:')&&!i.key.startsWith('image:lagoo:'));
const additions=[],newItems=[],skuSet=new Set();
for(const p of source.products){
 const d=source.details[p.handle].lagoo_data,m=d.metadata,imported=target.products.find(t=>t.handle===p.handle);
 for(const v of p.variants){
  if(!v.sku||skuSet.has(v.sku))throw Error('Duplicate SKU');skuSet.add(v.sku);
  const info=m.variantArticles[String(v.id)],article=m.articles[info.code]||{},publicV=d.variants.find(x=>x.id===v.id);
  const selection=Object.fromEntries(p.options.map((o,i)=>[o.name,v['option'+(i+1)]]).filter(([k,val])=>val&&val!=='Default Title'));
  const key='product:lagoo:'+v.sku+':'+hash([p.handle,v.sku,selection]);
  const selectedSrc=v.featured_image?.src||publicV?.image||'';
  const filename=x=>{try{return new URL(x.startsWith('//')?'https:'+x:x).pathname.split('/').at(-1)}catch{return ''}};
  const pics=[...p.images].sort((a,b)=>Number(filename(b.src)===filename(selectedSrc))-Number(filename(a.src)===filename(selectedSrc)));
  const images=pics.flatMap((im,index)=>{const f=ownBySource.get(im.src);if(f?.fileStatus!=='READY'||!f.image?.url)return[];const image={key:'image:lagoo:'+v.sku+':'+hash([im.src]),url:f.image.url,alt:im.alt||p.title,width:f.image.width||im.width||0,height:f.image.height||im.height||0,position:index+1,mediaId:f.id,sourceUrl:im.src};newItems.push({key:image.key,kind:'image'});return[image]});
  const docs=(article.downloads||[]).map(x=>{const f=ownBySource.get(x.url),isPdf=new URL(x.url).pathname.toLowerCase().endsWith('.pdf');return{title:x.title||'Document',url:f?.fileStatus==='READY'&&f.url?f.url:x.url,sourceUrl:x.url,fileId:f?.id||'',kind:isPdf?'pdf':'video',owned:!!(f?.fileStatus==='READY'&&f.url),sha256:pdfProof.get(x.url)?.sha256,suggested:false}});
  for(const x of suggestions.filter(s=>s.handle===p.handle&&s.article===info.code)){const f=ownBySource.get(x.source_url);if(f?.fileStatus==='READY'&&f.url&&!docs.some(z=>z.sourceUrl===x.source_url))docs.push({title:'Suggestie: '+new URL(x.source_url).pathname.split('/').at(-1),url:f.url,sourceUrl:x.source_url,fileId:f.id,kind:'pdf',owned:true,sha256:pdfProof.get(x.source_url)?.sha256,suggested:true});}
  const direct=docs.filter(x=>x.kind==='pdf'&&!x.suggested),gaps=[];
  if(!images.length)gaps.push('Productfoto ontbreekt');
  if(!selectedSrc)gaps.push('Eigen variantfoto niet gekoppeld');
  if(!direct.length)gaps.push('PDF ontbreekt');
  else if(!direct.some(x=>/maat|montage|handleiding|installatie/i.test(x.title)))gaps.push('Maattekening / handleiding ontbreekt');
  if(docs.some(x=>x.kind==='pdf'&&!x.owned))gaps.push('PDF nog niet in eigen beheer');
  if(!article.features?.length&&!Object.keys(selection).length)gaps.push('Specificaties aanvullen');
  if(!publicV?.barcode)gaps.push('EAN ontbreekt');
  if(images.length)gaps.push('Foto en kleur nog beoordelen');
  if(direct.length)gaps.push('PDF-inhoud nog beoordelen');
  const variantTitle=v.title==='Default Title'?'':v.title;
  const quality={sourceHandle:p.handle,article:info.code,colour:selection.Kleur||info.color||'',series:m.series||'',price:v.price,ean:publicV?.barcode||'',options:selection,features:article.features||[],rough:article.rough||[],documents:docs,gaps,imageBinding:selectedSrc?'Bronkoppeling, niet inhoudelijk goedgekeurd':'Geen bronkoppeling: kies juiste foto',imageNote:info.photoNote||'',shopifyStatus:imported?'DRAFT':'NOT_IMPORTED',adminUrl:imported?'https://admin.shopify.com/store/fpa9hu-i3/products/'+imported.id.split('/').at(-1):'',sourceUrl:'https://badkamervoorjou.nl/products/'+p.handle};
  additions.push({key,id:'lagoo-source:'+v.sku,title:p.title+(variantTitle?' — '+variantTitle:''),vendor:'Lagoo',type:p.product_type,url:'https://badkamercity.nl/products/'+p.handle,skus:[v.sku],variants:variantTitle?[variantTitle]:[],description:source.details[p.handle].product_schema.description||'',images,truncated:false,quality});newItems.push({key,kind:'product'});
 }
}
if(additions.length!==1796)throw Error('Wrong Lagoo variant count');
catalog.products=[...original,...additions];catalog.items=[...oldItems,...newItems];
if(new Set(catalog.items.map(x=>x.key)).size!==catalog.items.length)throw Error('Duplicate keys');
catalog.summary.brands=catalog.summary.brands.filter(b=>b.name!=='Lagoo');catalog.summary.brands.push({name:'Lagoo',products:additions.length,productGroups:211,images:additions.reduce((n,p)=>n+p.images.length,0),missingImages:additions.filter(p=>!p.images.length).length,incomplete:0,activeRead:0,complete:true,scope:'Gedateerde bronimport; één controle per artikel/kleurvariant; zes Shopify-conceptgroepen'});
catalog.snapshot={...catalog.snapshot,lagooAdded:'2026-11-02',lagooGroups:211,lagooVariants:1796};catalog.summary.snapshot=catalog.snapshot;
fs.writeFileSync('data/lagoo-catalogue.json',JSON.stringify({products:additions,items:newItems}));fs.writeFileSync('data/catalogue.json',JSON.stringify({...catalog,products:original,items:oldItems}));fs.writeFileSync('data/import-summary.json',JSON.stringify(catalog.summary,null,2)+'\n');
fs.writeFileSync('data/lagoo-ownership.json',JSON.stringify({sourceDate:source.retrieved_at_utc,shop:owned.shop,assets:assets.map(a=>{const f=ownBySource.get(a.source_url);return{sourceUrl:a.source_url,fileId:f?.id,status:f?.fileStatus,ownedUrl:f?.url||f?.image?.url||null}})}));
if(verification)fs.writeFileSync('data/lagoo-document-verification.json',JSON.stringify(verification));
console.log(JSON.stringify({preserved:original.length,added:additions.length,total:catalog.products.length,groups:211,images:additions.reduce((n,p)=>n+p.images.length,0),allOwned:owned.files.every(f=>f.fileStatus==='READY')}));
