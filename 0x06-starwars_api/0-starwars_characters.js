#!/usr/bin/node
const request = require("request");
const url = "https://swapi-api.hbtn.io/api";

if (process.argv.length > 2) {
  request(`${url}/films/${process.argv[2]}`, (error, _, body) => {
    if (error) {
      console.error(error);
      return;
    }
    const charactersURL = JSON.parse(body).characters;
    const charactersName = charactersURL.map(
      (url) =>
        new Promise((resolve, reject) => {
          request(url, (promiseErr, __, charactersReqBody) => {
            if (promiseErr) {
              reject(promiseErr);
            }
            resolve(JSON.parse(charactersReqBody).name);
          });
        })
    );

    Promise.all(charactersName)
      .then((names) => console.log(names.join("\n")))
      .catch((allErr) => console.log(allErr));
  });
}
