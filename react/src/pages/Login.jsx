import { useState } from "react";
import { motion } from "framer-motion";
import { useNavigate } from "react-router-dom";
import API from "../api";
import "./Login.css";

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const res = await API.post("/login", { username: email, password });
      localStorage.setItem("token", res.data.token);
      navigate("/dashboard");
    } catch (err) {
      alert("Błędny login lub hasło");
    }
  };

  return (
    <motion.div
      className="login-wrapper"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
    >
      <div className="login-card">
        <h1 className="logo-title">
          Trener<span className="logo-accent">AI</span>
        </h1>

        <form className="login-form" onSubmit={handleLogin}>
          <div className="form-group">
            <input
              type="email"
              placeholder="TrenerAI@wp.pl"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
            <span className="icon">@</span>
          </div>

          <div className="form-group">
            <input
              type="password"
              placeholder="Hasło"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
            <span className="icon">🔒</span>
          </div>

          <div className="options">
            <label>
              <input type="checkbox" /> Zapamiętaj mnie
            </label>
            <span className="forgot-password">Zapomniane hasło</span>
          </div>

          <button type="submit" className="login-btn">
            Zaloguj
          </button>
        </form>

        <div className="social-login">
          <img src="/img/google-icon.png" alt="Google login" />
          <img src="/img/facebook-icon.png" alt="Facebook login" />
        </div>

        <p className="register-link">
          Nie posiadasz konta? <span>Zarejestruj się</span>
        </p>
      </div>
    </motion.div>
  );
};

export default Login;
