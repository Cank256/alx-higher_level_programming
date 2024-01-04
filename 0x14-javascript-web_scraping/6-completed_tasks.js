#!/usr/bin/node
/* Computes the number of tasks completed by user id. */

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
    if (!error && response.statusCode === 200) {
        const todos = JSON.parse(body);
        const completed = {};
        todos.forEach(task => {
        if (task.completed) {
            completed[task.userId] = (completed[task.userId] || 0) + 1;
        }
        });
        console.log(completed);
    }
});
