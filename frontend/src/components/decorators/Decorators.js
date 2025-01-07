import React ,{useState, useEffect, useRef} from "react"
import styles from '../venue/venue.css'
import { data } from "react-router-dom"
import Homepage from "../landing/Homepage"
import ShimmerUI from "../venue/ShimmerUI" 
import DecoratorContainer from "./DecoratorContainer"
    
    
    
const Decorators = () =>{
    
    const [decor, setDecor] = useState([])
    const [city,setCity] = useState("jaipur")
    const [search,setSearch] = useState("")
    const [page, setPage] = useState(1)
    const [loading, setLoading] = useState(true)


    const cache = useRef({}); // Ref to store cached data

    const Decor_URL = `https://www.wedmegood.com/node/v1/vendor/list?category_slug=wedding-decorators&city_slug=${city}&filter_option=&offset=0&device_type=1&page=${page}`
    const URL = `http://127.0.0.1:8000/decor/decors/${city}/?page=${page}`

     

    async function Call() {
        const cacheKey = `${city}-page${page}`
        if (cache.current[cacheKey]) {
            setDecor(cache.current[cacheKey]); // Use cached data
            setLoading(false);
            return;
        }
        setLoading(true);
        const response = await fetch(URL)
        const data = await response.json()
        console.log(data.results)
        setDecor(data.results)
        cache.current[cacheKey] = data.results;
        setLoading(false);
    }

    const handleSearch = () => {
        const value = search.trim().toLowerCase()
        if (value && city !== value) {
            setCity(value);
            setPage(1)
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

    
    console.log(decor)
    
    return (
        <div className="maindivVenue">
        <Homepage/>
        

        <div className="div-srch">
            <div className="div-service" ><h1>Decorators List</h1></div>
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
                        Array.isArray(decor) && decor.length > 0 ? (
                            decor.map((data, index) => (
                                <DecoratorContainer key={index} data={data} />
                            ))
                        ) : (
                            <p>No Decors found!</p>
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

export default Decorators