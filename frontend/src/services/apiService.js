//This file contains a function to fetch legal information from the Flask API.

// src/services/apiService.js
import axios from 'axios';

// Set up the base URL for your Flask API
const apiClient = axios.create({
    baseURL: 'http://localhost:5000/api', // Use the appropriate port and endpoint
    headers: {
        'Content-Type': 'application/json',
    },
});

export const getLegalInformation = async () => {
    try {
        const response = await apiClient.get('/legal-info');
        return response.data;
    } catch (error) {
        console.error('Error fetching legal information:', error);
        throw error;
    }
};
