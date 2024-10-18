import React from "react";
import './Navbar.css';

const Navbar = () => {
  return (
    <>
      <nav>
        <div className="navbar-header">
          <button id="menu">☰</button>
          <a id="logo" className="navbar-brand" href="/">Digital Assitant</a>
          <ul>
            <li><a href="#">About</a></li>
            <li><a href="#">Contact Us</a></li>
            <li><a href="#">Latest</a></li>
            <li><a href="#">Login</a></li>
          </ul>
        </div>
        
      </nav>
    </>
  );
};

export default Navbar;
