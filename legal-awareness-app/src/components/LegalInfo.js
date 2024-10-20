// src/components/LegalInfo.js
//This React component will fetch and display the legal information from your Flask API.

import React, { useEffect, useState } from 'react';
import apiClient from '../api/apiClient';

const LegalInfo = () => {
  const [legalInfo, setLegalInfo] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchLegalInfo = async () => {
      try {
        const response = await apiClient.get('/legal-info'); // Flask endpoint
        setLegalInfo(response.data);
        setLoading(false);
      } catch (error) {
        setError('Failed to fetch legal information');
        setLoading(false);
      }
    };

    fetchLegalInfo();
  }, []);

  if (loading) {
    return <p>Loading...</p>;
  }

  if (error) {
    return <p>{error}</p>;
  }

  return (
    <div>
      <h2>Legal Information</h2>
      <ul>
        {legalInfo.map((info, index) => (
          <li key={index}>{info}</li>
        ))}
      </ul>
    </div>
  );
};

export default LegalInfo;
