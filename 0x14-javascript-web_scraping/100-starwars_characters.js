#!/usr/bin/node
// prints all characters of a star wars movie
const request = require('request');

const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

function getCharacterName (url) {
  request(url, function (err, response, body) {
    if (err) {
      console.log(err);
      return null;
    }

    const data = JSON.parse(body);
    console.log(data.name);
  });
}

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return null;
  }

  const data = JSON.parse(body);
  const names = data.characters;

  for (const name of names) {
    getCharacterName(name);
  }
});
