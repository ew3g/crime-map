//import { React, useEffect } from 'react'
import { React } from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import AppNavbar from './Navbar';
import 'bootstrap/dist/css/bootstrap.min.css';
import Mapa from './Mapa';
//import { useNavigate } from "react-router-dom";



const Home = () => {
    return (
        <div>
            <AppNavbar />
            <Mapa />
        </div>
    )

}

export default Home