import fs from 'node:fs/promises';
import {FileBlob,SpreadsheetFile} from '@oai/artifact-tool';
const [file,output,firstRow]=process.argv.slice(2);
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(file));
const r=await wb.render({sheetName:'Aanvullingen',range:`A${firstRow}:F${Number(firstRow)+4}`,scale:1,format:'png'});
await fs.writeFile(output,new Uint8Array(await r.arrayBuffer()));
