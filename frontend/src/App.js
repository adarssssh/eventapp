import logo from './logo.svg';
import './App.module.css';
import Login from './components/users/Login';
import Register from './components/users/Register';
import Homepage from './components/landing/Homepage';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';



function App() {

  
  return (
    <>
    <Router>
      <Routes>

        <Route path= '/' element= {<Homepage/>} />
        <Route path= '/login' element= {<Login />} />
        <Route path= '/register' element= {<Register />} />
        

      </Routes>
    </Router>
    
    </>
    
  );
};

export default App;
