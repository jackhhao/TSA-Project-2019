// Modules to control application life and create native browser window
const {app, BrowserWindow} = require('electron')
const {PythonShell} = require('python-shell')
const electron = require('electron')
//import {PythonShell} from 'python-shell';
let pyshell = new PythonShell('../stocks/run.py');


let options = {
  mode: 'text',
  // pythonPath: 'C:/Users/Jack/AppData/Local/Programs/Python/Python37/',
  encoding: 'utf8',
  pythonOptions: ['-u'], // get print results in real-time
  scriptPath: './',
  args : [10, 30, 40]
};

/*
var test = new PythonShell('run.py', options);
test.on('message', function(message) {
  console.log(message);
});
*/

// below: way to use pythonshell to get notifs successfully, doesn't return anything


PythonShell.run('run.py', options, function (err, results) {
  // if (err) throw err;
  // results is an array consisting of messages collected during execution
  console.log('results: %j', results);
});



pyshell.send(5);



// Keep a global reference of the window object, if you don't, the window will
// be closed automatically when the JavaScript object is garbage collected.
let mainWindow

function createWindow () {
  // Create the browser window.
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true
    }
  })

  // and load the index.html of the app.
  mainWindow.loadFile('index.html')

  // Open the DevTools.
  // mainWindow.webContents.openDevTools()

  // Emitted when the window is closed.
  mainWindow.on('closed', function () {
    // Dereference the window object, usually you would store windows
    // in an array if your app supports multi windows, this is the time
    // when you should delete the corresponding element.
    mainWindow = null
  })
}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.on('ready', createWindow)

// Quit when all windows are closed.
app.on('window-all-closed', function () {
  // On macOS it is common for applications and their menu bar
  // to stay active until the user quits explicitly with Cmd + Q
  if (process.platform !== 'darwin') app.quit()
})

app.on('activate', function () {
  // On macOS it's common to re-create a window in the app when the
  // dock icon is clicked and there are no other windows open.
  if (mainWindow === null) createWindow()
})

// In this file you can include the rest of your app's specific main process
// code. You can also put them in separate files and require them here.
