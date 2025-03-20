import { useEffect, useState } from "react";
import API from "../api";

const Indicators = () => {
  const [bmi, setBmi] = useState(null);
  const [calories, setCalories] = useState(null);
  const [rpe, setRpe] = useState(null);
  const userId = 1; // TODO: Pobierać z JWT

  useEffect(() => {
    API.get(`/metrics/${userId}/bmi`).then((res) => setBmi(res.data));
    API.get(`/metrics/${userId}/calories?activity_level=1.2`).then((res) => setCalories(res.data));
    API.get("/metrics/rpe?rir=2").then((res) => setRpe(res.data.RPE));
  }, []);

  return (
    <div>
      <h2>Twoje wskaźniki</h2>
      <p>BMI: {bmi}</p>
      <p>Kalorie: {calories}</p>
      <p>RPE: {rpe}</p>
    </div>
  );
};

export default Indicators;
