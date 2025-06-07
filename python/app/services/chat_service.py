import ollama

def generate_response(message: str, user):
    system_prompt = f"""
Jesteś profesjonalnym trenerem personalnym i dietetykiem. Twoim zadaniem jest doradzanie użytkownikowi w zakresie ćwiczeń i diety. 
Profil użytkownika:
- Wiek: {user.age} lat
- Wzrost: {user.height} cm
- Waga: {user.weight} kg

Na podstawie tego profilu, personalizuj każdą odpowiedź. Udzielaj konkretnych, praktycznych i zdrowych porad.
"""

    response = ollama.chat(
        model='llama3',  # lub inny model, np. mistral, gemma...
        messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': message}
        ]
    )

    return {"response": response['message']['content']}
