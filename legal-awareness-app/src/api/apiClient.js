// src/api/apiClient.js
//This file will handle all Axios requests to your Flask API.
import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:5000/api', // Replace with your Flask API URL
  headers: {
    'Content-Type': 'application/json',
  },
});

export default apiClient;
