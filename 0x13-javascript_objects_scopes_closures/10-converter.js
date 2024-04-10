#!/usr/bin/node
exports.converter = function (base) {
  return function (number) {
    if (base < 2 || base > 16 || isNaN(number)) {
      return 'Invalid input';
    }

    const digits = '0123456789ABCDEF';
    let result = '';

    // divide by base and collect remainders repeatedly
    while (number > 0) {
      const rem = number % base;
      result = digits[rem] + result;
      number = Math.floor(number / base);
    }

    return result;
  };
};
