import React, { useEffect, useState } from "react";
import './App.css';
import Posts from './components/posts';
import PostLoadingComponent from './components/postLoading';
import axios from "axios";


const App = (() => {
    const PostLoading = PostLoadingComponent(Posts);    // runs if the loading is false.
    const [appState, setAppState] = useState({
        loading: false, // true when the data is collected and becomes false while running.
        posts: null,    // stores all the data returned.
    });

    useEffect(() => {
        setAppState({ loading: true });
        // http://localhost:8000/api/   can also be used
        const apiUrl = `http://localhost:8000/api/`;

        // fetch(apiUrl)
        //     .then((data) => data.json())
        //     .then((posts) => {
        //         setAppState({ 
        //             loading: false,
        //             posts: posts
        //         });
        //     });

        // same functionality as fetch but used axios instead
        axios.get(apiUrl).then((posts) => {
            const allPosts = posts.data;
            setAppState({
                loading: false,
                posts: allPosts
            });
        });

    }, [setAppState]);

    return (
        <div className='App'>
            <h1>Latest Posts</h1>
            <PostLoading isLoading={appState.loading} posts={appState.posts} />
        </div>
    );
});


export default App;