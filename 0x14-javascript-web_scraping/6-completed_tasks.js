#!/usr/bin/node
const request = require('request');
const array = {};
let tempId = 1;

request(process.argv[2], function (error, response, body) {
  if (!error) {
    const parsedJSON = JSON.parse(body);
    array[parsedJSON[0].userId] = 0;
    for (const i in parsedJSON) {
      if (tempId !== parsedJSON[i].userId) {
        tempId = parsedJSON[i].userId;
        array[parsedJSON[i].userId] = 0;
      }
      if (parsedJSON[i].completed === true) {
        array[parsedJSON[i].userId]++;
      }
    }
    console.log(array);
  }
});
