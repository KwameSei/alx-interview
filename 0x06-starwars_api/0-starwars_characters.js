#!/usr/bin/node
const request = require('request');

baseURL = "https://swapi-api.alx-tools.com/api/films/";  // Base url
const filmID = process.argv[2];   // Film ID from command line
const url = `${baseURL}${filmID}`;  // Full url

(async () => {  // Request to API
  try { 
    const res = await new Promise((resolve, reject) => {
      request(url, (err, res) => {  // Request to API
        if (err) {
          reject(err);  // If error, reject
        } else {
          resolve(res);  // If no error, resolve
        }
      });
    });

    const film = JSON.parse(res.body);  // Parse body to JSON object (film)
    const x_ters = film.characters;  // Get characters from film

    for (const character of x_ters) {  // For each character
      const res2 = await new Promise((resolve, reject) => {
        request(character, (err, res) => {
          if (err) {
            reject(err);
          } else {
            resolve(res);
          }
        });
      });

      const oneChar = JSON.parse(res2.body);  // Parse body to JSON object (character)
      console.log(oneChar.name)
    }
  } catch (err) {
    console.log(err);
  }
})();
