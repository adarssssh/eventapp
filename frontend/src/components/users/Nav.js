import React from 'react';
import styles from '../../styles/Home.module.css';
import logo from '../../assests/logo/logo.svg';
import file from '../../assests/logo/file.png';

const NavCompo = () => {



  return (
    <div className={styles._1VEUe}>
        <header className={styles.nav}>
                <div>
                  <nav>
                    <div className={styles.logo}>
                    <img src={file} alt="Icon description" className={styles.navbar_logo}></img>
                    </div>
                  </nav>
                </div>
              </header>
    </div>
  )
}

export default NavCompo