import React from 'react';
import { useNavigate } from "react-router-dom";

import styles from '../../styles/Home.module.css';
import logo from '../../assests/logo/logo.svg';
import file from '../../assests/logo/file.png'


function Homepage() {
  const navigate = useNavigate()

  const loginPage=()=>{
    navigate("/login");
  }
  return (
    <body className={styles.homepage}>
      <header className={styles.header}>
        
          <nav className={styles.navbar}>
            <div className={styles.logo}>
            <img src={file} alt="Icon description" className={styles.navbar_logo}></img>
            </div>
            <div className={styles.links}>
            <ul className={styles.navlinks}>
                <li>
                  <a href="/products">Products</a>
                </li>
                <li>
                  <a href="/about">About Us</a>
                </li>
                <li>
                  <a href="/contact">Contact</a>
                </li>
              </ul>
            </div>
            <div className={styles.button}>
              <button
                variant="text"
                size="sm"
                className={styles.button5}
                onClick={() => loginPage()}
              >
                <span>Log In</span>
              </button>
              <button
                variant="gradient"
                size="sm"
                className={styles.button5}
                
              >
                <span>Sign Up</span>
              </button>
            </div>
          </nav>
        
      </header>
        <div className={styles.hero}>
          Hello
        </div>
      <footer className={styles.footer}>
        <div>
          Footer
        </div>
      </footer>
    </body>
    
  )
}

export default Homepage