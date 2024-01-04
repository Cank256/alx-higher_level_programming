#!/usr/bin/node
/* Prints all characters of a Star Wars movie. */

const request = require('request');
const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const movie = JSON.parse(body);
    movie.characters.forEach(characterUrl => {
      request(characterUrl, function (err, res, charBody) {
        if (!err && res.statusCode === 200) {
          const character = JSON.parse(charBody);
          console.log(character.name);
        }
      });
    });
  }
});
