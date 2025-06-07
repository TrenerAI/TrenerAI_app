import Sidebar from "@views/components/Sidebar";
import { Outlet } from "react-router-dom";
import { useEffect, useState } from "react";
import axios from "axios";
import { UserContext, UserData } from "@/context/UserContext";


const API_URL = import.meta.env.VITE_API_URL;

export default function Dashboard() {
  const userId = localStorage.getItem("user_id");
  const [userData, setUserData] = useState<UserData | null>(null);

  useEffect(() => {
    const fetchUser = async () => {
      if (!userId) return;

      try {
        const res = await axios.get(`${API_URL}/user/${userId}/info`);
        const data = res.data;

        setUserData({
          age: data.age ?? 0,
          weight: data.weight ?? 0,
          height: data.height ?? 0,
          gender: data.gender ?? "male",
        });
      } catch (err) {
        console.error("Błąd ładowania danych użytkownika:", err);
      }
    };

    fetchUser();
  }, [userId]);

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-100 to-white flex">
      <Sidebar />
      <main className="flex-1 p-6">
        {userData ? (
          <UserContext.Provider value={userData}>
            <Outlet />
          </UserContext.Provider>
        ) : (
          <p>Ładowanie danych użytkownika...</p>
        )}
      </main>
    </div>
  );
}
