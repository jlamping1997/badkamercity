import catalogue from '@/lib/catalogue';
import official from '@/data/lagoo-official.json';
export const dynamic='force-dynamic';
export async function GET(request:Request){
 const params=new URL(request.url).searchParams;const brand=params.get('brand');
 const sku=params.get('sku');const products=brand?catalogue.products.filter(x=>(brand==='all'||x.vendor===brand)&&(!sku||x.skus.includes(sku))):[];
 if(brand==='Lagoo'&&params.get('scope')==='legacy-import')return Response.json({error:'Oude bronimport blijft bewaard in de private herstelkopie; gebruik de nieuwe fabrikantwerkset.'},{status:410,headers:{'Cache-Control':'private, no-store'}});
 if(brand==='Lagoo'&&params.get('scope')==='import')return Response.json({schema:4,source:'lagoo.nl',summary:official.summary,products:products.filter(p=>p.quality?.official).map(p=>({...p,images:p.quality?.official?.photoEvidence==='exact_code'?p.images:[],photoImportReady:p.quality?.official?.photoEvidence==='exact_code'}))},{headers:{'Cache-Control':'private, no-store'}});
 const compact=params.get('scope')==='review';
 return Response.json(brand?{products:compact?products.map(p=>({...p,images:p.images.slice(0,1),description:p.description.slice(0,600),...(p.quality?{quality:{...p.quality,documents:[],features:[]}}:{})})):products,snapshot:catalogue.snapshot}:catalogue.summary,{headers:{'Cache-Control':'private, no-store'}});
}
