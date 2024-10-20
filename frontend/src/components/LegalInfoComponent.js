//to display the data in your UI.

// src/components/LegalInfoComponent.js
import React, { useEffect, useState } from 'react';
import { getLegalInformation } from '../services/apiService';

const LegalInfoComponent = () => {
    const [legalInfo, setLegalInfo] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {
        // Fetch legal information when the component mounts
        const fetchLegalInfo = async () => {
            try {
                const data = await getLegalInformation();
                setLegalInfo(data);
            } catch (err) {
                setError('Failed to fetch legal information');
            }
        };
        fetchLegalInfo();
    }, []);

    return (
        <div>
            <h2>Legal Information</h2>
            {error && <p>{error}</p>}
            {legalInfo ? (
                <pre>{JSON.stringify(legalInfo, null, 2)}</pre>
            ) : (
                <p>Loading...</p>
            )}
        </div>
    );
};

export default LegalInfoComponent;
