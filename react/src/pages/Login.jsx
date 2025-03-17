import { useState } from "react";
import { motion } from "framer-motion";
import { useNavigate } from "react-router-dom";
import { Button, Form, Container, Card } from "react-bootstrap";
import "./Login.css";

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleLogin = (e) => {
    e.preventDefault();
    navigate("/dashboard");
  };

  return (
    <motion.div
      className="login-container"
      initial={{ opacity: 0, scale: 0.9 }}
      animate={{ opacity: 1, scale: 1 }}
      exit={{ opacity: 0, scale: 0.9 }}
      transition={{ duration: 0.8 }}
    >
      <Container className="d-flex flex-column align-items-center justify-content-center vh-100">
        <Card as={motion.div} initial={{ y: -50, opacity: 0 }} animate={{ y: 0, opacity: 1 }} transition={{ duration: 1 }} className="p-4 login-card">
          <h2 className="text-center">
            Trener<span>AI</span>
          </h2>

          <Form onSubmit={handleLogin}>
            <Form.Group className="mb-3">
              <Form.Label>Email</Form.Label>
              <Form.Control type="email" placeholder="Wpisz email" value={email} onChange={(e) => setEmail(e.target.value)} />
            </Form.Group>

            <Form.Group className="mb-3">
              <Form.Label>Hasło</Form.Label>
              <Form.Control type="password" placeholder="Wpisz hasło" value={password} onChange={(e) => setPassword(e.target.value)} />
            </Form.Group>

            <motion.div whileHover={{ scale: 1.1 }} whileTap={{ scale: 0.9 }}>
              <Button variant="danger" type="submit" className="w-100">
                Zaloguj
              </Button>
            </motion.div>
          </Form>
        </Card>
      </Container>
    </motion.div>
  );
};

export default Login;
