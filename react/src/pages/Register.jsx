import { useState } from "react";
import API from "../api";

const Register = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleRegister = async (e) => {
    e.preventDefault();
    try {
      await API.post("/register", { email, password });
      alert("Rejestracja udana!");
    } catch (err) {
      console.error("Błąd rejestracji", err);
    }
  };

  return (
    <form onSubmit={handleRegister}>
      <input type="email" placeholder="Email" onChange={(e) => setEmail(e.target.value)} />
      <input type="password" placeholder="Hasło" onChange={(e) => setPassword(e.target.value)} />
      <button type="submit">Zarejestruj</button>
    </form>
  );
};

export default Register;
