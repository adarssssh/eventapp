import React, { useState } from 'react'
import axios from 'axios'
import styles from '../../../styles/Register.module.css'
import file from '../../../assests/logo/file.png'

function Register() {

    
    const [phone, setPhone] = useState('')
    const [password, setPassword] = useState('')
    const [confirm_password, setConfirmPassword] = useState('')
    const [usertype, setUsertype] = useState('general')
    


    const handlePhoneChange = (event) => setPhone(event.target.value)
    const handlePasswordChange = (event) => setPassword(event.target.value)
    const handleConfirmPasswordChange = (event) => setConfirmPassword(event.target.value)
    const handleUserTypeChange = (event) => setUsertype(event.target.value)



    const handleSubmit = async(event) => {
        event.preventDefault();
    
        try{
            const response = await axios.post('users/auth/register_general_user/',{
                phone: phone,
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

    
<div className={styles.container}>
    <div class = {styles.logindiv} >
          <img src={file} alt="Logo" className={styles.navbar_logo} />
          </div>
    <div className={styles.register}>
        <h2>Register</h2>
        <form onSubmit={handleSubmit}>
            <div>
                <label>Phone no.</label>
                <input
                    type="text"
                    value={phone}
                    onChange={handlePhoneChange}
                    required
                />
            </div>
            <div>
                <label>Password</label>
                <input
                    type="password"
                    value={password}
                    onChange={handlePasswordChange}
                    required
                />
            </div>
            <div>
                <label>Confirm Password</label>
                <input
                    type="password"
                    value={confirm_password}
                    onChange={handleConfirmPasswordChange}
                    required
                />
            </div>
            <div>
                <label>User Type</label>
                <select
                    value={usertype}
                    onChange={handleUserTypeChange}
                    required
                >
                    <option value="">Select user type</option>
                    <option value="general">User</option>
                    <option value="provider">Admin</option>
                </select>
            </div>
            <button type="submit">Register</button>
            <div className={styles.message}>
                {/* Add your success/error messages here */}
            </div>
        </form>
    </div>
</div>
  )
}

export default Register