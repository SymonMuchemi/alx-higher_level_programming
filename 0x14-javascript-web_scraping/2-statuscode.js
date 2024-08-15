#!/usr/bin/bash
// gets the status code of a get request
const request = require('request');

const url = process.argv[1];

request(url, (error, response) => {
  if (error) {
    console.log(error);
  } else {
    console.log('Code: ' + response.statusCode);
  }
});
