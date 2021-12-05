import react, { Component } from 'react';


export default class ValidationForm extends Component {
    render() {
        return (
            <Form>
                <div className='form-group'>
                    <label>Email</label>
                    <input type='email' className='form-control' />
                </div>

                <div className='forn-group'>
                    <label>Password</label>
                    <input type='text' className='form-control' />
                </div>

            </Form>
        );
    }
}

const regExp = RegExp(
    /^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[A-Za-z]+$/
)

const formValid = ({ isError, ...rest }) => {
    let isValid = false;

    Object.values(isError).forEach(val => {
        if (val.length > 0) {
            isValid = false;
        }   
        else {
            isValid = true
        }
    });

    Object.values(rest).forEach(val => {
        if (val === null) {
            isValid = false;
        }
        else {
            isValid = true;
        }
    });
    return isValid;
};