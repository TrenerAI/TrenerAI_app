import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Login from "@views/auth/Login";
import Register from "@views/auth/Register";
import ProfileSetup from "@views/auth/ProfileSetup";
import Dashboard from "@views/dashboard/Dashboard";
import RequireAuth from "@components/RequireAuth";
import RedirectIfAuth from "@components/RedirectIfAuth";
import Profile from "@views/dashboard/Profile";
import Metrics from "@views/dashboard/Metrics";
import Training from "@views/dashboard/Training";


export default function AppRoutes() {
  return (
    <BrowserRouter>
      <Routes>
        <Route
  path="/login"
  element={
    <RedirectIfAuth>
      <Login />
    </RedirectIfAuth>
  }
/>
        <Route
  path="/register"
  element={
    <RedirectIfAuth>
      <Register />
    </RedirectIfAuth>
  }
/>
        <Route
  path="/setup-profile"
  element={
    <RequireAuth>
      <ProfileSetup />
    </RequireAuth>
  }
/>
        <Route
          path="/dashboard"
          element={
            <RequireAuth>
              <Dashboard />
            </RequireAuth>
          }
        >
          <Route path="profile" element={<Profile />} />
          <Route path="training" element={<Training />} />
          <Route path="metrics" element={<Metrics />} />
        </Route>

        <Route path="*" element={<Navigate to="/login" />} />
      </Routes>
    </BrowserRouter>
  );
}
