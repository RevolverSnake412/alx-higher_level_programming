#!/usr/bin/node
const request = require('request');
const array = {};
let comp = 1;
let tempId = 1;

request(process.argv[2], function (error, response, body) {
  if (!error) {
    const parsedJSON = JSON.parse(body);
    for (const i in parsedJSON) {
      if (tempId !== parsedJSON[i].userId) {
        tempId = parsedJSON[i].userId;
        comp = 1;
      }
      if (parsedJSON[i].completed === true) {
        array[tempId] = comp++;
      }
    }
    console.log(array);
  }
});
