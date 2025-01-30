import React from 'react'
import axios from 'axios';
import { useState, } from 'react';
import { useNavigate } from 'react-router-dom';
import styles from '../../../styles/Login.module.css';
import file from '../../../assests/logo/file.png';

function Login() {
  const [loginIdentifier, setLoginIdentifier] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [message, setMessage] = useState('');

  const navigate = useNavigate();

  

  

  // Handle input changes
  const handleLoginIdentifierChange = (event) => setLoginIdentifier(event.target.value);
  const handlePasswordChange = (event) => setPassword(event.target.value);

  // Handle form submission
  const handleSubmit = async (event) => {
    event.preventDefault();

  

    // Clear previous messages
    setError('');
    setMessage('');

    try {
      const response = await axios.post('/users/auth/login/', {
        login_identifier: loginIdentifier,
        password: password,
      });
      
      // If successful, handle the response
      setMessage('Login successful');
      console.log(response.data);
    } catch (error) {
      // If there's an error (e.g. wrong credentials), show error message
      setError('Login failed. Please check your credentials.');
      console.error(error);
    }
  };
  return  (
    <div className={styles.container}>
    <div class = {styles.logindiv} >
      <img src={file} alt="Logo" className={styles.navbar_logo} fetchPriority="high" loading="eager" />
      </div>
      <div class = {styles.loginmain}>
        <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Username:</label>
          <input
            type="text"
            value={loginIdentifier}
            onChange={handleLoginIdentifierChange}
            required
          />
        </div>
        <div>
          <label>Password:</label>
          <input
            type="password"
            value={password}
            onChange={handlePasswordChange}
            required
          />
        </div>
        <button type="submit">Login</button>
        <button onClick={()=>{navigate("/register")}}>Register</button>
        <div className={styles.socials}>
          <p>Or login with</p>
          <div className={styles.socialButtons}>
            
            <button className={styles.socialButton}>
              <img src="https://img.icons8.com/color/48/000000/google-logo.png" alt="Google" />
              <span>Google</span>
            </button>
            </div>
          </div>
        
      </form>
      {message && <p>{message}</p>}
      {error && <p>{error}</p>}
      </div>
      </div>
    
  );
}

export default Login