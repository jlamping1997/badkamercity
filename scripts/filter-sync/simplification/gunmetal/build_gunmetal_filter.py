#!/usr/bin/env python3
"""Bundle reviewed public modules; no private runtime is read."""
import hashlib
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
def build():
    lifecycle=(HERE.parent/'tile-looks/release/apply_tile_look_filter.py').read_text().rstrip()+'\n'
    patch=(HERE/'gunmetal_worker_patch.py').read_text()
    template=(HERE/'apply_gunmetal_filter.py').read_text()
    for key,value in [('LIFECYCLE_SOURCE',lifecycle),('PATCH_SOURCE',patch)]:
        anchor=key+' = None';assert template.count(anchor)==1
        template=template.replace(anchor,key+' = '+ascii(value),1)
    data=template.encode('ascii');compile(template,'<gunmetal-release>','exec')
    output=HERE/'repair_gunmetal_filter.py';output.write_bytes(data)
    manifest={'installer':output.name,'installer_bytes':len(data),'installer_sha256':hashlib.sha256(data).hexdigest(),'base_worker_sha256':'79f676d035fdd6d250e2daec51b886d1aa54c117707718d7ea9695300c21c43d','base_api_sha256':'3a7701134be7ac55b0a83436ceb16ebb19ac0a88aba17c283490f90047f02094','api_source_unchanged':True,'target_worker_hash':'computed deterministically from the exactly hash-checked installed base and reviewed insertion; reverse-check on repeat','source':'f_kleur_exact','derived_field':'f_kleur','new_value':'Gunmetal','recommended_order':'image-then-data-completeness-with-vendor-type-series-round-robin-v1','internal_default_sorting_field':'bc_recommendation_rank','cinto_widths_required':{'38.4177':600,'38.4178':800},'raw_source_and_shopify_unchanged_by_installer':True,'requires_existing_tile_looks':True,'private_runtime_or_catalog_embedded':False,'transport_ascii':True,'lifecycle_source_sha256':hashlib.sha256(lifecycle.encode()).hexdigest()}
    (HERE/'gunmetal-release.json').write_text(json.dumps(manifest,indent=2)+'\n');return manifest

if __name__=='__main__':print(json.dumps(build(),indent=2))
