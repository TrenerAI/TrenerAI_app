import { NavLink, useNavigate } from "react-router-dom";

const handleLogout = () => {
  localStorage.clear();
  window.location.href = "/login";
};

export default function Sidebar() {
  const linkBase =
    "block px-4 py-2 rounded transition-colors duration-200";
  const activeLink = "bg-blue-100 text-blue-700 font-semibold";
  const inactiveLink = "text-gray-700 hover:bg-gray-100";

  return (
    <aside className="w-64 min-h-screen bg-white shadow-md border-r border-gray-200 flex flex-col">
      <div className="px-6 py-5 border-b border-gray-200">
        <h1 className="text-2xl font-bold text-blue-600">TrenerAI</h1>
      </div>

      <nav className="flex-1 px-4 py-6 space-y-2">
        <NavLink
          to="/dashboard/profile"
          className={({ isActive }) =>
            `${linkBase} ${isActive ? activeLink : inactiveLink}`
          }
        >
          🧍 Profil
        </NavLink>
        <NavLink
          to="/dashboard/training"
          className={({ isActive }) =>
            `${linkBase} ${isActive ? activeLink : inactiveLink}`
          }
        >
          🏋️ Trening
        </NavLink>
        <NavLink
          to="/dashboard/metrics"
          className={({ isActive }) =>
            `${linkBase} ${isActive ? activeLink : inactiveLink}`
          }
        >
          📊 Metryki
        </NavLink>
      </nav>
          <div className="p-4 border-t border-gray-200 text-sm text-gray-600">
  <button
    onClick={handleLogout}
    className="w-full text-left text-red-500 hover:text-red-700 transition"
  >
    🚪 Wyloguj się
  </button>
</div>
      <div className="p-4 border-t border-gray-200 text-sm text-gray-500">
        &copy; 2025 TrenerAI
      </div>
      
    </aside>
  );
}
