#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/people/18';

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const parsedJSON = JSON.parse(body);
  console.log(parsedJSON.films.length);
});
