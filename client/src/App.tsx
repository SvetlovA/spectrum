import React from 'react';
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import { HomePage } from './home/HomePage';
import { PlotPage } from './plot/PlotPage';

function App() {
  return (
    <Router>
      <Switch>
        <Route exact path='/' component={HomePage} />
        <Route path='/plot' component={PlotPage} />
      </Switch>
    </Router>
  );
}

export default App;
