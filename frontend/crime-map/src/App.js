import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import Home from './components/Home';
import Estatisticas from './components/Estatisticas';

const App = () => {
  return (
    <div>
      <Router>
        <Routes>
          <Route exact path="/" element={<Home />} />
          <Route exact path="/estatisticas" element={<Estatisticas />} />
          <Route exact path="/home" element={<Home />} />
        </Routes>
      </Router>
    </div>
  );
};

export default App;