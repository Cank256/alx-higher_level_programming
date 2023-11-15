#!/usr/bin/node

exports.esrever = function (list) {
  return list.reduceRight((reversed, element) => {
    reversed.push(element);
    return reversed;
  }, []);
};
