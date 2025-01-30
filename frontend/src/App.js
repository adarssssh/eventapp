import logo from './logo.svg';
import './App.module.css';
import Login from './components/pages/users/Login';
import Register from './components/pages/users/Register';
import Homepage from './components/pages/landing/Homepage';
import ListVenue from './components/pages/venue/listVenue';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Decorators from './components/pages/decorators/Decorators';
import VendorDetails from './components/pages/venue/VendorDetails';
import Home from './components/pages/Home/Home';



function App() {

  
  return (
    <>
    <Router>
      <Routes>

        <Route path= '/' element= {<Homepage/>} />
        <Route path= '/about' element= {<Homepage/>} />
        <Route path= '/home' element= {<Home/>} />
        <Route path= '/contact' element= {<Homepage/>} />
        <Route path= '/login' element= {<Login />} />
        <Route path= '/register' element= {<Register />} />
        <Route path = '/venue' element = {<ListVenue />} />
        <Route path= '/decorators' element={<Decorators/>} />
        
        <Route path="/vendor/:vendorId" element={<VendorDetails />} />
        

      </Routes>
    </Router>
    
    </>
    
  );
};

export default App;
