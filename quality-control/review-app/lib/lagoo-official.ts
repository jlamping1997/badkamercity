import type {QCCatalogue,QCProduct,QCDocument,QCImage} from './catalogue';
export type OfficialIndex={summary:Record<string,unknown>,assets:Record<string,{id:string,title:string,url:string,sourceUrl:string,fileId:string,kind:string,width:number,height:number,documentType:string}>,products:Record<string,{url:string,description:string,features:string[],roughPartMentions:{codes:string[],sourceText:string}[]}>,variants:Record<string,{imageIds:string[],documents:{id:string,suggested:boolean}[],productIds:string[],photoEvidence:string,gaps:string[]}>};
export function applyOfficialSource(catalogue:QCCatalogue,source:OfficialIndex):QCCatalogue{
 const docs=new Map<string,QCDocument>();
 const products=catalogue.products.map((p):QCProduct=>{const row=source.variants[p.key];if(p.vendor!=='Lagoo'||!p.quality||!row)return p;const detail=source.products[row.productIds[0]];const images:QCImage[]=row.imageIds.map((id,i)=>{const a=source.assets[id];return {key:'image:lagoo-official:'+p.skus[0]+':'+id,url:a.url,sourceUrl:a.sourceUrl,alt:'Lagoo '+p.skus[0]+' · '+a.title,width:a.width,height:a.height,position:i+1,mediaId:a.fileId}});const documents=row.documents.map(({id,suggested})=>{const k=id+':'+suggested;if(!docs.has(k)){const a=source.assets[id];docs.set(k,{title:a.title,url:a.url,sourceUrl:a.sourceUrl,fileId:a.fileId,kind:'pdf',owned:true,suggested})}return docs.get(k)!});const mentions=row.productIds.flatMap(id=>source.products[id]?.roughPartMentions||[]);return {...p,description:detail?.description||p.description,images,quality:{...p.quality,legacyApprovedImageKeys:p.quality.approvedImageKeys,approvedImageKeys:[],photoSelectionAppliedAt:undefined,sourceUrl:detail?.url||'',documents,features:detail?.features||p.quality.features,rough:mentions.length?[...new Set(mentions.flatMap(m=>m.codes))]:p.quality.rough,gaps:row.gaps,imageBinding:row.photoEvidence==='exact_code'?'Fabrikantfoto op artikel-/kleurcode':row.photoEvidence==='group_candidates'?'Fabrikantgalerij: kleur nog controleren':'Geen fabrikantfoto gekoppeld',imageNote:'Nieuwe fabrikantbestanden; eerdere beoordelingen blijven bewaard als historie.',official:{urls:row.productIds.map(id=>source.products[id].url),photoEvidence:row.photoEvidence,roughPartMentions:mentions}}}});
 const old=new Set(catalogue.items.map(i=>i.key));const added=products.flatMap(p=>p.images.filter(i=>!old.has(i.key)).map(i=>({key:i.key,kind:'image'})));
 return {...catalogue,products,items:[...catalogue.items,...added]};
}

// Manufacturer galleries are accepted by the owner. Colour-specific associations require exact evidence.
export function officialImportProducts(products:QCProduct[],source:OfficialIndex){
 return products.filter(p=>p.vendor==='Lagoo'&&p.quality?.official&&source.variants[p.key]).map(p=>{
  const row=source.variants[p.key];
  const ids=[...new Set([...row.imageIds,...((row as {galleryImageIds?:string[]}).galleryImageIds||[])])];
  const images:QCImage[]=ids.map(id=>source.assets[id]).filter(a=>a?.kind==='IMAGE'&&a.url&&a.fileId).map((a,i)=>({key:'image:lagoo-official:'+p.skus[0]+':'+a.id,url:a.url,sourceUrl:a.sourceUrl,alt:'Lagoo '+p.skus[0]+' · '+a.title,width:a.width,height:a.height,position:i+1,mediaId:a.fileId}));
  return {...p,images,variantImages:row.photoEvidence==='exact_code'?p.images:[],photoImportReady:images.length>0,variantPhotoMatched:row.photoEvidence==='exact_code',photoSource:'lagoo.nl',photoPolicy:'manufacturer_gallery_only',photoGap:images.length?'':'Geen fabrikantfoto gevonden; geen oude bronfoto gebruiken'};
 });
}
