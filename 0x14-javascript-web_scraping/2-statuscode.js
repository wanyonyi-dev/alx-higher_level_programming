#!/usr/bin/node
/**
 * This script makes an HTTPS GET request to a specified URL and logs the response code.
 */
const https = require('https');
const args = process.argv.slice(2);

https
  .get(args[0], (res) => {
    console.log('code: ' + res.statusCode);
  })
  .on('error', (err) => {
    console.log('Error: ' + err.message);
  });
