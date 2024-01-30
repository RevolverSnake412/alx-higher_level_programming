#!/usr/bin/node
const filesystem = require('fs');
filesystem.readFile(process.argv[2], 'utf8', function(content, error) {
    console.log(content || error);
});