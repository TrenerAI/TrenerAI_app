import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { updateFullName, updateUserInfo } from "@api/user";

export default function ProfileSetup() {
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [age, setAge] = useState<number | "">("");
  const [height, setHeight] = useState<number | "">("");
  const [weight, setWeight] = useState<number | "">("");
  const [gender, setGender] = useState("male");

  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const userId = localStorage.getItem("user_id");
    if (!userId) return navigate("/login");

    setLoading(true);
    setError("");

    try {
      const fullName = `${firstName} ${lastName}`;
      await updateFullName(userId, fullName);
      await updateUserInfo(userId, Number(age), Number(weight), Number(height), gender);
      navigate("/dashboard");
    } catch (err) {
      setError("Wystąpił błąd podczas zapisu danych.");
    } finally {
      setLoading(false);
    }
  };

  return (
  <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-100 to-white px-4">
    <div className="w-full max-w-lg bg-white rounded-2xl shadow-lg p-8">
      <h2 className="text-2xl font-bold text-center mb-6">Uzupełnij swój profil</h2>
      {error && <p className="text-red-500 text-center text-sm mb-4">{error}</p>}

      <form onSubmit={handleSubmit} className="grid grid-cols-2 gap-4">
        <input
          type="text"
          placeholder="Imię"
          value={firstName}
          onChange={(e) => setFirstName(e.target.value)}
          className="col-span-1 border p-2 rounded"
          required
        />
        <input
          type="text"
          placeholder="Nazwisko"
          value={lastName}
          onChange={(e) => setLastName(e.target.value)}
          className="col-span-1 border p-2 rounded"
          required
        />

        <input
          type="number"
          placeholder="Wiek"
          value={age}
          onChange={(e) => setAge(e.target.value === "" ? "" : Number(e.target.value))}
          className="col-span-1 border p-2 rounded"
          required
        />
        <input
          type="number"
          placeholder="Wzrost (cm)"
          value={height}
          onChange={(e) => setHeight(e.target.value === "" ? "" : Number(e.target.value))}
          className="col-span-1 border p-2 rounded"
          required
        />

        <input
          type="number"
          placeholder="Waga (kg)"
          value={weight}
          onChange={(e) => setWeight(e.target.value === "" ? "" : Number(e.target.value))}
          className="col-span-2 border p-2 rounded"
          required
        />

        <div className="col-span-2">
          <label className="block mb-2 font-medium">Płeć:</label>
          <div className="flex gap-6">
            <label className="flex items-center gap-2">
              <input
                type="radio"
                value="male"
                checked={gender === "male"}
                onChange={(e) => setGender(e.target.value)}
              />
              Mężczyzna
            </label>
            <label className="flex items-center gap-2">
              <input
                type="radio"
                value="female"
                checked={gender === "female"}
                onChange={(e) => setGender(e.target.value)}
              />
              Kobieta
            </label>
          </div>
        </div>

        <button
          type="submit"
          disabled={loading}
          className="col-span-2 bg-blue-600 text-white py-2 rounded hover:bg-blue-700 transition"
        >
          {loading ? "Zapisywanie..." : "Zapisz i przejdź dalej"}
        </button>
      </form>
    </div>
  </div>
);
}
