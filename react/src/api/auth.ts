import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL || "http://127.0.0.1:8088";

export const login = async (email: string, password: string) => {
  const formData = new URLSearchParams();
  formData.append("username", email);
  formData.append("password", password);

  const response = await axios.post(`${API_URL}/auth/login`, formData, {
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
  });

  return response.data;
};

export const register = async (email: string, password: string) => {
  const response = await axios.post(`${API_URL}/auth/register`, {
    email,
    password,
  });
  return response.data;
};
