import React, { Component } from "react";


const PostLoading = ((Component) => {
    return function PostLoadingComponent({ isLoading, ...props }) {
        if (!isLoading) {   
            return <Component {...props} />;
        }
        retrun (
            <p style={{ fontSize: '25px' }}>
                Waiting for the data to load
            </p>
        );
    }
});

export default PostLoading;