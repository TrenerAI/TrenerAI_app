import React, { useState, useContext } from "react";
import axios from "axios";
import { UserContext } from "@/context/UserContext";


export default function Chat() {
  const user = useContext(UserContext);

  const [messages, setMessages] = useState<{ role: string; content: string }[]>([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  if (!user) return <div>Ładowanie danych użytkownika...</div>;

  const { age, weight, height, gender } = user;

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = { role: "user", content: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setLoading(true);

    const systemMessage = {
      role: "system",
      content: `
Jesteś profesjonalnym trenerem personalnym i dietetykiem.
Dane użytkownika:
- Wiek: ${age}
- Waga: ${weight} kg
- Wzrost: ${height} cm
- Płeć: ${gender}
Udzielaj spersonalizowanych porad.
      `.trim(),
    };

    try {
      const response = await axios.post("http://localhost:8088/chat/", {
        messages: [systemMessage, ...messages, userMessage],
      });

      const aiResponse = response.data.response;
      if (aiResponse) {
        setMessages((prev) => [...prev, { role: "assistant", content: aiResponse }]);
      }
    } catch (error) {
      console.error("Błąd podczas wysyłania wiadomości:", error);
      alert("Nie udało się połączyć z serwerem czatu.");
    }

    setLoading(false);
  };

  return (
    <div className="p-6">
      <h2 className="text-2xl font-semibold mb-4">🧠 Chat personalnym</h2>
      <div className="border rounded-md p-4 h-[400px] overflow-y-auto bg-gray-50 mb-4">
        {messages.map((msg, index) => (
          <div
            key={index}
            className={`mb-2 p-2 rounded ${
              msg.role === "user" ? "bg-blue-100 text-right" : "bg-gray-200 text-left"
            }`}
          >
            {msg.content}
          </div>
        ))}
        {loading && <div className="text-gray-500">AI pisze...</div>}
      </div>
      <div className="flex gap-2">
        <input
          className="flex-1 border rounded p-2"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
          placeholder="Zadaj pytanie trenerowi AI..."
        />
        <button
          className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
          onClick={sendMessage}
          disabled={loading}
        >
          Wyślij
        </button>
      </div>
    </div>
  );
}
