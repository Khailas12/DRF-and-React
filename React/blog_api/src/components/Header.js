import React from "react";
import { AppBar } from "@material-ui/core";
import { Toolbar } from "@material-ui/core";
import { Typography } from "@material-ui/core";
import { CssBaseline } from "@material-ui/core";
import { makeStyles } from "@material-ui/core";


const useStyles = makeStyles((theme) => ({
    appBar: {
        borderBottom: `1px solid ${theme.palette.divider}`,
    },
}));

const Header = (() => {
    const classes = useStyles();
    return (
        <React.Fragment>
            <CssBaseline />
            <AppBar 
                position='static'
                color='white'
                elevation={0}
                className={classes.appBar}
            >
                <Toolbar>
                    <Typography variant='h6' color='inherit' nowrap>
                        BlogmeUp
                    </Typography>
                </Toolbar>
            </AppBar>
        </React.Fragment>
    );
});

export default Header;