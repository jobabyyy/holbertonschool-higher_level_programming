#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const movieData = JSON.parse(body);
  const count = movieData.results.filter(movie =>
    movie.characters.includes('https://swapi-api.hbtn.io/api/people/18/')
  ).length;

  console.log(count);
});
