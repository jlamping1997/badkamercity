import fs from 'node:fs/promises';
import path from 'node:path';
import {FileBlob,SpreadsheetFile} from '@oai/artifact-tool';

const root=path.resolve(process.argv[2]);
const source=path.resolve(process.argv[3]);
const outputDir=path.join(root,'outputs','brauer-27-benefits');
const catalog=JSON.parse(await fs.readFile(path.join(root,'prepared/catalog.json'),'utf8'));
const records=JSON.parse(await fs.readFile(path.join(root,'prepared/product-benefits.json'),'utf8'));
console.log('Approved benefit records loaded');
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(source));
console.log('Source workbook imported');
const proofs=new Map(records.map(r=>[r.sku,r]));
let s,existing=false;
try{s=wb.worksheets.getItem('Pluspunten');existing=Boolean(s);}catch{}
if(!s)s=wb.worksheets.add('Pluspunten');
if(existing){
 for(const t of s.tables.items)t.delete();
 s.getUsedRange()?.clear({applyTo:'all'});
}
console.log('Benefits sheet selected');
s.showGridLines=false;
const font={name:'Arial',size:10,color:'#213647'};
const rows=catalog.map(p=>{
 const items=proofs.get(p.sku).items;
 if(proofs.get(p.sku).ean!==p.ean)throw new Error('Benefits identity differs: '+p.sku);
 const fields=[...new Set(items.flatMap(x=>x.basis.map(b=>b.field+' = '+b.value)))].join('\n');
 const sources=[...new Set(items.flatMap(x=>x.basis.flatMap(b=>b.evidence.url?[b.evidence.url]:b.evidence.source_refs.map(r=>r.file+' | '+r.sheet+':'+r.row))))].join('\n');
 return [p.sku,p.ean,p.product_type,p.title,...Array.from({length:4},(_,i)=>items[i]?.text||''),fields,sources];
});
const end=rows.length+5;
s.getRange('A2').values=[['Pluspunten per artikel']];
s.getRange('A2').format.font={...font,size:14};
s.getRange('A3').values=[['Alleen bevestigde kenmerken van het exacte artikel. Lege vakken blijven open. Shopify-import geblokkeerd.']];
s.getRange('A3').format.font={...font,italic:true};
s.getRange('A5:J5').values=[['Artikelnummer','EAN','Producttype','Product','Pluspunt 1','Pluspunt 2','Pluspunt 3','Pluspunt 4','Bewijsvelden','Bronbestand of pagina']];
s.getRange(`A6:J${end}`).values=rows;
console.log('Benefit rows written');
s.getRange(`A5:J${end}`).format={font,rowHeight:48,verticalAlignment:'center'};
s.getRange(`A6:B${end}`).setNumberFormat('@');
s.getRange(`C6:J${end}`).format.wrapText=true;
s.getRange('A5:J5').format={fill:'#15374F',font:{...font,color:'#FFFFFF',bold:true},rowHeight:38,wrapText:true,horizontalAlignment:'center'};
for(const [i,w] of [25,22,32,88,40,40,40,40,62,100].entries()){
 const col=String.fromCharCode(65+i);s.getRange(`${col}1:${col}${end}`).format.columnWidth=w;
}
const heights=rows.map(r=>{
 const lines=Math.max(Math.ceil(String(r[3]).length/80),...r.slice(4,8).map(x=>Math.ceil(String(x).length/34)),...r.slice(8).map((x,j)=>String(x).split('\n').reduce((n,line)=>n+Math.max(1,Math.ceil(line.length/(j===0?57:94))),0)));
 return Math.max(48,lines*15+12);
});
let start=0,heightRuns=0;
for(let i=1;i<=heights.length;i++)if(i===heights.length||heights[i]!==heights[start]){
 if(heights[start]!==48){s.getRange(`A${start+6}:J${i+5}`).format.rowHeight=heights[start];heightRuns++;}
 start=i;
}
console.log(JSON.stringify({formatted_height_runs:heightRuns}));
s.tables.add(`A5:J${end}`,true,'BrauerProductBenefits');
s.freezePanes.freezeRows(5);s.freezePanes.freezeColumns(1);
wb.recalculate();
console.log((await wb.inspect({kind:'table',range:'Pluspunten!A5:H7',tableMaxRows:3,tableMaxCols:8,maxChars:2200})).ndjson);
console.log((await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:15},maxChars:1000})).ndjson);
await fs.mkdir(outputDir,{recursive:true});
const selections=[['Eerste-pluspunten',0]];
for(const [name,selector] of [
 ['Doucheset',p=>p.sku==='5-GM-077'],
 ['Draaibare-uitloop',p=>p.sku==='5-CE-003'],
 ['Doucheglas',p=>p.product_type==='Douchecabines'&&proofs.get(p.sku).items.length>0],
 ['Meubel',p=>p.product_type==='Onderkasten'&&proofs.get(p.sku).items.length>0],
]){
 const idx=catalog.findIndex(selector);if(idx<0)throw new Error('Missing review example '+name);selections.push([name,idx]);
}
for(const [name,idx] of selections){
 console.log('Rendering '+name);
 const range=name==='Eerste-pluspunten'?'A2:H7':`C${idx+6}:H${idx+6}`;
 const blob=await wb.render({sheetName:'Pluspunten',range,scale:1,format:'png'});
 await fs.writeFile(path.join(outputDir,name+'.png'),new Uint8Array(await blob.arrayBuffer()));
}
const output=await SpreadsheetFile.exportXlsx(wb);
await output.save(path.join(outputDir,'Brauer-specificaties-2026-11-07.xlsx'));
console.log(JSON.stringify({articles:catalog.length,rows_with_benefits:rows.filter(r=>r[4]).length,benefits:records.reduce((n,p)=>n+p.items.length,0),new_sheet:'Pluspunten',original_sheets:5}));
