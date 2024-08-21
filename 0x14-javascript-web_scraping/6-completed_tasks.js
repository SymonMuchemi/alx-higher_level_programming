#!/usr/bin/node
// compute the number of tasks completed by user id
const request = require('request');

const url = process.argv[2];

request(url, function (error, resp, body) {
  if (error) {
    console.log(error);
    return;
  }

  if (resp.statusCode !== 200) {
    console.log('Error occured');
    return;
  }

  const tasks = JSON.parse(body);
  const completedTasksByUser = {};

  tasks.forEach(task => {
    if (task.completed) {
      if (!completedTasksByUser[task.userId]) {
        completedTasksByUser[task.userId] = 0;
      }
      completedTasksByUser[task.userId]++;
    }
  });

  console.log(completedTasksByUser);
});
