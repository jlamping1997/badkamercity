import type { Judgement } from './qc';
export type PhotoChoice='correct'|'wrong'|'uncertain'|'technical';
export function mainPhotoItems<T extends {images:{key:string}[]}>(products:T[]){return products.flatMap(product=>product.images.length?[{key:product.images[0].key,product,image:product.images[0]}]:[])}
export function photoJudgement(choice:PhotoChoice):Judgement {
 if(choice==='technical')return {status:'wrong',role:'technical',main:'no',note:'Technische tekening als hoofdfoto.'};
 return {status:choice,role:'unknown',main:choice==='correct'?'yes':choice==='wrong'?'no':'unknown',note:choice==='wrong'?'Hoofdfoto klopt niet.':''};
}
export function mainPhotoCheckpoint<T extends {ids:string[],position:number,mode:string}>(checkpoint:T,available:Set<string>):T {
 if(checkpoint.mode!=='images')return checkpoint;
 return {...checkpoint,ids:checkpoint.ids.filter(id=>available.has(id)),position:checkpoint.ids.slice(0,checkpoint.position).filter(id=>available.has(id)).length};
}
