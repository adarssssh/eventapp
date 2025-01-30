import React from 'react'
import NavGeneral from '../../Navbar/NavGeneral'
import Services from '../venue/Services'
import ShimmerUI from '../venue/ShimmerUI'

function Home() {
  return (
    <>
    
    <div className="maindivVenue">
        <div className="navGeneral">
        <NavGeneral/>
        </div>
        <Services/>

        <div className="Listcontainer">
            <div className="Venuecontainer" >
              
                <ShimmerUI />
                    
                    
             
                

            </div>
        </div>
        
        
        
        
    </div>
        
    
    
    </>
  )
}

export default Home