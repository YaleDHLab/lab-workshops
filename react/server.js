// server.js
var express = require('express')
var path = require('path')
var compression = require('compression')
var session = require('express-session')
var morgan = require('morgan')
var cookieParser = require('cookie-parser')
var bodyParser = require('body-parser')
var methodOverride = require('method-override')

// configure database
var mongoose = require('mongoose')

/***
*
* Connect to the Mongoose db
*
***/

mongoose.connect('mongodb://localhost/dissertation');
mongoose.connection.on("error", function(err) {
  console.log(err);
});

/***
*
* Configure Express production server
*
***/

// initialize the server
var app = express()

// send compressed assets
app.use(compression())

// provide a session secret
app.use(session({ secret: 'hello_cello' }));

// serve files from the build directory
app.use(express.static(path.join(__dirname, 'build')))

// enable the cookie parser
app.use(cookieParser())

// enable the body parser
app.use(bodyParser())

// enable method overrides
app.use(methodOverride());

// enable logging
morgan('combined', {
  skip: function (req, res) { return res.statusCode < 400 }
})

/***
*
* View Routes
*
***/

// send requests to index.html so browserHistory in React Router works
app.get('*', function (req, res) {
  res.sendFile(path.join(__dirname, 'build', 'index.html'))
})

// ask server to listen on desired port
var PORT = process.env.PORT || 7000
app.listen(PORT, function() {
  console.log('Production Express server running at localhost:' + PORT)
})