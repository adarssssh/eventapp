import React from 'react'
import styles from '../../../styles/venue.css'
import {useNavigate} from 'react-router-dom' ;

function Services() {

    const navigate = useNavigate()
    
    const handleClickVenue = () => {
        navigate("/venue")
      }
      const handleClickDecorator = () => {
        navigate("/decorators")
      }
  return (
    <div className="serviceContainer">
          
          <div className="serviceDiv" onClick={handleClickVenue}>Venues</div>
          <div className="serviceDiv" onClick={handleClickDecorator}>Decorators</div>
          <div className="serviceDiv">DJ/Sound</div>
          <div className="serviceDiv">Food Serivces</div>
          <div className="serviceDiv" onMouseOver={() =>{
            console.log("Mouse")
          }}>Photography</div>
          <div className="serviceDiv" >Artists</div>
          <div className="serviceDiv" >Security</div>
          <div className="serviceDiv" >Travel Serivces</div>
        
    </div>
  )
}

export default Services