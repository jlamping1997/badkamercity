// Conditional product axes are visible only when their parent choice allows them.
// Unknown conditional choices keep multiple real candidates unresolved.
export function axisActive(axis, options, family) {
  if (axis.dependsOn) {
    const candidates = family.products.filter(product => axis.dependsOn.every(key => product.options[key] === options[key]));
    const values = new Set(candidates.map(product => product.options[axis.key]).filter(value => axis.values.includes(value)));
    return values.size > 1;
  }
  return !axis.when || Object.entries(axis.when).every(([key, value]) => options[key] === value);
}
export function matchingChoices(family, options) {
  return family.products.filter(product => family.axes.every(axis => {
    if (!axisActive(axis, options, family)) return true;
    if ((axis.when || axis.dependsOn) && !axis.values.includes(options[axis.key])) return true;
    return product.options[axis.key] === options[axis.key];
  }));
}
export function resolvedChoice(family, options) {
  const matches = matchingChoices(family, options);
  if (matches.length === 1) return matches[0];
  if (family.kind === 'cabinet') return matches.find(product => product.options.cutouts === options.cutouts) || null;
  return null;
}
