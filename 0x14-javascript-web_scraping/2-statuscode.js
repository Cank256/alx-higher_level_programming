#!/usr/bin/node
/* Displays the status code of a GET request. */

const request = require('request');
const url = process.argv[2];

request(url, function (error, response) {
    if (error) {
        console.log(error);
    } else {
        console.log('code:', response && response.statusCode);
    }
});
