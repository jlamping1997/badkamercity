(function (scope, create) {
  const api = create();
  if (typeof module === 'object' && module.exports) module.exports = api;
  else scope.BCPorcelanosa = api;
})(typeof window === 'undefined' ? this : window, function () {
  const scale = 10000;
  const fields = ['type', 'color', 'finish', 'size', 'thickness'];
  function units(value) {
    const text = String(value ?? '').trim();
    if (!/^\d{1,7}(?:[.,]\d{1,4})?$/.test(text)) return null;
    const [whole, fraction = ''] = text.replace(',', '.').split('.');
    const result = Number(whole) * scale + Number(fraction.padEnd(4, '0'));
    return Number.isSafeInteger(result) && result > 0 ? result : null;
  }
  function calculate(value, waste, boxUnits, priceCents, threshold = 500000) {
    const percentage = waste === true ? 10 : waste === false ? 0 : Number(waste);
    if (![0, 5, 10, 15, 20].includes(percentage)) return null;
    const needed = units(value);
    if (!needed || !Number.isSafeInteger(boxUnits) || boxUnits < 1 || !Number.isSafeInteger(priceCents) || priceCents < 0) return null;
    const boxes = Math.ceil(needed * (100 + percentage) / (boxUnits * 100));
    const result = calculateBoxes(boxes, boxUnits, priceCents, threshold);
    return result ? { ...result, needed, required: Math.ceil(needed * (100 + percentage) / 100) } : null;
  }
  function calculateBoxes(value, boxUnits, priceCents, threshold = 500000) {
    const text = String(value ?? '').trim();
    if (!/^\d{1,10}$/.test(text)) return null;
    const boxes = Number(text);
    if (!Number.isSafeInteger(boxes) || boxes < 1 || boxes > 2147483647 || !Number.isSafeInteger(boxUnits) || boxUnits < 1 || !Number.isSafeInteger(priceCents) || priceCents < 0) return null;
    const supplied = boxes * boxUnits;
    const total = boxes * priceCents;
    if (!Number.isSafeInteger(supplied) || !Number.isSafeInteger(total)) return null;
    return { boxes, supplied, total, needed: supplied, required: supplied, contact: supplied > threshold };
  }
  function choices(products, current, field) {
    const prefix = fields.slice(0, fields.indexOf(field));
    const found = products.filter(p => prefix.every(k => String(p[k]) === String(current[k])));
    return [...new Map(found.map(p => [String(p[field]), p])).values()];
  }
  function choose(products, current, field, value) {
    const index = fields.indexOf(field);
    if (index < 0) return null;
    const prefix = fields.slice(0, index);
    const candidates = products.filter(p => String(p[field]) === String(value) && prefix.every(k => String(p[k]) === String(current[k])));
    const score = p => fields.slice(index + 1).reduce((n, key, i) => n + (String(p[key]) === String(current[key]) ? Math.pow(20, fields.length - i) : 0), 0);
    return candidates.sort((a, b) => score(b) - score(a) || Math.abs(a.area - current.area) - Math.abs(b.area - current.area) || Number(a.thickness) - Number(b.thickness) || a.sku.localeCompare(b.sku))[0] || null;
  }
  return { scale, fields, units, calculate, calculateBoxes, choices, choose };
});

