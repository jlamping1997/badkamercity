import base from '@/data/catalogue.json';
import lagoo from '@/data/lagoo-catalogue.json';
const data={...base,products:[...base.products,...lagoo.products],items:[...base.items,...lagoo.items]};
export type QCImage={key:string,url:string,alt:string,width:number,height:number,position:number,mediaId?:string,sourceUrl?:string};
export type QCDocument={title:string,url:string,sourceUrl:string,fileId?:string,kind:string,owned:boolean,suggested?:boolean,sha256?:string};
export type QCQuality={sourceHandle:string,article:string,colour:string,series:string,price:string,ean:string,options:Record<string,string>,features:string[],rough:string[],documents:QCDocument[],gaps:string[],imageBinding:string,imageNote:string,shopifyStatus:string,adminUrl:string,sourceUrl:string};
export type QCProduct={key:string,id:string,title:string,vendor:string,type:string,url:string,skus:string[],variants:string[],description:string,images:QCImage[],truncated:boolean,quality?:QCQuality};
export type QCCatalogue={products:QCProduct[],items:{key:string,kind:string}[],snapshot:Record<string,unknown>,summary:{snapshot:Record<string,unknown>,brands:{name:string,products:number,images:number,missingImages:number,incomplete:number,[key:string]:unknown}[]}};
export default data as unknown as QCCatalogue;
