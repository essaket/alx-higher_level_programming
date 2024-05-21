#!/usr/bin/node

const request = require('request');
if (!(process.argv[2])) {
  console.error('Please provide API URL: https://jsonplaceholder.typicode.com/todos');
  process.exit(1);
}

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  const tasks = JSON.parse(body);
  const completedTasks = {};
  for (const task of tasks) {
    if (task.completed) {
      if (completedTasks[task.userId]) {
        completedTasks[task.userId]++;
      } else {
        completedTasks[task.userId] = 1;
      }
    }
  }
  console.log(completedTasks);
});
