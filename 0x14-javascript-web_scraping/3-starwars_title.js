#!/usr/bin/node
/**
 * This script prints the title of a Star Wars movie where the episode number matches a given integer.
 * The first argument is the movie ID.
 * It uses the Star Wars API with the endpoint https://swapi-api.alx-tools.com/api/films/:id.
 * It uses the module request.
 */

const request = require('request');
const args = process.argv.slice(2);
const movieId = args[0];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.log('code:', response.statusCode);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
