// app.js
const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const PORT = 3000 ;

//midware
app.use(bodyParser.urlencoded({ extended: true }) );
app.use(bodyParser.json());

let tasks = [] ;

//routes
app.get('/tasks', (req, res) => {
  res.json(tasks);
});


app.post('/tasks', (req, res) => {
  const task = req.body;
  tasks.push(task);
  res.status(201).json(task);
}
);
