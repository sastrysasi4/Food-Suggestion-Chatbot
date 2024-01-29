import logo from './logo.svg';
import './App.css';
import Header from './components/Header';
import Welcomepage from "./components/Home";
import { BrowserRouter as Router, Route, Switch, Link, Routes } from 'react-router-dom';
import React from 'react';
import Menu from './components/Menu';
import ChatInterface from './components/Chatbot'


function App() {
  return (
    <Router>
    <div className="App">
      <Header />
      <Routes>
          <Route path="/" element={<Welcomepage/>} />
          <Route path="/Menu" element={<Menu/>} />
          <Route path="/Chatbot" element={<ChatInterface/>} />
        </Routes>
    </div>
    </Router>
  );
}

export default App;
