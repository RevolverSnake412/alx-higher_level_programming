#!/usr/bin/node
const filesystem = require('fs');
filesystem.writeFile(process.argv[2], process.argv[3], function (error) {
  if (error) {
    console.log(error);
  }
});
