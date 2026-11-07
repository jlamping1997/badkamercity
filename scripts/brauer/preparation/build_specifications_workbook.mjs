import fs from 'node:fs/promises';
import path from 'node:path';
import {Workbook,SpreadsheetFile} from '@oai/artifact-tool';
const root=process.argv[2],dir=path.join(root,'outputs/brauer-20');
const catalog=JSON.parse(await fs.readFile(path.join(root,'prepared/catalog.json'),'utf8'));
const summary=JSON.parse(await fs.readFile(path.join(root,'prepared/specification-summary.json'),'utf8'));
const evidence=JSON.parse(await fs.readFile(path.join(root,'prepared/specification-evidence.json'),'utf8'));
const examples=JSON.parse(await fs.readFile(path.join(root,'prepared/specification-examples.json'),'utf8'));
const wb=Workbook.create(),font={name:'Arial',size:10,color:'#213647'};
for(const n of ['Overzicht','Voorbeelden','Artikelen'])wb.worksheets.add(n);
function col(i){let v='';for(i++;i;i=Math.floor((i-1)/26))v=String.fromCharCode(65+(i-1)%26)+v;return v;}
function table(name,headers,rows,widths){
 const s=wb.worksheets.getItem(name),end=rows.length+1,last=col(headers.length-1);s.showGridLines=false;
 s.getRange(`A1:${last}${end}`).values=[headers,...rows];s.getRange(`A1:${last}${end}`).format={font,rowHeight:26,verticalAlignment:'center'};
 s.getRange(`A1:${last}1`).format={fill:'#15374F',font:{...font,color:'#FFFFFF',bold:true},wrapText:true,rowHeight:38,horizontalAlignment:'center'};
 widths.forEach((w,i)=>s.getRange(`${col(i)}1:${col(i)}${end}`).format.columnWidth=w);
 s.tables.add(`A1:${last}${end}`,true,'Spec'+name);s.freezePanes.freezeRows(1);s.freezePanes.freezeColumns(1);return s;
}
const erows=examples.flatMap(p=>p.groups.flatMap(g=>g.items.map(i=>{const e=evidence[p.sku].facts[i.label];return [p.sku,p.type,g.group,i.label,i.value,e.kind==='supplier'?'Prijslijst BRAUER':'Eerdere controle exact artikel',e.field,e.fragment,e.url||e.source_refs[0]?.file||''];})));
const ex=table('Voorbeelden',['Artikelnummer','Producttype','Onderdeel','Specificatie','Klantwaarde','Herkomst','Bronveld','Bronwaarde','Bestand of bronpagina'],erows,[25,32,18,42,48,36,30,70,75]);
ex.getRange(`D2:I${erows.length+1}`).format.wrapText=true;
erows.forEach((r,i)=>{ex.getRange(`A${i+2}:I${i+2}`).format.rowHeight=Math.max(30,Math.ceil(Math.max(String(r[4]).length/45,String(r[7]).length/65,String(r[8]).length/70))*15+8);if(r[3]==='EAN')ex.getRange(`E${i+2}`).setNumberFormat('0000000000000');});
const prows=catalog.map(p=>{const s=p.specifications;return [p.sku,p.product_type,p.title,Object.keys(s).length,p.specification_review.status,s.Breedte||'',s.Diepte||'',s.Hoogte||'',s['Hoogte kraan']||'',s['Lengte uitloop']||'',p.specification_review.missing_essential_fields.join(', '),p.data_issues.join(', ')];});
const pr=table('Artikelen',['Artikelnummer','Producttype','Product','Aantal specs','Status specs','Breedte','Diepte','Hoogte','Hoogte kraan','Lengte uitloop','Nog aanvullen / bevestigen','Bestaande bronblokkades'],prows,[25,34,92,14,23,18,18,18,20,26,105,65]);
pr.getRange(`A2:A${prows.length+1}`).setNumberFormat('@');pr.getRange(`C2:C${prows.length+1}`).format.wrapText=true;pr.getRange(`K2:L${prows.length+1}`).format.wrapText=true;pr.getRange(`A2:L${prows.length+1}`).format.rowHeight=48;
pr.getRange(`E2:E${prows.length+1}`).conditionalFormats.add('containsText',{text:'AANVULLEN',format:{fill:'#FFF0CF',font:{color:'#6A4710'}}});
const o=wb.worksheets.getItem('Overzicht');o.showGridLines=false;o.tabColor='#15374F';o.getRange('A1:F90').format.font=font;
for(const [i,w] of [36,16,22,22,80,98].entries())o.getRange(`${col(i)}1:${col(i)}90`).format.columnWidth=w;
o.getRange('A2').values=[['BRAUER specificaties']];o.getRange('A2').format.font={...font,size:14};
o.getRange('A4:C7').values=[['Artikelen',null,'Alle unieke artikelnummers'],['Producttypen',summary.product_types,'Eigen relevante kenmerken per type'],['Nog technische gegevens nodig',null,'Ontbrekende maten en aansluitgegevens staan per artikel vermeld'],['Shopify-import','Geblokkeerd','Officiële afbeeldingen en PDF’s moeten nog binnenkomen']];
o.getRange('B4').formulas=[[`=COUNTA(Artikelen!A2:A${prows.length+1})`]];o.getRange('B6').formulas=[[`=COUNTIFS(Artikelen!E2:E${prows.length+1},"AANVULLEN")`]];
o.getRange('C4:C7').format.wrapText=true;[30,48,64,64].forEach((h,i)=>o.getRange(`A${i+4}:C${i+4}`).format.rowHeight=h);
o.getRange('A9:F9').values=[['Producttype','Artikelen','Specs totaal','Basis aanwezig','Ontbrekende kerngegevens (aantal artikelen)','Wat de status betekent']];
o.getRange('A9:F9').format={fill:'#15374F',font:{...font,color:'#FFFFFF',bold:true},wrapText:true,rowHeight:38,horizontalAlignment:'center'};
const tr=summary.types.map(t=>[t.type,t.articles,t.facts,t.complete_essential_articles,Object.entries(t.missing).map(([k,v])=>k+': '+v).join('; '),'Basis aanwezig = gekozen kernvelden gevuld; geen volledige technische vrijgave.']);
o.getRange(`A10:F${tr.length+9}`).values=tr;o.getRange(`A10:F${tr.length+9}`).format.rowHeight=42;o.getRange(`E10:F${tr.length+9}`).format.wrapText=true;
tr.forEach((r,i)=>o.getRange(`A${i+10}:F${i+10}`).format.rowHeight=Math.max(42,Math.ceil(r[4].length/75)*16));
o.tables.add(`A9:F${tr.length+9}`,true,'SpecTypen');o.freezePanes.freezeRows(9);
wb.recalculate();
if(o.getRange('B4').values[0][0]!==13161||o.getRange('B6').values[0][0]!==summary.articles_needing_essential_details)throw new Error('Summary mismatch');
console.log((await wb.inspect({kind:'table',range:'Overzicht!A4:C7',include:'values,formulas',tableMaxRows:4,tableMaxCols:3,maxChars:1800})).ndjson);
console.log((await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:20},maxChars:1000})).ndjson);
await fs.mkdir(dir,{recursive:true});
for(const [s,r] of [['Overzicht','A2:C7'],['Voorbeelden','A1:F7'],['Artikelen','A1:F6']]){const b=await wb.render({sheetName:s,range:r,scale:1,format:'png'});await fs.writeFile(path.join(dir,s+'.png'),new Uint8Array(await b.arrayBuffer()));}
const file=await SpreadsheetFile.exportXlsx(wb);await file.save(path.join(dir,'Brauer-specificaties-2026-11-07.xlsx'));console.log(JSON.stringify({articles:catalog.length,exampleRows:erows.length,output:dir}));
