#!/usr/bin/node
const dict = require('./101-data').dict;

const usersByOccurrence = Object.entries(dict).reduce((result, [user, occurrence]) => {
    result[occurrence] = result[occurrence] || [];
    result[occurrence].push(user);
    return result;
}, {});

console.log(usersByOccurrence);
