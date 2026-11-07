"""Offline release verification. No API, credentials, import or publication implementation."""
from pathlib import Path
import json,hashlib,argparse
REQUIRED=['official_package_received','media_inventory_reviewed','source_conflicts_resolved','shopify_identity_and_handle_check_passed','field_and_collection_mapping_rechecked','unpublished_theme_integration_verified','pilot_review_passed','merchant_import_release']
def check(catalog_path,gate):
 errors=[key for key in REQUIRED if gate.get(key) is not True]
 if gate.get('catalog_sha256')!=hashlib.sha256(Path(catalog_path).read_bytes()).hexdigest():errors.append('CATALOG_CHANGED_AFTER_REVIEW')
 for p in json.loads(Path(catalog_path).read_text()):
  if p.get('data_issues'):errors.append('DATA_ISSUES:'+p['sku'])
  if not p['media']['images']:errors.append('NO_OFFICIAL_IMAGE:'+p['sku'])
  if p.get('future_available_date'):errors.append('FUTURE_ITEM_REQUIRES_EXPLICIT_RELEASE:'+p['sku'])
 return {'import_allowed':not errors,'reasons':errors}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--catalog',required=True);p.add_argument('--gate',required=True);a=p.parse_args();r=check(a.catalog,json.loads(Path(a.gate).read_text()));print(json.dumps({'import_allowed':r['import_allowed'],'blocking_reasons':len(r['reasons']),'first_reasons':r['reasons'][:12]}));raise SystemExit(0 if r['import_allowed'] else 2)
