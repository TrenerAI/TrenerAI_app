import { useEffect, useState } from "react";
import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL;

export default function Metrics() {
  const userId = localStorage.getItem("user_id");
  const [bmi, setBmi] = useState<number | null>(null);
  const [bmiCategory, setBmiCategory] = useState("");

  const [activityLevel, setActivityLevel] = useState(1.2);
  const [calories, setCalories] = useState<any>(null);

  const [rir, setRir] = useState(2);
  const [rpe, setRpe] = useState<number | null>(null);
  const [rirError, setRirError] = useState("");

  useEffect(() => {
    if (!userId) return;

    // BMI
    axios.get(`${API_URL}/metrics/${userId}/bmi`)
      .then((res) => {
        setBmi(res.data.bmi);
        setBmiCategory(res.data.category);
      });

    // Kalorie
    axios.get(`${API_URL}/metrics/${userId}/calories`, {
      params: { activity_level: activityLevel }
    }).then((res) => {
      setCalories(res.data.macros);
    });

    // RPE
    if (rir >= 0 && rir <= 10) {
      axios.get(`${API_URL}/metrics/rpe`, { params: { rir } })
        .then((res) => {
          setRpe(res.data.RPE);
          setRirError("");
        });
    } else {
      setRpe(null);
      setRirError("Wartość RIR musi być liczbą od 0 do 10.");
    }
  }, [userId, activityLevel, rir]);

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-100 to-white p-8">
      <div className="max-w-4xl mx-auto bg-white shadow-lg rounded-2xl p-6 space-y-6">
        <h2 className="text-2xl font-bold text-blue-700 text-center">Metryki</h2>

        {/* BMI */}
        <div className="bg-gray-50 rounded p-4">
          <h3 className="font-semibold mb-2">BMI</h3>
          {bmi !== null ? (
            <p>Wskaźnik: <strong>{bmi.toFixed(2)}</strong> — {bmiCategory}</p>
          ) : (
            <p className="text-gray-500">Brak danych BMI.</p>
          )}
        </div>

        {/* Kalorie */}
        <div className="bg-gray-50 rounded p-4 space-y-2">
          <h3 className="font-semibold">Zapotrzebowanie kaloryczne</h3>
          <label className="text-sm font-medium">Poziom aktywności:</label>
          <input
            type="number"
            step="0.001"
            min="1.2"
            max="1.9"
            value={activityLevel}
            onChange={(e) => setActivityLevel(parseFloat(e.target.value))}
            className="mt-1 mb-2 border rounded px-2 py-1 w-28"
          />

          <div className="text-xs text-gray-600 mb-3">
            <h4 className="font-semibold mb-1">📘 Tabela poziomów aktywności:</h4>
            <ul className="list-disc pl-4 space-y-1">
              <li>1.2 – <b>Siedzący tryb życia</b> — Brak aktywności, praca biurowa</li>
              <li>1.375 – <b>Lekka aktywność</b> — Ćwiczenia 1–3x w tygodniu</li>
              <li>1.55 – <b>Średnia aktywność</b> — Ćwiczenia 3–5x w tygodniu</li>
              <li>1.725 – <b>Wysoka aktywność</b> — Ćwiczenia 6–7x w tygodniu</li>
              <li>1.9 – <b>Sportowiec</b> — Bardzo wysoka aktywność lub praca fizyczna</li>
            </ul>
          </div>

          {calories && (
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-sm">
              {["cut", "maintenance", "bulk"].map((key) => (
                <div key={key} className="bg-white p-3 rounded shadow">
                  <h4 className="font-semibold capitalize">{key}</h4>
                  <p>Kalorie: {calories[key].calories}</p>
                  <p>Białko: {calories[key].protein}g</p>
                  <p>Tłuszcze: {calories[key].fats}g</p>
                  <p>Węglowodany: {calories[key].carbs}g</p>
                </div>
              ))}
            </div>
          )}
        </div>

        {/* RPE */}
        <div className="bg-gray-50 rounded p-4 space-y-2">
          <h3 className="font-semibold mb-1">RPE (Rate of Perceived Exertion)</h3>
          <label className="text-sm font-medium">Podaj RIR (Reps in Reserve):</label>
          <input
            type="number"
            min="0"
            max="10"
            value={rir}
            onChange={(e) => setRir(Number(e.target.value))}
            className="mt-1 border rounded px-2 py-1 w-24"
          />
          {rirError && <p className="text-red-500 text-sm">{rirError}</p>}
          {rpe !== null && (
            <p>Twoje RPE: <strong>{rpe}</strong></p>
          )}

          <div className="text-xs text-gray-600 mt-2">
            <h4 className="font-semibold">📘 Czym jest RPE?</h4>
            <ul className="list-disc pl-4 space-y-1">
              <li><b>RIR 0</b> → RPE 10 (maksymalny wysiłek, brak rezerw)</li>
              <li><b>RIR 2</b> → RPE 8 (wysoki wysiłek, 2 powtórzenia w zapasie)</li>
              <li><b>RIR 4</b> → RPE 6 (umiarkowany wysiłek)</li>
              <li>... i tak dalej aż do <b>RIR 10</b> → brak wysiłku</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
}
