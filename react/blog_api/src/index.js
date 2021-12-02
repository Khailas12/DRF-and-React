import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Header from './components/header';
import Footer from './components/footer';


const routing = (
    <BrowserRouter>
        <React.StrictMode>  // strictmode highlights potential problems in an app
            <Header />
            <Routes>
                <Route path='/' element={<App />} />
            </Routes>
            <Footer />
        </React.StrictMode>
    </BrowserRouter>
);

ReactDOM.render(routing, document.getElementById('root'));
reportWebVitals();