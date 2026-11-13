"""Offline tile-format proposals. No network or store mutations.

Exact dimensions are inputs, never rewritten. A production consumer should use
reviewed, versioned mappings from ReviewedManifest; it should not infer new
nominal formats during a scheduled sync.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from decimal import Decimal, InvalidOperation
import re
from typing import Any, Iterable, Mapping

D = Decimal
MAX_DELTA_MM = D('8')
MAX_RELATIVE_DELTA = D('0.03')
APPROVED_STATUSES = frozenset({'OWNER_APPROVED_RULE', 'SOURCE_VERIFIED'})
# These are review hints, not definitive assertions about the physical outline.
# E.g.Circle or Diamond may describe relief/pattern on a rectangular tile.
SHAPE_REVIEW_HINT = re.compile(r'\b(?:hexagon\w*|hexa|octogon\w*|octagon\w*|escama|scale|zeshoek\w*|round|rond|ronde|circular|circle|arabesque|fishscale|fish scale|rhomb\w*|diamond|picket)\b', re.I)
MOSAIC_SHEET_HINT = re.compile(r'moza[iï]e?k|mosaic|sheet|tegelmat|visgraatmat', re.I)

# Candidate labels, not manufacturer attestations. Both sides are millimetres.
# Small / fractional established formats are intentional targets in their own
# right; the system does not round every number to a whole centimetre.
DEFAULT_TARGETS = (
    ('50', '50'), ('50', '200'), ('50', '250'), ('50', '300'),
    ('65', '200'), ('75', '150'), ('75', '300'),
    ('100', '100'), ('100', '200'), ('100', '300'),
    ('112.5', '450'), ('125', '250'), ('130', '130'),
    ('150', '150'), ('150', '300'), ('160', '160'),
    ('200', '200'), ('200', '400'), ('200', '600'), ('200', '1200'),
    ('250', '250'), ('250', '400'), ('250', '500'),
    ('300', '300'), ('300', '600'), ('300', '900'), ('300', '1200'),
    ('330', '330'), ('333', '333'), ('335', '335'),
    ('400', '400'), ('400', '800'), ('450', '450'), ('500', '500'),
    ('600', '600'), ('600', '1200'), ('750', '750'),
    ('800', '800'), ('800', '1600'), ('900', '900'),
    ('1000', '1000'), ('1200', '1200'), ('1200', '1800'), ('1200', '2000'),
)


def decimal_mm(value: Any) -> Decimal:
    """Parse an explicitly-mm numeric value; never silently infer/convert units."""
    if isinstance(value, bool) or value is None:
        raise ValueError('Missing or nonnumeric dimension')
    text = str(value).strip()
    # A comma decimal is accepted; mixed separators and unit suffixes are not.
    if not re.fullmatch(r'[+]?(?:\d+(?:[.,]\d+)?|[.,]\d+)', text):
        raise ValueError('Dimension must be a plain millimetre number')
    try:
        result = D(text.replace(',', '.'))
    except InvalidOperation as exc:
        raise ValueError('Invalid decimal dimension') from exc
    if not result.is_finite() or result <= 0:
        raise ValueError('Dimension must be finite and positive')
    return result


def number(value: Decimal) -> str:
    return format(value.normalize(), 'f')


def pair(a: Any, b: Any) -> tuple[Decimal, Decimal]:
    return tuple(sorted((decimal_mm(a), decimal_mm(b))))  # type: ignore[return-value]


def format_key(p: tuple[Decimal, Decimal]) -> str:
    return 'x'.join(number(v / 10) for v in p)


def format_label(p: tuple[Decimal, Decimal]) -> str:
    return ' × '.join(number(v / 10).replace('.', ',') for v in p) + ' cm'


@dataclass(frozen=True)
class TileContext:
    shape: str
    measure_basis: str
    source_unit: str = 'mm'
    vendor: str = ''
    series: str = ''
    title: str = ''
    product_type: str = ''

    def blocked_reason(self) -> str | None:
        if self.source_unit != 'mm':
            return 'Source unit is not explicitly millimetres'
        if self.shape.casefold() not in {'rectangular', 'square'}:
            return 'Shape is not confirmed rectangular or square'
        if self.measure_basis.casefold() != 'piece':
            return 'Dimension basis is not confirmed to be one tile piece'
        text = ' '.join((self.title, self.product_type)).casefold()
        if MOSAIC_SHEET_HINT.search(text) or SHAPE_REVIEW_HINT.search(text):
            return 'Mosaic, sheet or shape-related name requires separate shape/basis review'
        return None


@dataclass(frozen=True)
class Decision:
    raw_input_mm: tuple[str, str]
    raw_pair_mm: tuple[str, str] | None
    nominal_pair_mm: tuple[str, str] | None
    format_key: str | None
    label: str | None
    status: str
    reason: str
    delta_mm: tuple[str, str] | None = None
    candidates: tuple[str, ...] = ()
    approval_basis: str | None = None
    eligible_for_plan: bool = False

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _decision(raw_input: tuple[str, str], raw: tuple[Decimal, Decimal] | None,
              target: tuple[Decimal, Decimal] | None, status: str, reason: str,
              *, candidates: Iterable[str] = (), approval_basis: str | None = None,
              ready: bool = False) -> Decision:
    return Decision(
        raw_input_mm=raw_input,
        raw_pair_mm=tuple(number(v) for v in raw) if raw else None,
        nominal_pair_mm=tuple(number(v) for v in target) if target else None,
        format_key=format_key(target) if target else None,
        label=format_label(target) if target else None,
        status=status, reason=reason,
        delta_mm=tuple(number(abs(a-b)) for a,b in zip(raw,target)) if raw and target else None,
        candidates=tuple(candidates), approval_basis=approval_basis,
        eligible_for_plan=ready,
    )


@dataclass(frozen=True)
class ReviewedRule:
    raw: tuple[Decimal, Decimal]
    nominal: tuple[Decimal, Decimal]
    status: str
    approval_basis: str
    vendor: str = ''
    series: str = ''

    def matches(self, raw: tuple[Decimal, Decimal], ctx: TileContext) -> bool:
        return (self.raw == raw
                and (not self.vendor or self.vendor.casefold() == ctx.vendor.strip().casefold())
                and (not self.series or self.series.casefold() == ctx.series.strip().casefold()))


class ReviewedManifest:
    """Explicit approval map. Proposed rows cannot enter this index contract."""
    def __init__(self, document: Mapping[str, Any]):
        if document.get('version') != 'tile-nominal-v1' or document.get('unit') != 'mm':
            raise ValueError('Unsupported reviewed-manifest version or unit')
        if not isinstance(document.get('rules', []), list):
            raise ValueError('Reviewed rules must be a list')
        rules: list[ReviewedRule] = []
        seen: dict[tuple[Any, ...], ReviewedRule] = {}
        for row in document.get('rules', []):
            if not isinstance(row, Mapping) or any(not isinstance(row.get(k), (list,tuple)) or len(row[k]) != 2 for k in ('raw_mm','nominal_mm')):
                raise ValueError('Each reviewed rule needs two explicit raw and nominal sides')
            raw, nominal = pair(*row['raw_mm']), pair(*row['nominal_mm'])
            if row.get('status') not in APPROVED_STATUSES or not isinstance(row.get('approval_basis'),str) or not row['approval_basis'].strip():
                raise ValueError('Only explicitly approved rules with evidence can be used')
            scope = row.get('scope') or {}
            if not isinstance(scope, Mapping) or set(scope) - {'vendor','series'}:
                raise ValueError('Scope must use only explicit vendor/series keys')
            if any(not isinstance(v,str) for v in scope.values()):
                raise ValueError('Scope values must be explicit strings')
            vendor, series = str(scope.get('vendor', '')).strip(), str(scope.get('series', '')).strip()
            if series and not vendor:
                raise ValueError('A series-specific rule must include the manufacturer/vendor')
            rule = ReviewedRule(raw, nominal, row['status'], row['approval_basis'], vendor, series)
            identity = (raw, vendor.casefold(), series.casefold())
            if identity in seen:
                raise ValueError('Duplicate or conflicting reviewed rule for the same raw pair/scope')
            seen[identity] = rule
            rules.append(rule)
        self.rules = tuple(rules)

    def match(self, raw: tuple[Decimal, Decimal], ctx: TileContext) -> ReviewedRule | None:
        matches = [r for r in self.rules if r.matches(raw, ctx)]
        if not matches:
            return None
        # Series-specific overrides vendor-specific overrides global; source
        # dimensions remain unchanged. Same-specificity ambiguity is impossible
        # under this manifest's duplicate/scope restrictions.
        return max(matches, key=lambda r: bool(r.vendor) + bool(r.series))


def classify_pair(width_mm: Any, length_mm: Any, *, context: TileContext,
                  targets: Iterable[tuple[Any, Any]] = DEFAULT_TARGETS,
                  reviewed: ReviewedManifest | None = None) -> Decision:
    """Return an orientation-independent candidate without mutating source data.

    Only the explicit owner 596->600 example, unchanged recognized pairs, and
    reviewed mappings can be marked ready. All other nearest-pair suggestions
    remain proposals. Multiple compatible targets are blocked rather than
    silently choosing a nearest one.
    """
    original = (str(width_mm), str(length_mm))
    try:
        raw = pair(width_mm, length_mm)
    except (ValueError, TypeError):
        return _decision(original, None, None, 'BLOCKED_INVALID', 'Missing, zero, invalid or unit-bearing dimension')
    blocked = context.blocked_reason()
    if blocked:
        return _decision(original, raw, None, 'BLOCKED_CONTEXT', blocked)
    if reviewed:
        rule = reviewed.match(raw, context)
        if rule:
            return _decision(original, raw, rule.nominal, rule.status,
                             'Explicit reviewed raw-pair mapping', approval_basis=rule.approval_basis, ready=True)
    choices = sorted(set(pair(*p) for p in targets))
    if raw in choices:
        return _decision(original, raw, raw, 'EXACT_RECOGNIZED', 'Exact recognized candidate label; dimensions unchanged', ready=True)
    compatible = [p for p in choices if all(
        abs(a-b) <= MAX_DELTA_MM and abs(a-b) <= b * MAX_RELATIVE_DELTA
        for a,b in zip(raw,p)
    )]
    if not compatible:
        if D('596') in raw:
            # The owner's explicit side mapping remains valid for a real pair
            # which isn't in the illustrative common-pair list, e.g.596x1500.
            # No other side is rounded or paired with a different product.
            target = tuple(D('600') if v == D('596') else v for v in raw)
            return _decision(original, raw, target, 'OWNER_APPROVED_RULE',
                             'Owner 596-to-600 side rule applied to this actual source pair; other side left exact',
                             approval_basis='USER_2026-11-08_59_6_TO_60_FILTER_ONLY', ready=True)
        return _decision(original, raw, None, 'BLOCKED_UNKNOWN', 'No bounded, recognized nominal pair fits; preserve exact dimensions')
    if len(compatible) != 1:
        return _decision(original, raw, None, 'BLOCKED_AMBIGUOUS', 'More than one nominal pair fits; explicit review required',
                         candidates=(format_label(p) for p in compatible))
    target = compatible[0]
    changed = [(a,b) for a,b in zip(raw,target) if a != b]
    owner_example = changed and all(a == D('596') and b == D('600') for a,b in changed)
    if owner_example:
        return _decision(original, raw, target, 'OWNER_APPROVED_RULE',
                         'Owner explicitly permits 59.6 cm to be grouped as 60 cm in tile filters',
                         approval_basis='USER_2026-11-08_59_6_TO_60_FILTER_ONLY', ready=True)
    return _decision(original, raw, target, 'PROPOSED',
                     'Candidate pair fits max 8 mm and 3% per side; review before adding to a versioned index manifest',
                     candidates=(format_label(target),))


def approved_rule_from_decision(decision: Decision, *, context: TileContext) -> dict[str, Any]:
    """Export approved changed rules only, never silently promote a proposal."""
    if decision.status not in APPROVED_STATUSES or not decision.eligible_for_plan:
        raise ValueError('Decision has no explicit approval')
    if not decision.raw_pair_mm or not decision.nominal_pair_mm or not decision.approval_basis:
        raise ValueError('Incomplete approved decision')
    if context.blocked_reason():
        raise ValueError('Unsupported context cannot create a reviewed rectangle rule')
    scope = {k:v for k,v in [('vendor',context.vendor.strip()),('series',context.series.strip())] if v}
    if 'series' in scope and 'vendor' not in scope:
        raise ValueError('Series requires vendor scope')
    return {'raw_mm':list(decision.raw_pair_mm),'nominal_mm':list(decision.nominal_pair_mm),
            'status':decision.status,'approval_basis':decision.approval_basis,'scope':scope}
