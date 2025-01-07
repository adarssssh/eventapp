// src/components/VendorDetails.js
import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import Homepage from '../landing/Homepage';

const VendorDetails = () => {

    const { vendorId } = useParams(); // Get the vendorId from the URL params
    const [vendorData, setVendorData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [index, setIndex] = useState(0)

    const vendor_id_URL = `http://127.0.0.1:8000/venue/vendor/${vendorId}`

    useEffect(() => {
        const fetchVendorData = async () => {
        try {
            const response = await axios.get(vendor_id_URL);
            
            setVendorData(response.data);
        } catch (err) {
            setError('Error fetching vendor details.');
        } finally {
            setLoading(false);
        }
        };

        fetchVendorData();
    }, [vendorId]);

    if (loading) return ;
    if (error) return <p>{error}</p>;

    console.log(vendorData)
    
    let img = vendorData.profile_pic_url
    const image = img.replace("%%","250")

    const venueImages = vendorData.venue_images;

    const handleNext = () => {
        setIndex((prevIndex) =>
          prevIndex === venueImages.length - 1 ? 0 : prevIndex + 1
        );
      };
    
      const handlePrevious = () => {
        setIndex((prevIndex) =>
          prevIndex === 0 ? venueImages.length - 1 : prevIndex - 1
        );
      };

    return (
        <div>
        <Homepage/>
        <h2>Vendor Details: {vendorData.name}</h2>
        <div>
            <div style={{ position: 'relative', width: '100%', maxWidth: '600px', margin: 'auto' }}>
                <img
                src={venueImages[index].image_url.replace("%%",950)}
                alt="Vendor"
                style={{ width: '100%', borderRadius: '10px' }}
                />
            </div>
            <button
          onClick={handlePrevious}
          style={{
            position: 'absolute',
            top: '50%',
            left: '10px',
            transform: 'translateY(-50%)',
            backgroundColor: 'rgba(0, 0, 0, 0.5)',
            color: '#fff',
            border: 'none',
            borderRadius: '50%',
            width: '40px',
            height: '40px',
            cursor: 'pointer',
          }}
        >
          ‹
        </button>
        <button
          onClick={handleNext}
          style={{
            position: 'absolute',
            top: '50%',
            right: '10px',
            transform: 'translateY(-50%)',
            backgroundColor: 'rgba(0, 0, 0, 0.5)',
            color: '#fff',
            border: 'none',
            borderRadius: '50%',
            width: '40px',
            height: '40px',
            cursor: 'pointer',
          }}
        >
          ›
        </button>
        </div>
        <div className="Venuecards styles_containerV2__1_U51">
                
                
                <div className='vc-venue-details '>
                    <div className='vc-venue-name'>{vendorData.name}</div>
                    <div>{vendorData.city}</div>
                    <div>Locality: {vendorData.locality}</div>
                    <div>{vendorData.categories[0].category_name}, {vendorData.categories[1]?.category_name}</div>
                    <div>
                    Booking price: {vendorData.vendor_price}
                    </div>
                    <div>
                    Information: {vendorData.information}
                    </div>
                    <div>
                        Ratings: {vendorData.vendor_rating}
                    </div>
                    <button>Book</button>
                </div>
                
                
                
            </div>
        </div>
    );
    };

    export default VendorDetails;
