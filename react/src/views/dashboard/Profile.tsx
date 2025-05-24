import { useEffect, useState } from "react";
import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL;

export default function Profile() {
  const userId = localStorage.getItem("user_id");

  const [fullName, setFullName] = useState("");
  const [age, setAge] = useState<number>(0);
  const [weight, setWeight] = useState<number>(0);
  const [height, setHeight] = useState<number>(0);
  const [gender, setGender] = useState("male");

  const [editing, setEditing] = useState(false);
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");

 useEffect(() => {
  if (!userId) return;

  const fetchData = async () => {
    try {
      const infoRes = await axios.get(`${API_URL}/user/${userId}/info`);
      const infoRes2 = await axios.get(`${API_URL}/user/${userId}`);
      const info = infoRes.data;
      const info2 = infoRes2.data;

      console.log("INFO:", info); // Debug

      setFullName(info2.full_name ?? "Test")
      setAge(info.age ?? 0);
      setWeight(info.weight ?? 0);
      setHeight(info.height ?? 0);
      setGender(info.gender ?? "male");
    } catch (err) {
      console.error("Błąd ładowania danych profilu", err);
    }
  };

  fetchData();
}, [userId]);

  const handleSave = async () => {
    if (!userId) return;
    setLoading(true);
    setMessage("");

    try {
      await axios.put(`${API_URL}/user/${userId}`, { full_name: fullName });
      await axios.put(`${API_URL}/user/${userId}/info`, {
        age,
        weight,
        height,
        gender,
      });

      setEditing(false);
      setMessage("✅ Zapisano pomyślnie!");
    } catch (err) {
      console.error("Błąd zapisu", err);
      setMessage("❌ Nie udało się zapisać zmian.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-gradient-to-br from-blue-100 to-white px-4">
      <div className="w-full max-w-2xl bg-white shadow-lg rounded-2xl p-8">
        <h2 className="text-2xl font-bold mb-6 text-center text-blue-700">
          Profil użytkownika
        </h2>

        {message && (
          <div className="mb-4 text-sm text-center text-gray-600">{message}</div>
        )}

        <div className="space-y-4">
          <div>
            <label className="block font-medium">Imię i nazwisko:</label>
            <input
              disabled={!editing}
              type="text"
              value={fullName}
              onChange={(e) => setFullName(e.target.value)}
              className="w-full border rounded px-3 py-2"
            />
          </div>

          <div className="grid grid-cols-2 gap-4">
            <div>
              <label className="block font-medium">Wiek:</label>
              <input
                disabled={!editing}
                type="number"
                value={age}
                onChange={(e) => setAge(Number(e.target.value))}
                className="w-full border rounded px-3 py-2"
              />
            </div>
            <div>
              <label className="block font-medium">Waga (kg):</label>
              <input
                disabled={!editing}
                type="number"
                value={weight}
                onChange={(e) => setWeight(Number(e.target.value))}
                className="w-full border rounded px-3 py-2"
              />
            </div>
          </div>

          <div className="grid grid-cols-2 gap-4">
            <div>
              <label className="block font-medium">Wzrost (cm):</label>
              <input
                disabled={!editing}
                type="number"
                value={height}
                onChange={(e) => setHeight(Number(e.target.value))}
                className="w-full border rounded px-3 py-2"
              />
            </div>
            <div>
              <label className="block font-medium">Płeć:</label>
              <select
                disabled={!editing}
                value={gender}
                onChange={(e) => setGender(e.target.value)}
                className="w-full border rounded px-3 py-2"
              >
                <option value="male">Mężczyzna</option>
                <option value="female">Kobieta</option>
                <option value="other">Inna</option>
              </select>
            </div>
          </div>
        </div>

        <div className="mt-6 flex justify-between">
          <button
            onClick={() => setEditing((prev) => !prev)}
            className="bg-gray-200 hover:bg-gray-300 text-gray-800 px-4 py-2 rounded"
          >
            {editing ? "Anuluj" : "Edytuj"}
          </button>
          {editing && (
            <button
              onClick={handleSave}
              className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded"
              disabled={loading}
            >
              {loading ? "Zapisuję..." : "Zapisz zmiany"}
            </button>
          )}
        </div>
      </div>
    </div>
  );
}
