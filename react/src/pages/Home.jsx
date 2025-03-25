import React from "react";
import "./Home.css";
import { useNavigate } from "react-router-dom";

const Home = () => {
  const navigate = useNavigate();

  const handleStartClick = () => {
    navigate("/login"); // lub inna ścieżka, np. "/register"
  };

  return (
    <div className="start-page">
      <section className="hero-section">
        <div className="hero-image-container">
          {/* Grafika z folderu public/img */}
          <img
            src="/img/barbell-hero.png"
            alt="Trener podnoszący sztangę"
            className="hero-image"
          />

          {/* Faliste tło */}
          <div className="wave-background"></div>

          {/* Tekst i przycisk na grafice */}
          <div className="hero-text-overlay">
            <h1 className="hero-title">Dołącz do nas!</h1>
            <button className="start-btn" onClick={handleStartClick}>
              Rozpocznij
            </button>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Home;
