import React from 'react'
import styles from '../../../styles/Footer.css';

function Footer() {
  return (
    <div className='footer'>
        <div className="sb-footer-section-padding">
            <div className="sb-footer-links">
                <div className="sb-footer-links-div">
                    <h4>For Business</h4>
                    <a href="/employer">
                        <p>Employer</p>
                    </a>
                    <a href="/healthplan">
                        <p>Plan</p>
                    </a>
                    <a href="/individual">
                        <p>Individual</p>
                    </a>
                </div>
                <div className="sb-footer-links-div">
                    <h4>Resources</h4>
                    <a href="/employer">
                        <p>Resources Center</p>
                    </a>
                    <a href="/healthplan">
                        <p>Testimonials</p>
                    </a>
                    <a href="/individual">
                        <p>Vendors</p>
                    </a>
                </div>
                <div className="sb-footer-links-div">
                    <h4>Partners</h4>
                    <a href="/employer">
                        <p>Yatraa</p>
                    </a>
                </div>
                <div className="sb-footer-links-div">
                    <h4>Company</h4>
                    <a href="/about">
                        <p>About</p>
                    </a>
                    <a href="/press">
                        <p>Press</p>
                    </a>
                    <a href="/career">
                        <p>career</p>
                    </a>
                    <a href="/contact">
                        <p>Contact</p>
                    </a>
                </div>
                <div className="sb-footer-links-div">
                    <h4>Coming soon on</h4>
                    <div className="socialmedia">
                        <p>fb</p>
                        
                    </div>
                </div>
            </div>
            <hr></hr>

                <div className="sb-footer-below">
                    <div className="sb-footer-copyright">
                        <p>@{new Date().getFullYear()} HappenDo All right reserved</p>
                    </div>
                    <div className="sb-footer-below-links">
                        <a href="/term">
                            <div>
                                <p>Term & Conditions</p>
                            </div>
                        </a>
                        <a href="/privacy">
                            <div>
                                <p>Privacy</p>
                            </div>
                        </a>
                        <a href="/security">
                            <div>
                                <p>Security</p>
                            </div>
                        </a>
                        <a href="/cookie">
                            <div>
                                <p>Cookie Declaration</p>
                            </div>
                        </a>
                    </div>
                </div>
        </div>
    </div>
  )
  
}

export default Footer