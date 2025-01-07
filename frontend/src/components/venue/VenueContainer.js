import styles from '../venue/venue.css'

const VenueContainer = (data) => {

    console.log(data.data)

    let img = data.data.profile_pic_url
    const image = img.replace("%%","250")

    
    
    
    return(
        <>
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
        </>
    )
}

export default VenueContainer