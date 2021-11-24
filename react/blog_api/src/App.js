import React, { useEffect, useState } from "react";
import './App.css';
import Posts from './components/Posts';
import PostLoadingComponent from './components/PostLoading';


const App = (() => {
    const PostLoading = PostLoadingComponent(Posts);    // runs if the loading is false.
    const [appState, setAppState] = useState({
        loading: false, // true when the data is collected and becomes false while running.
        posts: null,    // stores all the data returned.
    });

    useEffect(() => {
        setAppState({ loading: true });
        const apiUrl = `http://127.0.0.1:8000/api/a`;

        fetch(apiUrl)
            .then((data) => data.json())
            .then((posts) => {
                setAppState({ 
                    loading: false,
                    posts: posts
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