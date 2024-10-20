// src/pages/HomePage.js
//This is the main page that will display your UI, including the LegalInfo component.

import React from 'react';
import LegalInfo from '../components/LegalInfo';

const HomePage = () => {
  return (
    <div>
      <h1>Welcome to the Legal Awareness Platform</h1>
      <LegalInfo />
    </div>
  );
};

export default HomePage;
