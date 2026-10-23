# Läslistan: testautomatisering

Tester för webbsidan [Läslistan](https://tap-vt26-testautomatisering.github.io/exam/), skrivet i Python med pytest, behave och Playwright.

## 1. Vad jag har testat

### Enhetstester (pytest, `tests/unit/`)

Testar klasserna i `src/book_store.py` och `src/fav_books.py` var för sig.

**BookStore.addBook**
- Boken läggs till sist i listan med rätt titel och författare.
- En ny bok är inte favorit.
- Id blir högsta befintliga id + 1, och två nya böcker får olika id.

**BookStore.toggleFavorite**
- Inga böcker är favoriter från start.
- Ett klick markerar, två klick avmarkerar och tre klick markerar igen.
- Bara den valda boken påverkas.
- Ett okänt id ger `None`.
- Med en mockad `FavoriteBooks` (pytest-mock) kontrolleras att `add` och `remove` anropas med rätt bok och rätt antal gånger.

**FavoriteBooks.add / remove**
- Listan är tom från start.
- Samma bok kan inte läggas till två gånger.
- Att ta bort en bok lämnar övriga böcker kvar.
- Att ta bort en bok som inte finns gör ingenting.

### Integrationstester (pytest, `tests/integration/`)

Testar att `BookStore` och en riktig `FavoriteBooks` fungerar tillsammans:
- Att markera en bok lägger till den i favoritlistan, och att avmarkera tar bort den.
- En nyligen tillagd bok kan bli favorit.
- Favoritlistan stämmer med böckernas `fav`-värden.
- Ett okänt id lämnar favoritlistan orörd.

### BDD/E2E-tester (behave + Playwright, `src/features/`)

User stories och acceptanskriterier finns i [STORIES.md](STORIES.md). Varje user story har en feature-fil, stegen finns i `src/features/steps/` och sidorna beskrivs med Page Object i `src/features/pages/`.

| Feature | Vad som testas |
|---|---|
| `katalog.feature` | Katalogen visas vid start med 13 böcker, varje bok har titel, författare och hjärta. |
| `favoriter.feature` | Markera och avmarkera favoriter, klicka flera gånger, favoriterna under "Mina böcker", tom lista och flera favoriter. |
| `lagg_till_bok.feature` | Lägga till böcker (Scenario Outline), att fälten töms, att en ny bok kan bli favorit och när knappen är aktiv eller inaktiverad. |
| `statistik.feature` | Antal böcker och hjärtmarkerade böcker, och att siffrorna uppdateras. |
| `navigering.feature` | Byta mellan alla fyra vyer (Scenario Outline), att aktiv knapp är inaktiverad och att favoriter finns kvar vid vybyte. |

Totalt: 25 pytest-tester och 28 BDD-scenarier. Koden kontrolleras även med flake8.

### CI

Alla tester körs automatiskt med GitHub Actions (`.github/workflows/tests.yml`) vid push och pull request till `master`. Webbläsaren körs headless.

## 2. Hur man startar projektet

Filen `requirements.txt` innehåller alla paket som ska installeras.

```bash
git clone <repo-url>
cd Exam_L-listan
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
playwright install
```

(På macOS/Linux aktiveras miljön med `source .venv/bin/activate`.)

Kör testerna i projektets rotmapp:

```bash
pytest     # enhets- och integrationstester
behave     # BDD-testerna
flake8     # linting
```

Bara enhetstester eller integrationstester:

```bash
pytest -m unit
pytest -m integration
behave src/features/statistik.feature
```

BDD-testerna körs headless. För att se webbläsaren, ändra `headless=True` till `headless=False` i `src/features/environment.py`.

## Mappstruktur

```text
root/
├── .github/workflows/tests.yml
├── src/
│   ├── book_store.py
│   ├── fav_books.py
│   └── features/
│       ├── pages/
│       ├── steps/
│       └── environment.py
├── tests/
│   ├── integration/
│   └── unit/
├── conftest.py
├── behave.ini
├── pytest.ini
├── setup.cfg
├── requirements.txt
├── README.md
├── STORIES.md
└── ANSWERS.md
```
