import React from 'react';
import styles from '../../styles/Home.module.css';
import logo from '../../assests/logo/logo.svg';
import file from '../../assests/logo/file.png';
import { useNavigate,Link } from 'react-router-dom';
import { useState, useEffect } from 'react';
import Navlanding from './Navlanding';

const NavCompo = () => {
  
  const navigate = useNavigate();

  

    


  return (
    <div className={styles.header_background} >
      <header className={styles.nav} >
        <div className={styles.logo}>
          <img src={file} alt="Logo" className={styles.navbar_logo} />
        </div>
        <Navlanding/>
      </header>
    </div>
    
  )
}

export default NavCompo