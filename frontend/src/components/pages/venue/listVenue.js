
import React ,{useState, useEffect, useRef} from "react"
import styles from '../../../styles/venue.css'
import VenueContainer from "./VenueContainer"
import ShimmerUI from "./ShimmerUI"
import Services from "./Services"
import NavGeneral from "../../Navbar/NavGeneral"
import Footer from "../landing/Footer"






const ListVenue = () => {

    const [venue, setVenue] = useState([])
    const [city,setCity] = useState("jaipur")
    const [search,setSearch] = useState("")
    const [page, setPage] = useState(1)
    const [loading, setLoading] = useState(true)
    const [vendor_id, setVendor_id] = useState("")


    const cache = useRef({}); // Ref to store cached data

    const VENUE_URL = `https://www.wedmegood.com/node/v1/vendor/list?category_slug=wedding-venues&city_slug=${city}&filter_option=&offset=0&device_type=1&page=${page}`
    const URL = `http://127.0.0.1:8000/venue/vendors/${city}/?page=${page}`
    async function Call() {
        const cacheKey = `${city}-page${page}`
        if (cache.current[cacheKey]) {
            setVenue(cache.current[cacheKey]); // Use cached data
            setLoading(false);
            return;
        }
        setLoading(true);
        const response = await fetch(URL)
        const data = await response.json()
        console.log(data)
        setVenue(data.results)
        cache.current[cacheKey] = data.results;
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

    
    
    
    return (
        <>
        <div className="maindivVenue">
        <div className="navGeneral">
        <NavGeneral/>
        </div>
        <Services/>
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
            
            <button onClick={handleSearch}>Search</button>

        </div>
        

        <div className="Listcontainer">
            <div className="Venuecontainer" >
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
        
        <Footer/>
        </>
    )
}

export default ListVenue