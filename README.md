# TrenerAI_app
Repozytorium z backendem/frontendem aplikacji

### Poziom Aktywnosci
- 1.2 -	Siedzący tryb życia	| Brak aktywności, praca biurowa
- 1.375 - Lekka aktywność	| Ćwiczenia 1-3x w tygodniu
- 1.55 - Średnia aktywność |	Ćwiczenia 3-5x w tygodniu
- 1.725 - Wysoka aktywność  |	Ćwiczenia 6-7x w tygodniu
- 1.9 -	Bardzo wysoka aktywność |	Sportowiec, praca fizyczna

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
Konsola 1:
```bash
pip install -r requirements.txt
uvicorn --app-dir python app.main:app --host 127.0.0.1 --reload --port 8088
```
Konsola 2:
```bash
npm run frontend:install
npm run frontend:dev
```

### Seedowanie bazy po odpaleniu backendu:

```bash
$env:PYTHONPATH ="sciezka do folderu python"
np: "C:\Users\barte\Desktop\TrenerAI\TrenerAI_app\python"

py -m app.db_seed
```

### Przydatne

Aktualizacja zależności
```bash
pip freeze > requirements.txt
```