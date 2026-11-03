import catalogue from '@/lib/catalogue';
import approvedImport from '@/data/lagoo-approved-import.json';
export const dynamic='force-dynamic';
export async function GET(request:Request){
 const params=new URL(request.url).searchParams;const brand=params.get('brand');
 const sku=params.get('sku');const products=brand?catalogue.products.filter(x=>(brand==='all'||x.vendor===brand)&&(!sku||x.skus.includes(sku))):[];
 if(brand==='Lagoo'&&params.get('scope')==='import')return Response.json(approvedImport,{headers:{'Cache-Control':'private, no-store'}});
 const compact=params.get('scope')==='review';
 return Response.json(brand?{products:compact?products.map(p=>({...p,images:p.images.slice(0,1),description:p.description.slice(0,600),...(p.quality?{quality:{...p.quality,documents:[],features:[]}}:{})})):products,snapshot:catalogue.snapshot}:catalogue.summary,{headers:{'Cache-Control':'private, no-store'}});
}
