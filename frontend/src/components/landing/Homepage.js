import React from 'react';
import {useNavigate} from 'react-router-dom' ;

import styles from '../../styles/Home.module.css';
import logo from '../../assests/logo/logo.svg';
import file from '../../assests/logo/file.png'

import NavCompo from '../users/Nav.js';


function Homepage() {

  const navigate = useNavigate()

  const handleClickVenue = () => {
    navigate("/venue")
  }
  const handleClickDecorator = () => {
    navigate("/decorators")
  }
  
  return (
    <div className={styles.homepage}>
        <NavCompo/>
        <div className={styles.hero}>
          
          <div className={styles.serviceDiv} onClick={handleClickVenue}>Venues</div>
          <div className={styles.serviceDiv} onClick={handleClickDecorator}>Decorators</div>
          <div className={styles.serviceDiv}>DJ/Sound</div>
          <div className={styles.serviceDiv}>Food Serivces</div>
          <div className={styles.serviceDiv} onMouseOver={() =>{
            console.log("Mouse")
          }}>Photography & Video</div>
          <div className={styles.serviceDiv} >Artists</div>
          <div className={styles.serviceDiv} >Security</div>
          <div className={styles.serviceDiv} >Travel Serivces</div>
        </div>
      
    </div>
    
  )
}

export default Homepage