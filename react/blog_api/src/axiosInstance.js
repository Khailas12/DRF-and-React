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

axiosInstance.interceptors.response.use(
    (response) => {
        return response;
    },

    async function (error) {
        const originalRequest = error.config;

        if (typeof error.response === 'undefined') {    // if server isn't connected 
            alert(
                'A server/netwoek error occured. ' +
                    'Looks like CORS might be the problem. '  +
                    'Sorry about this - we will get if fixed shortly'
            );
            return Promise.reject(error);
        }

        if (
            error.response.status === 401 && 
            originalRequest.url === baseURL + 'token/refresh/'
        ) {
            window.location.href = '/login/';
            return Promise.reject(error);
        }

        if (
            error.response.data.code === 'token_invalid' &&
            error.response.status === 401 &&
            error.response.statusText === 'Unauthorized'
        ) {
            const refreshToken = localStorage.getItem('refresh_token');

            if (refreshToken) {
                const tokenParts = JSON.parse(atob(refreshToken.split('.')[1]));

                const now = Math.ceil(Date.now() / 1000);
                console.log(tokenParts.exp);

                if (tokenParts.exp > now) {
                    return axiosInstance
                        .post('/token/refresh/', { refresh: refreshToken })
                        .then((response) => {
                        
                            // updating the localStorage
                            localStorage.setItem('access_token', response.data.access);
                            localStorage.setItem('access_token', response.data.refresh);

                            axiosInstance.defaults.headers['Authorization'] = 'JWT' + response.data.access;

                            originalRequest.headers['Authorization'] = 'JWT' + response.data.access;

                            return axiosInstance(originalRequest);
                        })

                        .catch((err) => {
                            console.log(err);
                        });
                }
                else {
                    console.log('Refresh token is expired', tokenParts.exp, now);
                    window.location.href = '/login/';
                }
            }
            else {
                console.log('Refresh token Unavailable');
                window.location.href = '/login/';
            }
        }
        return Promise.reject(error);
    }
);


export default axiosInstance;