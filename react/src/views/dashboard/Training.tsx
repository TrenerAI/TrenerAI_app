import { useState } from "react";
import axios from "axios";

const Training = () => {
  const [formData, setFormData] = useState({
    name: "",
    split_type: "FBW",
    goal: "Redukcja",
    days_per_week: 3,
    difficulty: "Poczatkujacy",
  });

  const userId = Number(sessionStorage.getItem("user_id"));

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const mapDifficulty = (diff: string) => {
    switch (diff) {
      case "Poczatkujacy": return "BEGINNER";
      case "Srednio Zaawansowany": return "INTERMEDIATE";
      case "Zaawansowany": return "ADVANCED";
      default: return diff;
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const payload = {
        ...formData,
        difficulty: mapDifficulty(formData.difficulty),
        days_per_week: Number(formData.days_per_week),
      };
      const res = await axios.post(`http://127.0.0.1:8088/training/create?user_id=${userId}`, payload);
      alert("Plan treningowy utworzony!");
      console.log(res.data);
    } catch (err) {
      console.error(err);
      alert("Błąd przy tworzeniu planu.");
    }
  };

  const handleSubmitPDF = async () => {
  try {
    const payload = {
      ...formData,
      difficulty: mapDifficulty(formData.difficulty),
      days_per_week: Number(formData.days_per_week),
    };

    const response = await axios.post(
      `http://127.0.0.1:8088/training/create-fbw-pdf?user_id=${userId}`,
      payload,
      { responseType: "blob" }
    );

    const url = window.URL.createObjectURL(new Blob([response.data]));
    const link = document.createElement("a");
    link.href = url;
    link.setAttribute("download", `${formData.name}_plan.pdf`);
    document.body.appendChild(link);
    link.click();
    link.remove();
  } catch (err) {
    console.error("Błąd podczas pobierania PDF:", err);
    alert("Błąd przy pobieraniu PDF-a.");
  }
};

  return (
    <div className="min-h-screen bg-gradient-to-b from-blue-100 to-white flex items-center justify-center px-4">
      <form onSubmit={handleSubmit} className="bg-white p-8 rounded-lg shadow-md w-full max-w-lg">
        <h2 className="text-2xl font-bold text-center text-blue-600 mb-6">Utwórz plan treningowy</h2>

        <label className="block mb-2 font-semibold">Nazwa:</label>
        <input
          type="text"
          name="name"
          value={formData.name}
          onChange={handleChange}
          className="w-full border rounded p-2 mb-4"
          required
        />

        <label className="block mb-2 font-semibold">Split:</label>
        <select name="split_type" value={formData.split_type} onChange={handleChange} className="w-full border rounded p-2 mb-4">
          <option value="FBW">FBW</option>
          <option value="PPL" disabled>PPL (wkrótce)</option>
          <option value="Góra-Dół" disabled>Góra-Dół (wkrótce)</option>
        </select>

        <label className="block mb-2 font-semibold">Cel:</label>
        <select name="goal" value={formData.goal} onChange={handleChange} className="w-full border rounded p-2 mb-4">
          <option value="Redukcja">Redukcja</option>
          <option value="Siła">Siła</option>
          <option value="Masa">Masa</option>
        </select>

        <label className="block mb-2 font-semibold">Dni w tygodniu:</label>
        <input
          type="number"
          name="days_per_week"
          value={formData.days_per_week}
          onChange={handleChange}
          className="w-full border rounded p-2 mb-4"
          min={1}
          max={7}
        />

        <label className="block mb-2 font-semibold">Poziom trudności:</label>
        <select name="difficulty" value={formData.difficulty} onChange={handleChange} className="w-full border rounded p-2 mb-6">
          <option value="Poczatkujacy">Początkujący</option>
          <option value="Srednio Zaawansowany">Średnio zaawansowany</option>
          <option value="Zaawansowany">Zaawansowany</option>
        </select>

        <div className="flex gap-4">
  
  <button
    type="button"
    onClick={handleSubmitPDF}
    className="w-full bg-green-600 text-white py-2 rounded hover:bg-green-700 transition"
  >
    Pobierz PDF
  </button>
</div>
      </form>
    </div>
  );
};

export default Training;