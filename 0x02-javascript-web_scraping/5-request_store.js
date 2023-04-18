#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file.

const request = require('request');
const fs = require('fs');

if (process.argv.length < 3) {
  console.error('Usage: ./5-request_store.js <URL> <output_file_path>');
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  fs.writeFile(filePath, body, 'utf-8', (error) => {
    if (error) {
      console.error(error);
    }
  });
});
