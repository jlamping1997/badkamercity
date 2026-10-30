import catalogue from '@/data/catalogue.json';
export const dynamic='force-dynamic';
export async function GET(request:Request){
 const params=new URL(request.url).searchParams;const brand=params.get('brand');
 const products=brand?catalogue.products.filter(x=>brand==='all'||x.vendor===brand):[];
 const compact=params.get('scope')==='review';
 return Response.json(brand?{products:compact?products.map(p=>({...p,images:p.images.slice(0,1),description:p.description.slice(0,600)})):products,snapshot:catalogue.snapshot}:catalogue.summary,{headers:{'Cache-Control':'private, no-store'}});
}
