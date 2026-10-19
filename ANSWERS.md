# Teorifrågor

## 1. Vad är _skillnaden_ mellan enhetstest, integrationstest, regressionstest och prestandatest?

- **Enhetstest** testar en enskild del av koden, till exempel en metod i en klass, separat från resten av systemet. Om klassen är beroende av en annan klass kan man byta ut den mot en mock, så att testet bara testar det man vill testa. Exempel: att `BookStore.addBook` ger den nya boken rätt id, eller att `toggleFavorite` anropar `FavoriteBooks.add` (med en mockad `FavoriteBooks`).
- **Integrationstest** verifierar att flera moduler samarbetar korrekt och utbyter data på rätt sätt. Exempel: att `toggleFavorite` i `BookStore` lägger till boken i en riktig `FavoriteBooks`-lista.
- **Regressionstest** handlar om att upptäcka en regression, alltså att något som fungerade tidigare slutar fungera när man ändrar eller lägger till ny kod. Man kör de befintliga testerna igen efter varje ändring, helst automatiskt med CI vid varje push.
- **Prestandatest** mäter hur lång tid koden tar att köra, till exempel med pytest-benchmark. Man kan mäta körtiden för olika stora indata och se hur den växer, alltså vilken tidskomplexitet koden har (till exempel O(n) eller O(n²)). Testet kontrollerar inte att resultatet är rätt, utan hur snabbt det tas fram.

## 2. Beskriv hur det går till när man arbetar med TDD

TDD (Test Driven Development) innebär att man skriver testet innan koden, i en cykel som upprepas:

1. **Red:** skriv ett test för något som inte finns ännu. Kör det och se att det misslyckas.
2. **Green:** skriv precis så mycket kod som behövs för att testet ska gå igenom.
3. **Refactor:** förbättra koden utan att ändra vad den gör. Testerna ska fortfarande vara gröna.

Sedan tar man nästa lilla krav och börjar om. Testerna skrivs enligt Arrange, Act, Assert, och fixtures används för att förbereda testerna. Resultatet blir att all kod har tester från början och att man vågar ändra i koden, eftersom testerna säger till om något går sönder.

## 3. Beskriv hur BDD skiljer sig från TDD.

BDD (Behavior Driven Development) togs fram av Dan North 2006 och är en vidareutveckling av TDD. Testerna skrivs fortfarande innan koden, men skillnaden är vad testerna beskriver och vem som kan läsa dem:

- I TDD skriver utvecklaren tekniska tester för metoder och klasser.
- I BDD skrivs testerna som läsbara meningar på nära naturligt språk, så att alla i projektet kan förstå vad systemet ska göra. Fokus ligger på affärsnyttan och det användaren ska kunna göra.

I BDD utgår man från user stories och acceptanskriterier. De skrivs som scenarier i feature-filer med Gherkin (`Feature`, `Scenario`, `Given`, `When`, `Then`, `And`), gärna tillsammans med kunden. Varje steg kopplas sedan till kod i en step-fil, och testerna körs med behave.

## 4. vilka sorters tester skulle du vilja använda? Motivera ditt val.

- **Enhetstester med pytest** för backend-klasserna. De är snabba och pekar ut exakt var felet sitter. Beroenden mellan klasser mockas med pytest-mock, så att varje klass testas för sig. Här skulle jag ha flest tester.
- **Integrationstester med pytest** för att kontrollera att klasserna fungerar tillsammans, till exempel att böcker och favoritlistan hänger ihop. Markers (`unit`, `integration`) gör att man kan köra testerna var för sig.
- **E2E-tester med behave och Playwright** för det användaren gör på sidan: se katalogen, lägga till böcker, favoritmarkera och navigera. Jag skulle utgå från user stories och acceptanskriterier och skriva scenarier i Gherkin, som även beställaren kan läsa. Med designmönstret Page Object blir testkoden återanvändbar och lättare att underhålla. Färre av dessa, eftersom de är långsammare.
- **Prestandatester med pytest-benchmark** för funktioner som kan bli långsamma när listan växer, till exempel sökning eller sortering.
- **CI med GitHub Actions** som kör linting (flake8) och alla tester vid varje push och pull request till main. Tillsammans med branch protection och pull requests blir det svårt att få in kod som inte har testats.

Motivering: enhetstesterna ger snabb återkoppling medan man utvecklar, integrationstesterna visar att delarna fungerar ihop, och E2E-testerna visar att användaren faktiskt kan göra det hen ska. När alla tester körs automatiskt i CI blir de också regressionstester, så att nya funktioner inte förstör det som redan fungerar.
