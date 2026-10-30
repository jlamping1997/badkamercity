import type { Judgement } from './qc';
export type PhotoChoice='correct'|'wrong'|'uncertain'|'technical';
export function mainPhotoItems<T extends {images:{key:string}[]}>(products:T[]){return products.flatMap(product=>product.images.length?[{key:product.images[0].key,product,image:product.images[0]}]:[])}
export function photoJudgement(choice:PhotoChoice,note:string=""):Judgement {
 if(choice==='technical')return {status:'wrong',role:'technical',main:'no',note:note.trim()||'Technische tekening als hoofdfoto.'};
 return {status:choice,role:'unknown',main:choice==='correct'?'yes':choice==='wrong'?'no':'unknown',note:note.trim()||(choice==='wrong'?'Hoofdfoto klopt niet.':'')};
}
export function mainPhotoCheckpoint<T extends {ids:string[],position:number,mode:string}>(checkpoint:T,available:Set<string>):T {
 if(checkpoint.mode!=='images')return checkpoint;
 return {...checkpoint,ids:checkpoint.ids.filter(id=>available.has(id)),position:checkpoint.ids.slice(0,checkpoint.position).filter(id=>available.has(id)).length};
}
export function reviewBatch<T extends {key:string}>(items:T[],reviews:Record<string,{payload:{status:string}}>,filter:string,size:number,order:string,rng:()=>number=Math.random):string[]{
 const eligible=items.filter(x=>filter==='pending'?(!reviews[x.key]||reviews[x.key].payload.status==='unchecked'):filter==='all'?true:reviews[x.key]?.payload.status===filter).map(x=>x.key);
 if(order==='random')for(let i=eligible.length-1;i>0;i--){const j=Math.floor(rng()*(i+1));[eligible[i],eligible[j]]=[eligible[j],eligible[i]];}
 return eligible.slice(0,size);
}
