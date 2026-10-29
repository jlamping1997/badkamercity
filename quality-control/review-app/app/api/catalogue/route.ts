import catalogue from '@/data/catalogue.json';
export const dynamic='force-dynamic';
export async function GET(request:Request){const brand=new URL(request.url).searchParams.get('brand');return Response.json(brand?{products:catalogue.products.filter(x=>x.vendor===brand),snapshot:catalogue.snapshot}:catalogue.summary,{headers:{'Cache-Control':'private, no-store'}})}
