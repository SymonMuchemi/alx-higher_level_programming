#!/usr/bin/node
// get the number of movies where a character is present
const { count } = require('console');
const request = require('request');

const url = process.argv[2];

request(`${url}`, function (error, resp, body) {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(body).results;

    console.log(results.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
