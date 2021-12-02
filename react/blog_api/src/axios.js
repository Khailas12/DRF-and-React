import axios from 'axios';


const baseURL = 'http://127.0.0.1:8000/api/';

const axiosInstance = axios.create({
    baseURL: baseURL,
    timeout: 5000,

    headers: {
        // to get the data outta the local storage. 
        Authorization: localStorage.getItem('access_token')
            ? 'JWT ' + localStorage.getItem('access_token') : null,
        'Content-Type': 'application/json',
        accept: 'application/json'
    },
});

