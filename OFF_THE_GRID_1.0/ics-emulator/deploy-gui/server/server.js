const http = require('http');
const express = require('express');
const RED = require('node-red');
const cors = require('cors');

// Create an Express app
const app = express();

const port = process.env.PORT || 8000;

// Add a simple route for static content served from 'public'
app.use('/', express.static('public'));

// Cors middleware
app.use(cors());
// Create a server
const server = http.createServer(app);

var fs = require('fs'),
    path = require('path'),    
    filePath = path.join('/home/nol/.nodered/projects/project2/flow.json');

fs.readFile(filePath, {encoding: 'utf-8'}, function(err,data){
    if (!err) {
        console.log('received data: ' + data);
        //response.writeHead(200, {'Content-Type': 'text/html'});
        //response.write(data);
        //response.end();
    } else {
        console.log(err);
    }
});

// Create the settings object - see default settings.js file for other options
const settings = {
  httpAdminRoot: '/red',
  httpNodeRoot: '/api',
  userDir: '/home/nol/.nodered/',
  editorTheme: {
    projects: {
      enabled: true
    }
  },
  adminAuth: {
    type: 'credentials',
    users: [
      {
        username: 'admin',
        password:
          '$2b$08$lT4hFY4HkQ4PCCiJDV5Jl.kK3Hjw1VmNUNUyFOlX4I.NkGsthdVMu',
        permissions: '*'
      }
    ]
  },
  functionGlobalContext: {} // enables global context,
};

// Initialise the runtime with a server and settings
RED.init(server, settings);

// Serve the editor UI from /red
app.use(settings.httpAdminRoot, RED.httpAdmin);

// Serve the http nodes UI from /api
app.use(settings.httpNodeRoot, RED.httpNode);

// Start the runtime
RED.start();

app.get('/runtime-settings', (req, res) => {
  RED.runtime.settings
    .getRuntimeSettings({ username: 'admin' })
    .then(settings => {
      res.send(settings);
    });
});

app.get('/user-keys', (req, res) => {
  RED.runtime.settings.getUserKeys({ username: 'admin' }).then(settings => {
    res.send(settings);
  });
});

app.get('/listprojects', (req, res) => {
  RED.runtime.projects
    .listProjects({ username: 'admin' })
    .then(projectsList => {
      res.send(projectsList);
    });
});

app.get('/projects-metadata', (req, res) => {
  RED.runtime.projects
    .getProject({ username: 'admin', id: 'd751713988987e9331980363e24189ce' })
    .then(projectsList => {
      res.send(projectsList);
    });
});

app.get('/flows', (req, res) => {
  RED.runtime.flows.getFlows({ username: 'admin' }).then(projectsList => {
    res.send(projectsList);
  });
});

app.get('/nodes-list', (req, res) => {
  RED.runtime.nodes.getNodeList({ username: 'admin' }).then(projectsList => {
    res.send(projectsList);
  });
});

app.get('/is-started', (req, res) => {
  RED.runtime.isStarted({ username: 'admin' }).then(projectsList => {
    res.send(projectsList);
  });
});

server.listen(port, () => {
  console.log(`server started @ ${port}`);
});
