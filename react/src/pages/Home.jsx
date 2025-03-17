import { useNavigate } from "react-router-dom";
import { motion } from "framer-motion";
import { Button, Container } from "react-bootstrap";
import "./Home.css";

const Home = () => {
  const navigate = useNavigate();

  return (
    <motion.div
      className="home-container"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0, scale: 0.9 }}
      transition={{ duration: 0.8 }}
    >
      <Container className="d-flex flex-column align-items-center justify-content-center">
        {/* Animowany napis */}
        <motion.h1
          className="title"
          initial={{ y: -50, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          transition={{ duration: 1, delay: 0.3 }}
        >
          Trener<span>AI</span>
        </motion.h1>

        {/* Przycisk z animacją kliknięcia */}
        <motion.div
          whileHover={{ scale: 1.1 }}
          whileTap={{ scale: 0.9 }}
        >
          <Button
            variant="danger"
            className="mt-4"
            size="lg"
            onClick={() => navigate("/login")}
            as={motion.button}
            initial={{ y: 50, opacity: 0 }}
            animate={{ y: 0, opacity: 1 }}
            transition={{ duration: 1, delay: 0.5 }}
          >
            Rozpocznij
          </Button>
        </motion.div>
      </Container>
    </motion.div>
  );
};

export default Home;
