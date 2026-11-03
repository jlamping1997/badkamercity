export function lagooProtectedSet(p:{skus:string[],quality?:{article:string}}){return /^LVS[123]$/i.test(p.quality?.article||'')||p.skus.some(s=>/^LVS[123](CH|BN|MB|TC|BB|BK|GM|PG)$/i.test(s));}
export function lagooGalleryProducts<T extends {skus:string[],quality?:{article:string}}>(products:T[]):T[]{return products.filter(p=>!lagooProtectedSet(p));}
