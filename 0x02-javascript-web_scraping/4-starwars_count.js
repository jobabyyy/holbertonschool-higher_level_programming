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

  for (let i = 0; i < movieData.results.length; i++) {
    const characterUrls = movieData.results[i].characters;
    if (characterUrls.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      count++;
    }
  }

  console.log(count);
});
