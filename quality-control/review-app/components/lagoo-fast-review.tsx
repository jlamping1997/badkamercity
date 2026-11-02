'use client';
import {Check,X,HelpCircle,ArrowLeft,ArrowRight,RotateCcw,ZoomIn,Moon,Sun,Loader2,CloudCheck} from 'lucide-react';
import type {QCProduct} from '@/lib/catalogue';
import type {PhotoChoice} from '@/lib/main-photo';
type Image=QCProduct['images'][number];
type Props={product?:QCProduct,image?:Image,candidates:Image[],detailsReady:boolean,position:number,total:number,reviewed:number,available:number,loading:boolean,ready:boolean,busy:boolean,blocked:boolean,imageReady:boolean,imageError:boolean,error:string,message:string,theme:string,canUndo:boolean,done:boolean,onJudge:(c:PhotoChoice)=>void,onChoose:(i:Image)=>void,onImageLoad:()=>void,onImageError:()=>void,onZoom:()=>void,onTheme:()=>void,onAdvanced:()=>void,onUndo:()=>void,onSkip:()=>void,onContinue:()=>void,onRetry:()=>void,onConnect:()=>void};
export default function LagooFastReview(p:Props){
 const colour=p.product?.quality?.colour?.trim()||'Geen kleur opgegeven';
 const current=Math.max(0,p.candidates.findIndex(i=>i.key===p.image?.key));
 const locked=p.busy||p.blocked;
 return <div className="lagoo-fast">
  <header className="fast-header"><strong>Lagoo <span>· kleurcontrole</span></strong><div><span className="fast-saved" role="status">{p.busy?<Loader2 size={15} className="spin"/>:<CloudCheck size={15}/>}<span>{p.busy?'Opslaan…':p.ready?'Opgeslagen':'Niet verbonden'}</span></span><button className="icon-button" onClick={p.onTheme} aria-label={p.theme==='dark'?'Dagmodus':'Nachtmodus'}>{p.theme==='dark'?<Sun size={17}/>:<Moon size={17}/>}</button></div></header>
  <main className="fast-main">
   {p.error&&<div className="alert" role="alert"><span>{p.error}</span>{p.blocked&&<button onClick={p.onRetry} disabled={p.busy}>Opnieuw proberen</button>}{!p.ready&&<><a href="/signin-with-chatgpt?return_to=/" target="_top">Aanmelden</a><button onClick={p.onConnect}>Opnieuw verbinden</button></>}</div>}
   {p.product&&p.image?<section className="fast-card" aria-label="Lagoo kleur controleren">
    <div className="fast-colour"><span>Kleur volgens titel</span><h1>{colour}</h1><small>{p.product.skus[0]} <span>· {p.position+1} / {p.total}</span></small></div>
    <div className="fast-photo"><img key={p.product.key+":"+p.image.url} src={p.image.url} alt={'Controleer '+colour+' — '+p.product.skus[0]} onLoad={p.onImageLoad} onError={p.onImageError} draggable={false}/><button className="icon-button fast-zoom" aria-label="Foto vergroten" onClick={p.onZoom}><ZoomIn size={20}/></button>{p.imageError&&<p className="image-error">Foto laadt niet. Kies een andere foto of Twijfel.</p>}</div>
    <div className="fast-candidates"><button onClick={()=>p.onChoose(p.candidates[current-1])} disabled={locked||!p.detailsReady||current===0} aria-label="Vorige foto"><ArrowLeft size={17}/></button><span>{p.detailsReady?`Foto ${current+1} van ${p.candidates.length}`:'Foto’s laden…'}</span><button onClick={()=>p.onChoose(p.candidates[(current+1)%p.candidates.length])} disabled={locked||!p.detailsReady||p.candidates.length<2}>Andere foto <ArrowRight size={17}/></button></div>
    <div className="fast-dock"><div className="decisions"><button className="decision no" disabled={locked||!p.ready} onClick={()=>p.onJudge('wrong')}><X size={23}/><span>Nee</span></button><button className="decision unsure" disabled={locked||!p.ready} onClick={()=>p.onJudge('uncertain')}><HelpCircle size={23}/><span>Twijfel</span></button><button className="decision yes" disabled={locked||!p.ready||!p.detailsReady||!p.imageReady||p.imageError} onClick={()=>p.onJudge('correct')}><Check size={24}/><span>Ja</span></button></div></div>
    <div className="fast-secondary"><button onClick={p.onUndo} disabled={!p.canUndo||locked}><RotateCcw size={14}/> Terug</button><button disabled={locked||!p.ready||!p.detailsReady||!p.imageReady||p.imageError} onClick={()=>p.onJudge('technical')}>Technische tekening</button><button disabled={locked} onClick={p.onSkip}>Later <ArrowRight size={14}/></button></div>
    <details className="fast-details"><summary>Alle foto’s en producttitel</summary><p>{p.product.title}</p><div className="candidate-grid">{p.candidates.map(im=><button type="button" key={im.key} aria-label={'Kies foto '+im.position} aria-pressed={p.image?.key===im.key} disabled={locked} onClick={()=>p.onChoose(im)}><img loading="lazy" src={im.url} alt={'Foto '+im.position}/></button>)}</div></details>
   </section>:<section className="fast-empty"><h1>{p.loading?'Foto’s laden…':p.done?'Deze ronde is klaar.':'Geen nieuwe foto’s.'}</h1><p>{p.loading?'Je Lagoo-foto’s en opgeslagen voortgang worden opgehaald.':'Je keuzes zijn bewaard. Open Uitgebreid om afgekeurde foto’s, twijfels of ontbrekende gegevens te bekijken.'}</p>{!p.loading&&<button className="primary" onClick={p.onContinue} disabled={locked}>Verder met Lagoo <ArrowRight size={17}/></button>}</section>}
   <footer className="fast-footer"><span>{p.reviewed} / {p.available} foto’s beoordeeld</span><button disabled={locked} onClick={p.onAdvanced}>Uitgebreid</button></footer><p className="fast-message" role="status">{p.message||'Kleur klopt? Kies Ja. Je gaat automatisch verder.'}</p>
  </main>
 </div>
}
