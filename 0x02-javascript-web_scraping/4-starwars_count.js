#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const movieData = JSON.parse(body);
  let count = 0;

  movieData.results.forEach(movie => {
    const characterUrls = movie.characters;
    if (characterUrls.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      count++;
    }
  });

  console.log(`Wedge Antilles appears in ${count} Star Wars movies.`);
});
