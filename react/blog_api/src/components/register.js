import React, { useState } from 'react';
import axiosInstance from '../axios';
import { useNavigate } from 'react-router-dom';
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import Checkbox from '@material-ui/core/Checkbox';
import Link from '@material-ui/core/Link';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';
import IconButton from "@material-ui/core/IconButton";
import Visibility from "@material-ui/icons/Visibility";
import InputAdornment from "@material-ui/core/InputAdornment";
import VisibilityOff from "@material-ui/icons/VisibilityOff";
import { makeStyles } from '@material-ui/core/styles';
import { isEmail } from 'validator';
import { useForm, Controller } from 'react-hook-form';



const required = (value) => {
    if (!value) {
        return (
            <div className="alert alert-danger" role="alert">
                This field is required!
            </div>
        );
    }
};

const validEmail = (value) => {
    if (!isEmail(value)) {
        return (
            <div className='alert alert-danger' role='alert'>
                This is not a valid email
            </div>
        );
    }
};

const validPassword = (value) => {
    if (value.length < 6 || value.length > 60) {
        return (
            <div className='alert alert-danger' role='alert'>
                The Password must contain minimum 6 Characters
            </div>
        );
    }
};


const useStyles = makeStyles((theme) => ({
    paper: {
        marginTop: theme.spacing(8),
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
    },
    avatar: {
        margin: theme.spacing(1),
        backgroundColor: theme.palette.secondary.main,
    },
    form: {
        width: '100%', // Fix IE 11 issue.
        marginTop: theme.spacing(3),
    },
    submit: {
        margin: theme.spacing(3, 0, 2),
    },
}));

const SignUp = () => {
    const navigate = useNavigate();
    
    // Object.freeze() method freezes an object. A frozen object can no longer be changed; freezing an object prevents new properties from being added to it
    const initialFormData = Object.freeze({
        email: '',
        username: '',
        password: '',
    });

    const [formData, updateFormData] = useState(initialFormData);

    const handleChange = (e) => {
        updateFormData({
            ...formData,
            // Trimming any whitespace
            [e.target.name]: e.target.value.trim(),
        });
    };

    const [showPassword, setShowPassword] = useState(false);

    const handleClickShowPassword = () => {
        setShowPassword(!showPassword);
    };

    const handleMouseDownPassword = () => {
        setShowPassword(!showPassword);
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(formData);

        axiosInstance
            .post(`user/register/`, {
                email: formData.email,
                user_name: formData.username,
                password: formData.password,

            })
            .then((res) => {
                navigate('/login');
                console.log(res);
                console.log(res.data);
            });
    };
    

    const classes = useStyles();
    const { control } = useForm();


    return (
        <React.Fragment>

        <Container component="main" maxWidth="xs">
            <CssBaseline />
            <div className={classes.paper}>
                <Avatar className={classes.avatar}></Avatar>

                <Typography component="h1" variant="h5">
                    Sign up
                </Typography>

                <form className={classes.form} onSubmit={handleSubmit}>

                    <Grid container spacing={2}>
                        <Grid item xs={12}>
                            <Controller
                                name='Email'
                                control={control}
                                
                                render={({ 
                                    field: {value}, 
                                    fieldState: { error } 
                                }) => (
                                    <TextField
                                    variant="outlined"
                                    required
                                    fullWidth
                                    id="email"
                                    label="Email Address"
                                    name="email"
                                    autoComplete="email"
                                    onChange={handleChange}
                                    error={!!error}
                                    helperText={error ? error.message : null}
                                    />
                                    )}
                                    rules={validEmail}
                            />
                        </Grid>

                        <Grid item xs={12}>
                            <TextField
                                variant="outlined"
                                required
                                fullWidth
                                id="username"
                                label="Username"
                                name="username"
                                autoComplete="username"
                                onChange={handleChange}
                                />
                        </Grid>

                        <Grid item xs={12}>
                            <TextField
                                variant="outlined"
                                required
                                fullWidth
                                name="password"
                                type={showPassword ? "type" : "password"}
                                label='Password'
                                id="password"
                                autoComplete="current-password"
                                onChange={handleChange}
                                validations={[required, validPassword]}
                                
                                InputProps={{
                                    endAdornment: (
                                        <InputAdornment position='end'>
                                            <IconButton
                                                aria-label="toggle password visibility"
                                                onClick={handleClickShowPassword}
                                                onMouseDown={handleMouseDownPassword}
                                                >
                                                {showPassword ? <Visibility /> : <VisibilityOff />}
                                            </IconButton>
                                        </InputAdornment>
                                    )
                                }}
                            />
                        </Grid>

                        <Grid item xs={12}>
                            <FormControlLabel
                                control={<Checkbox value="allowExtraEmails" color="primary" />}
                                label="I want to receive inspiration, marketing promotions and updates via email."
                                />
                        </Grid>
                    </Grid>

                    <Button
                        type="submit"
                        fullWidth
                        variant="contained"
                        color="primary"
                        className={classes.submit}
                        onClick={handleSubmit}
                        >
                        Sign Up
                    </Button>

                    <Grid container justify="flex-end">
                        <Grid item>
                            <Link href="/login" variant="body2">
                                Already have an account? Sign in
                            </Link>
                        </Grid>
                    </Grid>

                </form>
            </div>
        </Container>
    </React.Fragment>
    );
};

export default SignUp;