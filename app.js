// brain of project
const express = require('express'); // this imports dependencies to app.js
const expressLayouts = require('express-ejs-layouts');
const fileUpload = require('express-fileupload');
const session = require('express-session');
const cookieParser = require('cookie-parser');
const flash = require('connect-flash');

const app = express();
const port = process.env.PORT || 3000; //we made the port for all as 3000 as we are using localhost

require('dotenv').config();

app.use(express.urlencoded( { extended: true } ));
app.use(express.static('public'));// we dont want to list the full path to import images, scripts or whatever
app.use(expressLayouts);

app.use(cookieParser('CookingBlogSecure'));
app.use(session({
  secret: 'CookingBlogSecretSession',
  saveUninitialized: true,
  resave: true
}));
app.use(flash());
app.use(fileUpload());

app.set('layout', './layouts/main');// this is where we are going to store layouts and main layout
app.set('view engine', 'ejs'); // explicitly telling the browser that we are using ejs for frontend 

const routes = require('./server/routes/recipeRoutes.js')
app.use('/', routes);

app.listen(port, ()=> console.log(`Listening to port ${port}`)); // this is to print the port and connect to port number 3000