
import React ,{useState, useEffect, useRef} from "react"
import styles from '../venue/venue.css'

import VenueContainer from "./VenueContainer"
import { data } from "react-router-dom"
import Homepage from "../landing/Homepage"
import ShimmerUI from "./ShimmerUI"






const ListVenue = () => {

    const [venue, setVenue] = useState([])
    const [city,setCity] = useState("jaipur")
    const [search,setSearch] = useState("")
    const [page, setPage] = useState(1)
    const [loading, setLoading] = useState(true)


    const cache = useRef({}); // Ref to store cached data

    const VENUE_URL = `https://www.wedmegood.com/node/v1/vendor/list?category_slug=wedding-venues&city_slug=${city}&filter_option=&offset=0&device_type=1&page=${page}`

    async function Call() {
        const cacheKey = `${city}-page${page}`
        if (cache.current[cacheKey]) {
            setVenue(cache.current[cacheKey]); // Use cached data
            setLoading(false);
            return;
        }
        setLoading(true);
        const response = await fetch(VENUE_URL)
        const data = await response.json()
        setVenue(data.data)
        cache.current[cacheKey] = data.data;
        setLoading(false);
    }

    const handleSearch = () => {
        const value = search.trim().toLowerCase()
        if (value && city !== value) {
            setCity(value);
        }
    }
    const handleEnter =(event) =>{
        if (event.keyCode === 13){
            handleSearch()
        }
    }
    const handlePageChange = (increment) => {
        setPage((prevPage) => Math.max(1, prevPage + increment)); // Prevent page number below 1
    };

    useEffect(() =>{
        Call()
    },[city,page])

    
    console.log(venue)
    
    return (
        <div className="maindivVenue">
        <Homepage/>
        

        <div className="div-srch">
            <div className="div-service" ><h1>Venue List</h1></div>
            <input
            type="text"
            placeholder="Search City"
            value= {search}
            name="name"
            onKeyUp={handleEnter}
            onChange={(e) => setSearch(e.target.value)}
            />
            
            <button onClick={handleSearch} >Search</button>

        </div>
        

        <div className="Listcontainer">
            <div className="Venuecontainer">
                {loading ? (<ShimmerUI />):
                    
                    (
                        Array.isArray(venue) && venue.length > 0 ? (
                            venue.map((data, index) => (
                                <VenueContainer key={index} data={data} />
                            ))
                        ) : (
                            <p>No venues found!</p>
                        )
                    )
                }
             
                

            </div>
        </div>
        <div className="vid-pagination">
        
                <button onClick={() => handlePageChange(-1)} disabled={page === 1}>
                    Previous
                </button>
                <span>Page: {page}</span>
                <button onClick={() => handlePageChange(1)}>Next</button>
            
        </div>

        </div>
    )
}

export default ListVenue