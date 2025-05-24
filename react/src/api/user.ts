import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL || "http://127.0.0.1:8088";

export const updateFullName = async (userId: string, fullName: string) => {
  return await axios.put(`${API_URL}/user/${userId}`, {
    full_name: fullName,
  });
};

export const updateUserInfo = async (
  userId: string,
  age: number,
  weight: number,
  height: number,
  gender: string
) => {
  return await axios.post(`${API_URL}/user/${userId}/info`, {
    age,
    weight,
    height,
    gender,
  });
};
