import React from 'react';
import {useNavigate} from 'react-router-dom';
import styles from '../../../styles/Home.module.css';
import logo from '../../../assests/logo/logo.svg';
import file from '../../../assests/logo/file.png';
import image from '../../../assests/img/hero_image.png';
import NavCompo from '../../Navbar/Nav.js';
import Footer from './Footer.js';
import Navlanding from '../../Navbar/Navlanding.js';


function Homepage() {

  const navigate = useNavigate();

  const handleClick = () => {
    navigate("/venue")
  }

  return (
    <div className={styles.homepage}>
        <NavCompo/>
        <div className={styles.hero}>
          <div className={styles.hero_text}>
          
            <h1><span>Organize</span>any type of <span>Event</span> in any City.</h1>
            <p>We always make our customer happy by providing
            as many choices as possible </p>
            <button onClick={handleClick}>Get Started</button>
          </div>
          <img
            src={image}
            alt="Hero Image"
            className={styles.hero_img}
          />

        </div>

        <Footer/>
    </div>
    
  )
}

export default Homepage