import React from 'react'
import axios from 'axios';
import { useEffect, useState } from 'react';
import styles from '../../../styles/Login.module.css';

function Login() {
  const [loginIdentifier, setLoginIdentifier] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [message, setMessage] = useState('');

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
      Welcome to HappenDo
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
      </form>
      {message && <p>{message}</p>}
      {error && <p>{error}</p>}
      </div>

      </div>
    
  );
}

export default Login