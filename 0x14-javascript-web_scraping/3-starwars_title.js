#!/usr/bin/node

// Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.
//
const axios = require('axios').default;
const ID = process.argv[2];
const endPoint = `https://swapi-api.hbtn.io/api/films/${ID}`;

axios
  .get(endPoint)
  .then((res) => console.log(res.data.title))
  .catch((err) => console.log(err.message));
