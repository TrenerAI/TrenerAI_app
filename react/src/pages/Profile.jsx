import { useEffect, useState } from "react";
import API from "../api";

const Profile = () => {
  const [user, setUser] = useState(null);
  const userId = 1; // TODO: Pobierać z JWT lub localStorage

  useEffect(() => {
    API.get(`/users/${userId}/info`)
      .then((res) => setUser(res.data))
      .catch((err) => console.error("Błąd pobierania profilu", err));
  }, []);

  const updateProfile = async () => {
    try {
      await API.put(`/users/${userId}/info`, { ...user });
      alert("Profil zaktualizowany!");
    } catch (err) {
      console.error("Błąd aktualizacji profilu", err);
    }
  };

  return user ? (
    <div>
      <h2>Profil użytkownika</h2>
      <input type="text" value={user.full_name} onChange={(e) => setUser({ ...user, full_name: e.target.value })} />
      <button onClick={updateProfile}>Zapisz zmiany</button>
    </div>
  ) : (
    <p>Ładowanie...</p>
  );
};

export default Profile;
