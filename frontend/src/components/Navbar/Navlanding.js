import React from 'react'
import { Link } from 'react-router-dom'
import styles from '../../styles/Home.module.css'

function Navlanding() {
  return (
    <>
    <nav className={styles.navbar_links}>
            <Link to = "/" className={styles.navbar_link}>Home</Link>
            <Link to = "/about" className={styles.navbar_link}>About</Link>
            <Link to = "/venue" className={styles.navbar_link}>Services</Link>
            <Link to = "/contact" className={styles.navbar_link}>Contact</Link>
          </nav>
        <div>
          <Link to ="/login" className={styles.navbar_cta}>Sign Up</Link>
        </div>
    </>
  )
}

export default Navlanding