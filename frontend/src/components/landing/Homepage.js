import React from 'react';

import styles from '../../styles/Home.module.css';
import logo from '../../assests/logo/logo.svg';
import file from '../../assests/logo/file.png'


function Homepage() {
  return (
    <body className={styles.homepage}>
      <header className={styles.nav}>
        <div>
          <nav>
            <div className={styles.logo}>
            <img src={file} alt="Icon description" className={styles.navbar_logo}></img>
            </div>
          </nav>
        </div>
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