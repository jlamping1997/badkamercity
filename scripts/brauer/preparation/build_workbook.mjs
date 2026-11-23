import fs from 'node:fs/promises';
import path from 'node:path';
import {Workbook,SpreadsheetFile} from '@oai/artifact-tool';

const root=process.argv[2],outputDir=path.join(root,'outputs','brauer-19');
const data=JSON.parse(await fs.readFile(path.join(root,'prepared','sheet-data.json'),'utf8'));
const summary=JSON.parse(await fs.readFile(path.join(root,'prepared','summary.json'),'utf8'));
const catalog=JSON.parse(await fs.readFile(path.join(root,'prepared','catalog.json'),'utf8'));
const groups=JSON.parse(await fs.readFile(path.join(root,'prepared','families.json'),'utf8'));
const wb=Workbook.create();
for(const name of ['Overzicht','Producten','Keuzegroepen','Uitzonderingen'])wb.worksheets.add(name);
const fmt={name:'Arial',size:10,color:'#223849'};
function column(i){let s='';for(i++;i;i=Math.floor((i-1)/26))s=String.fromCharCode(65+(i-1)%26)+s;return s;}
function table(name,headers,rows,widths){
 const sh=wb.worksheets.getItem(name);sh.showGridLines=false;
 const last=column(headers.length-1),end=rows.length+1;
 const range=sh.getRange(`A1:${last}${end}`);range.values=[headers,...rows];range.format.font=fmt;range.format.rowHeight=30;range.format.verticalAlignment='center';
 const head=sh.getRange(`A1:${last}1`);head.format={fill:'#12334C',font:{...fmt,bold:true,color:'#FFFFFF'},wrapText:true,rowHeight:34,horizontalAlignment:'center'};
 widths.forEach((width,i)=>{sh.getRange(`${column(i)}1:${column(i)}${end}`).format.columnWidth=width;});
 const t=sh.tables.add(`A1:${last}${end}`,true,'Brauer'+name);t.showFilterButton=true;
 sh.freezePanes.freezeRows(1);sh.freezePanes.freezeColumns(name==='Producten'?2:1);
 return sh;
}
const rows=data.product_rows.map(row=>row.map((v,i)=>i===9?(v?new Date(v+'T00:00:00Z'):null):v));
const products=table('Producten',data.product_headers,rows,[22,20,30,95,18,36,80,18,44,20,16,12,20,65,65,55,55]);
products.getRange(`N2:Q${rows.length+1}`).format.fill='#FFF4D6';
products.getRange(`N2:Q${rows.length+1}`).format.wrapText=true;
products.getRange(`A2:A${rows.length+1}`).setNumberFormat('@');
// Values remain strings in XLSX. Explicit digits also avoid scientific display in the preview engine.
products.getRange(`B2:B${rows.length+1}`).setNumberFormat('0000000000000');
products.getRange(`E2:E${rows.length+1}`).setNumberFormat('"€" #,##0.00');
products.getRange(`J2:J${rows.length+1}`).setNumberFormat('dd-mm-yyyy');
products.getRange(`D2:D${rows.length+1}`).format.wrapText=true;
products.getRange(`I2:I${rows.length+1}`).format.wrapText=true;
products.getRange(`H2:H${rows.length+1}`).conditionalFormats.add('containsText',{text:'CONTROLEREN',format:{fill:'#FCE3DF',font:{color:'#84231B'}}});
const gr=groups.map(g=>[g.id,g.product_type,g.name,g.sku_count,g.status,g.axes.map(a=>a.label+' ('+a.values.length+')').join(', '),Object.entries(g.fixed_partitions).map(([k,v])=>({depth:'Diepte-uitvoering',height:'Hoogtemaat bron'}[k]||k)+': '+v).join(', ')]);
const fam=table('Keuzegroepen',data.family_headers,gr,[36,32,80,14,20,70,40]);fam.getRange(`F2:G${gr.length+1}`).format.wrapText=true;
const issues=table('Uitzonderingen',data.issue_headers,data.issue_rows,[22,85,70]);issues.getRange(`B2:C${data.issue_rows.length+1}`).format.wrapText=true;issues.getRange(`A2:C${data.issue_rows.length+1}`).format.rowHeight=42;
const overview=wb.worksheets.getItem('Overzicht');overview.showGridLines=false;overview.tabColor='#12334C';
overview.getRange('A1:D28').format.font=fmt;overview.getRange('A1:A28').format.columnWidth=48;overview.getRange('B1:B28').format.columnWidth=22;overview.getRange('C1:C28').format.columnWidth=70;
overview.getRange('A2').values=[['BRAUER importvoorbereiding']];overview.getRange('A2').format.font={...fmt,size:14};overview.getRange('A2:C2').format.rowHeight=28;
overview.getRange('A4:C4').values=[['Onderdeel','Aantal / status','Betekenis']];overview.getRange('A4:C4').format={fill:'#12334C',font:{...fmt,bold:true,color:'#FFFFFF'},rowHeight:26};
overview.getRange('A5:C15').values=[
 ['Artikelen',null,'Alle unieke fabrikantartikelnummers uit de drie prijslijsten'],
 ['Keuzegroepen',null,'Technisch verschillende uitvoeringen blijven herkenbaar'],
 ['Bronconflicten',null,'Artikelen met verschillende materiaal- of afwerkingswaarden'],
 ['Niet-unieke keuzewaarden',null,'Verschillende artikelnummers waarvoor extra uitleg nodig is'],
 ['Toekomstige artikelen',null,'Bron noemt leverbaar vanaf 1 februari 2027'],
 ['Import toegestaan',null,'Wacht op complete media, controle en latere vrijgave'],
 ['Groepen te controleren',summary.families_to_review,'Zie de uitzonderingen en de status bij iedere groep'],
 ['Officiële afbeeldingen / PDF’s','Wachten','Bestanden worden straks exact op artikelnummer gekoppeld'],
 ['Kleurkeuze','Eerst','Zes kleuren zichtbaar, daarna Bekijk meer kleuren'],
 ['Spiegelkastkleuren','Decorstalen','Deurrichting verschijnt alleen bij meerdere echte keuzes'],
 ['Kasten 120 / 160 cm','Losse producten','120 cm halfhoog en 160 cm hoog blijven afzonderlijk']
 ];
overview.getRange('B5:B10').formulas=[
 [`=COUNTA(Producten!A2:A${rows.length+1})`],
 [`=COUNTA(Keuzegroepen!A2:A${gr.length+1})`],
 [`=COUNTIF(Producten!I2:I${rows.length+1},"BRONCONFLICT")`],
 [`=COUNTIF(Producten!I2:I${rows.length+1},"KEUZECOMBINATIE_NIET_UNIEK")`],
 [`=COUNTA(Producten!J2:J${rows.length+1})`],
 [`=COUNTIF(Producten!M2:M${rows.length+1},"JA")`]
 ];
overview.getRange('A5:C15').format.rowHeight=32;overview.getRange('C5:C15').format.wrapText=true;overview.getRange('B5:B11').setNumberFormat('#,##0');
overview.getRange('A16:C16').values=[['Maatbronconflicten',null,'Drie eerdere verschillen blijven apart tot de juiste tekeningen er zijn']];overview.getRange('B16').formulas=[[`=COUNTIF(Producten!I2:I${rows.length+1},"MAATBRONCONFLICT")`]];overview.getRange('A16:C16').format.rowHeight=32;overview.getRange('C16').format.wrapText=true;
overview.getRange('A18:C18').values=[['Bronbestand','Bronregels','Datum prijslijst']];overview.getRange('A18:C18').format={fill:'#12334C',font:{...fmt,bold:true,color:'#FFFFFF'},rowHeight:26};
overview.getRange('A19:C21').values=summary.source_files.map(s=>[s.name,s.rows,s.name.includes('28-10')?'28 oktober 2026':'13 oktober 2026']);overview.getRange('A19:A21').format.wrapText=true;overview.getRange('A19:C21').format.rowHeight=38;
overview.getRange('A24:C25').values=[['Leveranciersdata','Ongewijzigd','Dit overzicht is een nieuwe voorbereiding; de vorige productbasis blijft bewaard.'],['Werkelijke import','Nog niet uitgevoerd','Ook geen conceptproducten, media-upload of publicatie in Shopify.']];overview.getRange('C24:C25').format.wrapText=true;overview.getRange('A24:C25').format.rowHeight=34;
wb.recalculate();
const inspect=await wb.inspect({kind:'table',range:'Overzicht!A4:C15',include:'values,formulas',tableMaxRows:12,tableMaxCols:3,maxChars:5000});console.log(inspect.ndjson);
const values=overview.getRange('B5:B10').values.flat();const expected=[13161,summary.families,27,12,163,0];if(JSON.stringify(values)!==JSON.stringify(expected))throw new Error('Summary calculation mismatch '+JSON.stringify(values));
const errors=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:20},maxChars:2000});console.log(errors.ndjson);
await fs.mkdir(outputDir,{recursive:true});
for(const [name,range] of [['Overzicht','A1:C16'],['Producten','A1:E6'],['Keuzegroepen','A1:E6'],['Uitzonderingen','A1:C6'],['Aanvullen','N1:Q5']]){
 const b=await wb.render({sheetName:name==='Aanvullen'?'Producten':name,range,scale:1,format:'png'});await fs.writeFile(path.join(outputDir,name+'.png'),new Uint8Array(await b.arrayBuffer()));
}
const file=await SpreadsheetFile.exportXlsx(wb);await file.save(path.join(outputDir,'Brauer-importvoorbereiding-2026-11-07.xlsx'));
console.log(JSON.stringify({output:path.join(outputDir,'Brauer-importvoorbereiding-2026-11-07.xlsx'),articles:rows.length,groups:gr.length}));
