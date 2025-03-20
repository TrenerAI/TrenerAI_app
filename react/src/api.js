import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8000", // Adres backendu
  headers: { "Content-Type": "application/json" }
});

// Przechwytujemy żądania i dodajemy token JWT do autoryzowanych zapytań
API.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default API;
