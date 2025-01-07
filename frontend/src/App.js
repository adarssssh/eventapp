import logo from './logo.svg';
import './App.module.css';
import Login from './components/users/Login';
import Register from './components/users/Register';
import Homepage from './components/landing/Homepage';
import ListVenue from './components/venue/listVenue';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Decorators from './components/decorators/Decorators';
import VendorDetails from './components/venue/VendorDetails';



function App() {

  
  return (
    <>
    <Router>
      <Routes>

        <Route path= '/' element= {<Homepage/>} />
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
