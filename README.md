# TrenerAI_app
Repozytorium z backendem/frontendem aplikacji


# Backend
### Wymagania
- Python 3.13
- pip (menadzer pakietow python)

### Instalacja zależności

```bash 
pip install -r requirements.txt
```

### Sekrety
Utwórz plik **.env** w głownym katalogu projektu  
Dodaj do pliku **.env** 
```bash
DATABASE_URL=
SECRET_KEY=
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
```
O wartości pytaj Cofala  
### Aby uruchomić wpisz:
```bash
uvicorn --app-dir python app.main:app --host 127.0.0.1 --reload --port 8088
```

### Przydatne
Aktualizacja zależności
```bash
pip freeze > requirements.txt
```