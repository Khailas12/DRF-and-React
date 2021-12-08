import React, { useEffect } from 'react';
import axiosInstance from '../axios';
import { useNavigate } from 'react-router-dom';


const Logout = (() => {
    const navigate = useNavigate();

    useEffect(() => {
        axiosInstance.post('user/logout/blacklist/', {
            refresh_token: localStorage.getItem('refresh_token'),
        });

        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        axiosInstance.defaults.headers['Authorization'] = null;
        navigate('/login');
    });
    return (
        <div>Logout</div>
    );
});

export default Logout;