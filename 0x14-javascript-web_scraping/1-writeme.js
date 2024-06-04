#!/usr/bin/node
/**
 * Writes the specified content to the file at the given file path.
 * @param {string} filePath - The path of the file to write to.
 * @param {string} content - The content to write to the file.
 */
const args = process.argv.slice(process.argv.length - 2);
const fs = require('fs');

const [filePath, content] = args;

fs.writeFile(filePath, content, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
