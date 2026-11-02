import type { QCProduct } from './catalogue';
import type { Judgement } from './qc';
export function openGaps(product:QCProduct,reviews:Record<string,{payload:Judgement}>):string[]{
 const q=product.quality;if(!q)return[];
 const checks=reviews[product.key]?.payload.checks||{};
 const photo=product.images[0]?reviews[product.images[0].key]?.payload:undefined;
 const photoOK=photo?.status==='correct'&&photo.main==='yes';
 return q.gaps.filter(g=>{
  if(photoOK&&['Foto en kleur nog beoordelen','Eigen variantfoto niet gekoppeld'].includes(g))return false;
  if(['correct','na'].includes(checks.pdf||'')&&['PDF-inhoud nog beoordelen','PDF ontbreekt','Maattekening / handleiding ontbreekt'].includes(g))return false;
  if(['correct','na'].includes(checks.specifications||'')&&g==='Specificaties aanvullen')return false;
  return true;
 });
}
