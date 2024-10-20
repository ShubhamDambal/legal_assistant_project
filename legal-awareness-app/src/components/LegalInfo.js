// src/components/LegalInfo.js
import React, { useEffect, useState } from 'react';
import apiClient from '../api/apiClient';

const LegalInfo = () => {
  const [legalInfo, setLegalInfo] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchLegalInfo = async () => {
      try {
        const response = await apiClient.get('/legal_info'); // Flask endpoint
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
        {legalInfo.map((info) => (
          <li key={info.id}>
            <strong>Category:</strong> {info.category} <br />
            <strong>Content:</strong> {info.content}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default LegalInfo;
