#!/usr/bin/env python3
"""Offline component source/field index. Outputs metadata only, never values.

Use a fresh read-only theme snapshot and manifest. Git candidates are exact blobs
from the explicit baseline commit, not possibly modified working-tree files.
"""
import argparse
import collections
import hashlib
import json
import re
import sqlite3
import subprocess
from pathlib import Path

from architecture_scan import mask_comments


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def build(args):
    snapshot=args.snapshot.resolve()
    output=args.output.resolve()
    if output==snapshot or snapshot in output.parents:
        raise ValueError('Output may not be inside the theme snapshot')
    registry=json.loads(args.registry.read_text())
    manifest=json.loads(args.manifest.read_text())
    files={row['filename']:row for row in manifest['files']}
    repo=args.repo.resolve()
    baseline=subprocess.check_output(['git','rev-parse',args.baseline+'^{commit}'],cwd=repo,text=True).strip()
    tree=subprocess.check_output(['git','ls-tree','-rz',baseline],cwd=repo).split(b'\0')
    tracked=collections.defaultdict(list)
    for item in tree:
        if not item:continue
        meta,name=item.split(b'\t',1)
        mode,kind,digest=meta.split()
        if kind==b'blob':tracked[digest.decode()].append(name.decode())
    components=collections.defaultdict(list)
    for component in registry['components']:
        if not (args.registry.parent/component['document']).is_file():
            raise ValueError('Missing component document: '+component['document'])
        for name in component['sources']:components[name].append(component['id'])
    source_rows=[]
    consumers=collections.defaultdict(list)
    dynamic=[]
    for name,ids in sorted(components.items()):
        path=snapshot/name
        if not path.is_file() or name not in files:raise ValueError('Missing source: '+name)
        raw=path.read_bytes()
        md5=hashlib.md5(raw).hexdigest()
        if md5!=files[name]['checksumMd5'] or len(raw)!=int(files[name]['size']):
            raise ValueError('Source does not match metadata: '+name)
        blob=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        text=raw.decode('utf-8-sig')
        source_rows.append({'path':name,'components':ids,'md5':md5,'sha256':hashlib.sha256(raw).hexdigest(),
                            'bytes':len(raw),'lines':len(text.splitlines()),'gitBlobSha':blob,
                            'exactTrackedMatchesAtBaseline':tracked.get(blob,[])})
        clean=mask_comments(text)
        for line_no,line in enumerate(clean.splitlines(),1):
            for match in re.finditer(r'metafields\.([A-Za-z_]\w*)\.([A-Za-z_]\w*)',line):
                key='.'.join(match.groups())
                consumers[key].append({'source':name,'line':line_no,'components':ids})
            if re.search(r'metafields(?:\.\w+)?\[',line):
                dynamic.append({'source':name,'line':line_no,'components':ids})
    fields=collections.defaultdict(list)
    if args.product_db:
        db=sqlite3.connect(args.product_db.resolve().as_uri()+'?mode=ro',uri=True)
        for owner,namespace,key,kind,count in db.execute('SELECT owner_type,namespace,key,type,COUNT(*) FROM metafields GROUP BY owner_type,namespace,key,type'):
            fields[namespace+'.'+key].append({'ownerType':owner,'type':kind,'records':count})
        db.close()
    index={'schemaVersion':1,'themeId':manifest['theme_id'],'manifestCheckedAt':manifest.get('checkedAt'),
           'baselineCommit':baseline,'sourceFiles':len(source_rows),'components':registry['components'],
           'coverage':'Curated source/line index. Not a complete runtime dependency graph.',
           'files':source_rows}
    field_index={'schemaVersion':1,'literalKeyCount':len(consumers),'sources':len(source_rows),
                 'dataCountsSource':'DOC-01 private product export, not a new live Admin read' if args.product_db else None,
                 'limitations':['Literal references only; dynamic mapping and nested JSON keys not fully resolved.',
                                'Presence/type/count is not truth, visibility, consumer reachability, or permission to change data.',
                                'No values, IDs, descriptions, costs, URLs or stock rows are copied.'],
                 'fields':[{'key':key,'consumers':rows,'observedFields':fields.get(key,[])} for key,rows in sorted(consumers.items())],
                 'dynamicConsumerLocations':dynamic}
    output.mkdir(parents=True,exist_ok=True)
    write_json(output/'source-index.json',index)
    write_json(output/'field-consumers.json',field_index)
    return {'sourceFiles':len(source_rows),'literalKeys':len(consumers),'dynamicConsumerLocations':len(dynamic),
            'allIndexedBytesMatchManifest':True,'baselineCommit':baseline}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--snapshot',type=Path,required=True)
    parser.add_argument('--manifest',type=Path,required=True)
    parser.add_argument('--registry',type=Path,required=True)
    parser.add_argument('--repo',type=Path,required=True)
    parser.add_argument('--baseline',required=True)
    parser.add_argument('--product-db',type=Path)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    print(json.dumps(build(args)))


if __name__=='__main__':main()
