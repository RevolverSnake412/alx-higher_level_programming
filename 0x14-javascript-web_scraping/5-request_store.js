#!/usr/bin/node
const request = require('request');
const filesystem = require('fs');

request(process.argv[2], function (error, request, body) {
  if (!error) {
    filesystem.writeFile(process.argv[3], body, function (error) {
      if (error) {
        console.log(error);
      }
    });
  }
});
