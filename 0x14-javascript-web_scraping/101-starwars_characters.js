#!/usr/bin/node
// prints all names of a star wars movie
const request = require('request');

const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

function getCharacterName (names, idx) {
  request(names[idx], function (err, response, body) {
    if (err) {
      console.log(err);
      return null;
    }

    const data = JSON.parse(body).name;
    console.log(data);

    if (idx + 1 < names.length) {
      getCharacterName(names, idx + 1);
    }
  });
}

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return null;
  }

  const data = JSON.parse(body);
  const names = data.characters;

  getCharacterName(names, 0);
});
