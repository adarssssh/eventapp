import React, { useState } from 'react'
import axios from 'axios'

function Register() {

    const [phonenumber, setphonenumber] = useState('')
    const [password, setPassword] = useState('')
    const [confirm_password, setConfirmPassword] = useState('')
    const [usertype, setUsertype] = useState('general')
    const [submit, setSubmit] = useState()


    const handlePhoneNumberChange = (event) => setphonenumber(event.target.value)
    const handlePasswordChange = (event) => setPassword(event.target.value)
    const handleConfirmPasswordChange = (event) => setConfirmPassword(event.target.value)
    const handleUserTypeChange = (event) => setUsertype(event.target.value)



    const handleSubmit = async(event) => {
        event.preventDefault();
    
        try{
            const response = await axios.post('users/auth/register_general_user/',{
                username: phonenumber,
                password: password,
                confirm_password: confirm_password,
                user_type: usertype,
            });

            console.log(response)
        }
        catch(error){
            // console.log(error)
        }
    }

  return (
    <div>Register
        <div>
            
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Phone no.</label>
                    <input
                    type = "text" 
                    value = {phonenumber}
                    onChange={handlePhoneNumberChange}
                    required/>
                </div>
                <div>
                    <label>Password.</label>
                    <input
                    type = "password" 
                    value = {password}
                    onChange={handlePasswordChange}
                    required/>
                </div>
                <div>
                    <label>Confirm Password.</label>
                    <input
                    type = "password"
                    value = {confirm_password}
                    onChange={handleConfirmPasswordChange}
                    required/>
                </div>
                <div>
                    <label>User Type.</label>
                    <input
                    type = "choice" 
                    value = {usertype}
                    onChange={handleUserTypeChange}
                    required/>
                </div>
                <button type="submit">Register</button>
                <div>
                    {}
                </div>
            </form>
        </div>
    </div>
  )
}

export default Register