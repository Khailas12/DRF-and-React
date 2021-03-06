import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Header from './components/header';
import Footer from './components/footer';
import Register from './components/register';
import Login from './components/login';
import Logout from './components/logout';
import Single from './components/single';
import Search from './components/search';


/* strictmode highlights potential problems in an app */
const routing = (
    <BrowserRouter>
        <React.StrictMode>  
            <Header />
            <Routes>

                <Route path='/' element={<App />} />
                <Route path='/register' element={<Register />} />
                <Route path='/login' element={<Login />} />
                <Route path='/logout' element={<Logout />} />
                <Route path='/post/:slug' element={<Single />} />
                <Route path='/search' element={<Search />} />
                
            </Routes>
            <Footer />
        </React.StrictMode>
    </BrowserRouter>
);

ReactDOM.render(routing, document.getElementById('root'));
reportWebVitals();