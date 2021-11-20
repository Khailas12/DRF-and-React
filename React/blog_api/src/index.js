import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Header from './components/Header';
import Footer from './components/Footer';


const routing = (
    <Router>
        <React.StrictMode>
            <Header />
            <Routes>
                <Route exact path='/' component={App} />
            </Routes>
            <Footer />
        </React.StrictMode>
    </Router>
);

ReactDOM.render(routing, document.getElementById('root'));
reportWebVitals();