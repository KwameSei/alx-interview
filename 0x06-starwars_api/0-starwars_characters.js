#!/usr/bin/node
const request = require('request');

baseURL = "https://swapi-api.alx-tools.com/api/films/";  // Base url
const filmID = process.argv[2];   // Film ID from command line
const url = `${baseURL}${filmID}`;  // Full url

request(url, (error, res, body) => {  // Request to API
  if (error) {  // If error, print error
    console.log(error);
  } else {  // If no error, print characters
    const film = JSON.parse(body);  // Parse body to JSON object (film)
    const x_ters_url = film.characters;  // Get characters from film

    for (const character of x_ters_url) {  // For each character
      request(character, (error, res, body) => {   // Request to API
        if (error) {  
          console.log(error);
        } else {   // If no error, print character name
          const character = JSON.parse(body); 
          console.log(character.name);
        }
      });
    }
  }
});
