
const {PythonShell} = require('python-shell')
//import {PythonShell} from 'python-shell';

let pyshell = new PythonShell('run.py');

/*
var options = {
  mode: 'text',
  encoding: 'utf8',
  pythonOptions: ['-u'],
  scriptPath: './',
  args: [2],
  pythonPath: 'C:/Users/Jack/AppData/Local/Programs/Python/Python37'
}
*/

let options = {
  mode: 'text',
  //pythonPath: 'C:/Users/Jack/AppData/Local/Programs/Python/Python37/',
  encoding: 'utf8',
  pythonOptions: ['-u'], // get print results in real-time
  scriptPath: './',
  args: [5]
};

/*
var test = new PythonShell('run.py', options);
test.on('message', function(message) {
  console.log(message);
});
*/


// sends a message to the Python script via stdin
pyshell.send(5);

pyshell.on('message', function (message) {
 // received a message sent from the Python script (a simple "print" statement)
 console.log(message);
});

/*
PythonShell.run('run.py', options, function (err, results) {
  // if (err) throw err;
  // results is an array consisting of messages collected during execution
  console.log('results: %j', results);
});
*/
