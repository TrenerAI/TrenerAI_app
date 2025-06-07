import { Navigate } from "react-router-dom";

export default function RedirectIfAuth({ children }: { children: JSX.Element }) {
  const userId = localStorage.getItem("user_id");
  return userId ? <Navigate to="/dashboard" replace /> : children;
}
