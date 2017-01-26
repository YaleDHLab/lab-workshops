import './main.css';

import React from 'react';
import ReactDOM from 'react-dom';
import { Router, Route, browserHistory, IndexRoute } from 'react-router';

import AppWrapper from './components/AppWrapper';
import Home from './components/Home';

ReactDOM.render(
  <Router history={browserHistory}>
    <Route component={AppWrapper}>
      <Route path="/" component={Home} />
    </Route>
  </Router>,
  document.getElementById('app')
);