import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter, Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
// import Footer from './components/Footer';


const routing = (
    <BrowserRouter>
        <React.StrictMode>
            <Header />
            <Routes>
                <Route path='/' element={<App />} />
            </Routes>
            {/* <Footer /> */}
        </React.StrictMode>
    </BrowserRouter>
);

ReactDOM.render(routing, document.getElementById('root'));
reportWebVitals();
