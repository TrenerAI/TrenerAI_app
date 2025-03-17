import { useNavigate } from "react-router-dom";
import { Button, Container } from "react-bootstrap";
import "./Dashboard.css";

const Dashboard = () => {
  const navigate = useNavigate();

  return (
    <Container className="d-flex flex-column align-items-center justify-content-center vh-100 dashboard-container">
      <h1 className="mb-4">Witaj w Trener<span>AI</span></h1>
      
      <Button variant="primary" className="mb-3 w-50" onClick={() => navigate("/profile")}>
        Profil
      </Button>
      
      <Button variant="success" className="mb-3 w-50" onClick={() => navigate("/history")}>
        Historia treningów
      </Button>
      
      <Button variant="warning" className="mb-3 w-50" onClick={() => navigate("/indicators")}>
        Twoje wskaźniki
      </Button>
    </Container>
  );
};

export default Dashboard;
