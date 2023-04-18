#!/usr/bin/node
// Script that computes the number of tasks completed by user id.

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) throw err;
  const tasks = JSON.parse(body);
  const dict = {};
  for (const task of tasks) {
    if (task.completed) {
      if (dict[task.userId]) {
        dict[task.userId] += 1;
      } else {
        dict[task.userId] = 1;
      }
    }
  }
  console.log(dict);
});
