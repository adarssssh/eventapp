import { useState } from 'react';
import styles from '../venue/venue.css';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

const VenueContainer = (data) => {
    
    const [vendorDetails, setVendorDetails] = useState(null);
    const navigate = useNavigate()
    const vendor_id_URL = `http://127.0.0.1:8000/venue/vendor/`

    

    let img = data.data.profile_pic_url
    const image = img.replace("%%","250")

    const handleVenue = async () => {
        const vendorId = data?.data?.vendor_id;
    
        if (vendorId) {
          try {
            
            
            // const response = await axios.get(vendor_id_URL+vendorId);
            
            navigate(`/vendor/${vendorId}`);
          } catch (err) {
            console.error("Error fetching vendor data", err);
          }
        } else {
          console.error("Vendor ID not found");
        }
      };
    
    
    return(
        <div className="Venuecontainer" onClick={handleVenue}>
        <div className="Venuecards styles_containerV2__1_U51">
            <div className='vc-img'>
            <img src = {image}/>
        </div>
            
            <div className='vc-venue-details '>
                <div className='vc-venue-name'>{data?.data?.name}</div>
                <div>{data?.data?.city}</div>
                <div>{data?.data?.categories[0].category_name}, {data?.data?.categories[1]?.category_name}</div>
                <div>
                   Booking price: {data.data?.vendor_price}
                </div>
                <button>Book</button>
            </div>
            
            
            
        </div>
        </div>
    )
}

export default VenueContainer