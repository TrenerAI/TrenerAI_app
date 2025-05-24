import { Navigate } from "react-router-dom";

export default function RequireAuth({ children }: { children: JSX.Element }) {
  const userId = localStorage.getItem("user_id");
  return userId ? children : <Navigate to="/login" replace />;
}
