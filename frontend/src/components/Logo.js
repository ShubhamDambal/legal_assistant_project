import React from 'react'
import './Logo.css'
import logo from './logo.svg'; 

const Logo = () => {
  return (
    <>
      <div className='Log'>
        <img src={logo} alt='LOGO'></img>
        <h1>Digital Assistant for Legal Awareness and</h1>
        <h1>Know-Your-Rights Framework</h1>
      </div>
    </>
  )
}

export default Logo
