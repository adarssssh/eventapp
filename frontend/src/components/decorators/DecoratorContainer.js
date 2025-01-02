import React from 'react'
import styles from '../venue/venue.css'

const DecoratorContainer= (data) => {
    let img = data.data.profile_pic_url
    const image = img.replace("%%","250")
  return (
    <>
        <div className="Venuecards styles_containerV2__1_U51">
            <div className='vc-img'>
            <img src = {image}/>
            </div>
            
            <div className='vc-venue-details '>
                <div className='vc-venue-name'>{data?.data?.name}</div>
                <div>{data?.data?.city}</div>
                <div>{data?.data?.information}</div>
                <div>
                   Booking price: Rs.{data.data.vendor_price}
                </div>
                <button>Book</button>
            </div>
            
            
            
        </div>
        </>
  )
}

export default DecoratorContainer