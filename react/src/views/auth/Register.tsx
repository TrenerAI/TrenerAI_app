import { useState } from "react";
import { register } from "@api/auth";
import { useNavigate } from "react-router-dom";

export default function Register() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
  e.preventDefault();
  setError("");

  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email)) {
    setError("Podaj poprawny adres e-mail z domeną.");
    return;
  }

  if (password.length < 8) {
    setError("Hasło musi mieć co najmniej 8 znaków.");
    return;
  }

  setLoading(true);

  try {
    const data = await register(email, password);
    console.log("✅ Zarejestrowano:", data);

    localStorage.setItem("user_id", data.id);
    localStorage.setItem("email", data.email);

    navigate("/setup-profile");
  } catch (err: any) {
    setError(err.response?.data?.detail || "Błąd rejestracji");
  } finally {
    setLoading(false);
  }
};


  return (
    <div className="flex min-h-screen items-center justify-center bg-gradient-to-br from-blue-100 to-white px-4">
      <div className="w-full max-w-md bg-white rounded-2xl shadow-lg p-8">
        <h2 className="text-2xl font-bold text-center text-gray-800 mb-6">
          Zarejestruj się w <span className="text-blue-600">TrenerAI</span>
        </h2>

        {error && <p className="text-red-500 text-sm text-center mb-4">{error}</p>}

        <form onSubmit={handleSubmit} className="space-y-4">
          <input
            type="email"
            className="w-full px-4 py-2 border border-gray-300 rounded-lg"
            placeholder="you@example.com"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
          <input
            type="password"
            className="w-full px-4 py-2 border border-gray-300 rounded-lg"
            placeholder="Hasło"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
          <button
            type="submit"
            disabled={loading}
            className="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 rounded-lg"
          >
            {loading ? "Rejestruję..." : "Zarejestruj się"}
          </button>
          <p className="mt-4 text-sm text-center text-gray-600">
  Masz już konto?{" "}
  <a
    href="/login"
    className="text-blue-600 hover:underline font-medium"
  >
    Zaloguj się
  </a>
</p>

        </form>
        <p className="mt-6 text-xs text-gray-400 text-center">
          &copy; {new Date().getFullYear()} TrenerAI. Wszelkie prawa zastrzeżone.
        </p>
      </div>
    </div>
  );
}
