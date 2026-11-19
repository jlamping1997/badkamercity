(function () {
  'use strict';

  const formatters = new Map();

  function createFormatter(locale = 'nl-NL', currency = 'EUR') {
    const key = JSON.stringify([locale, currency]);
    if (formatters.has(key)) return formatters.get(key);

    const regular = new Intl.NumberFormat(locale, { style: 'currency', currency });
    const whole = currency === 'EUR'
      ? new Intl.NumberFormat(locale, {
          style: 'currency', currency, minimumFractionDigits: 0, maximumFractionDigits: 0
        })
      : regular;
    const formatter = Object.freeze({
      format(value) {
        const amount = Number(value);
        return (currency === 'EUR' && amount >= 100 && Number.isInteger(amount) ? whole : regular).format(amount);
      }
    });
    formatters.set(key, formatter);
    return formatter;
  }

  window.BCMoney = Object.freeze({ createFormatter });
})();
