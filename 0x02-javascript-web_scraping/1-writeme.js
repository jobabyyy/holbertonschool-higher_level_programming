#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
const fileContent = process.argv[3];

fs.writeFile(filePath, fileContent, 'utf8', (err) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log('The file has been saved!');
});
