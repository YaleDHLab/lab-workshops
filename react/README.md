# React Boilerplate

This repository aims to provide a quick way to start React.js applications. To get started, you'll need Node.js installed on your machine.

## Quickstart

To start a new React.js app, one can run the following commands:

```
# download the code from this repository
git clone https://github.com/duhaime/react-boilerplate

# use the Node package manager (npm) to install the dependencies
npm install

# start the webpack development server
npm start
```

If you run these commands then navigate to `localhost:8081` in a browser, you should see the simple boilerplate within this application.

## Styles

To gain some intuition about the way React.js apps are organized, open the `/app` directory. There you'll see a file named `main.css` that you can use to set the styles for the application. If you have the webpack dev server running, open `main.css` in a text editor and write:

```
body {
  background: cornsilk;
}
```

If you save the file and return to `localhost:8081` in a browser, you should see the background color of the webpage update. Other CSS rules you write in `main.css` will update the application in a similar way.

## Interactivity

React.js is meant for building highly interactive applications. To get a taste of how interaction works in React, let's create a button in `/app/main.css`:

```
.button {
  padding: 15px;
  text-align: center;
  min-width: 100px;
  background-color: lightsteelblue;
  display: inline-block;
  border-radius: 5px;
  cursor: pointer;
  text-transform: uppercase;
  font-weight: 600;
}
```

Once that's done, replace the content of `app/components/Home.jsx` with the following:

```
var React = require('react')

var Home = React.createClass({

  getInitialState() {
    return {
      totalCount: 0
    }
  },

  incrementCount() {
    var count = this.state.totalCount;
    this.setState({totalCount: count+1});
  },

  render: function() {
    return (
      <div className="home">
        <div>The total count is: {this.state.totalCount}</div>
        <div className="button" onClick={this.incrementCount}>Increment Count</div>
      </div>
    )
  }
});

module.exports = Home;
```

If you return to `localhost:8081`, you should see your button and a counter. If you click the button you should see the count increases. That's all it takes!

## Getting Started with State

Let's step through each line of the new `App.jsx` file:

```
// Import the React library into App.jsx
var React = require('react')

// Use a method named createClass within the React library to create a
// class named Home that we'll use in our application
var Home = React.createClass({

  // Identify the initial "state" of the React application. An application's
  // state is where you keep track of the status of the application. As users
  // interact with an app (e.g. click buttons, move sliders, etc.), you will
  // update values within a component's state
  getInitialState() {
    return {
      totalCount: 0
    }
  },

  // Define a function that will update the `totalCount` value
  // within this component's state
  incrementCount() {

    // Determine what the current totalCount is by examining the current state
    // of the `totalCount` variable
    var count = this.state.totalCount;

    // Update the state of this component by setting the `totalCount` variable
    // to the value of `count` plus one
    this.setState({totalCount: count+1});
  },

  // Define the html elements that are part of this component
  render: function() {
    return (

      // Create a container div with the "home" class
      <div className="home">

        // Display the current state of the totalCount variable
        <div>The total count is: {this.state.totalCount}</div>

        // Create a div with the class "button", and make it so that
        // when users click this button, we call the `incrementCount` function
        // defined in this component
        <div className="button" onClick={this.incrementCount}>Increment Count</div>
      </div>
    )
  }
});

// Export this component
module.exports = Home;
```

There are a few things to note about this component. `getInitialState` is an example of a special function that's defined by the React library. This special function allows you to initialize variables that you define in state. Likewise, `this.setState({variableName: newValue})` is a special bit of code that lets you update the variables in state. You can use these functions to manage the internal state of a component.

## Getting Started with Props

The last major building block of React.js apps is Props. Props are nothing more than variables from one component's state that are passed to other components. As an example, suppose you wanted to separate the counter from the Home component. You could do so by creating a new file `/app/components/Counter.jsx` and defining the counter logic in that component:

```
// app/components/Counter.jsx

var React = require('react')

var Counter = React.createClass({

  render: function() {
    return (
      <div className="header">
        <div>The total count is: {this.props.totalCount}</div>
        <div className="button"
          onClick={this.props.incrementCount}>Increment Count</div>
      </div>
    )
  }
});

module.exports = Counter;
```

Once you've saved the above, you can mount the Counter component within Home.jsx, which should be updated so as to read:

```
// app/components/Counter.jsx

var React = require('react')
var Counter = require('./Counter')

var Home = React.createClass({

  getInitialState() {
    return {
      totalCount: 0
    }
  },

  incrementCount() {
    var count = this.state.totalCount;
    this.setState({totalCount: count+1});
  },

  render: function() {
    return (
      <div className="home">
        <Counter totalCount={this.state.totalCount}
          incrementCount={this.incrementCount} />
      </div>
    )
  }
});

module.exports = Home;
```

The Home and Counter components work together to keep track of the `totalCount` variable. That variable's value is initially established in the `getInitialState()` of Home.jsx, and is passed through props to the Counter component. In other words, props are the vehicle through which application state is passed from the Home component to the Counter component.

Likewise, the function `incrementCount` is defined in Home and passed to Counter. By passing this function through props, one can call that function from Counter whenever website visitors click the Increment Count button. That is to say, just like application state can be passed through props, functions and callbacks can also be passed through props.

## Going Further

The brief guide above is meant only to give you a very quick introduction to React.js. To go further, I recommend the following resources:

<b>[React in 15ish Minutes](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi?hl=en)</b>: A great video introduction to React.js

<b>[React Developer Tools](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi?hl=en)</b>: A plugin for Chrome that allows you to inspect the props and state of each component, which helps tremendously as you're building and troubleshooting applications.

<b>[SurviveJS: Webpack and React](https://www.amazon.com/SurviveJS-Webpack-React-apprentice-master/dp/152391050X/ref=sr_1_1?ie=UTF8&qid=1485442146&sr=8-1&keywords=survivejs)</b>: A helpful beginner's guide to React and its ecosystem (Babel, Webpack, ES6, etc.)