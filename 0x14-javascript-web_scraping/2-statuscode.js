#!/usr/bin/node
// gets the status code of a get request
const request = require('request');

const url = process.argv[2];

request(url, (error, response) => {
  if (error) {
    console.log(error);
  } else {
    console.log('Code: ' + response.statusCode);
  }
});
