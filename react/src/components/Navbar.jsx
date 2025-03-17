import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav style={{ padding: "10px", background: "#eee" }}>
      <Link to="/">Home</Link> | 
      <Link to="/history">Historia</Link> | 
      <Link to="/indicators">Wskaźniki</Link> | 
      <Link to="/profile">Profil</Link>
    </nav>
  );
};

export default Navbar;
