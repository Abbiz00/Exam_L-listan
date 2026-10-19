# User stories: Läslistan

User stories för den funktionalitet som finns på webbsidan idag. Varje story har acceptanskriterier som ligger till grund för BDD-scenarierna i `src/features/`.

## 1. Se katalogen

**Som** student
**vill jag** se en lista över alla böcker i katalogen
**så att** jag kan hitta böcker som verkar intressanta att läsa.

Acceptanskriterier:
- När sidan öppnas visas vyn "Katalog".
- Varje bok visas med titel och författare.
- Varje bok har ett hjärta som går att klicka på.
- Knappen "Katalog" är inaktiverad när katalogen visas.

## 2. Markera en bok som favorit

**Som** student
**vill jag** kunna klicka på hjärtat vid en bok
**så att** boken sparas bland mina favoriter.

Acceptanskriterier:
- När jag klickar på hjärtat vid en bok markeras hjärtat som valt.
- Boken visas därefter under "Mina böcker".
- Andra böcker påverkas inte.

## 3. Ta bort en bok från favoriter

**Som** student
**vill jag** kunna klicka på hjärtat igen vid en bok som redan är favorit
**så att** boken tas bort från mina favoriter om jag ångrar mig.

Acceptanskriterier:
- När jag klickar på ett valt hjärta avmarkeras det.
- Boken visas inte längre under "Mina böcker".

## 4. Se mina favoriter

**Som** student
**vill jag** se en lista över de böcker jag har valt som favoriter
**så att** jag vet vilka böcker jag vill läsa.

Acceptanskriterier:
- Under "Mina böcker" visas alla böcker jag har hjärtmarkerat, som en numrerad lista med titel.
- Om jag inte har valt några favoriter visas texten "När du valt, kommer dina favoritböcker att visas här."
- Om jag har favoriter visas texten "Dina favoriter:" ovanför listan.

## 5. Lägga till en ny bok

**Som** student
**vill jag** kunna lägga till en bok som saknas i katalogen
**så att** fler kan hitta och läsa den.

Acceptanskriterier:
- Under "Lägg till bok" finns fälten "Titel" och "Författare" och knappen "Lägg till ny bok".
- När jag fyller i båda fälten och klickar på knappen läggs boken till sist i katalogen.
- Efter att boken lagts till töms båda fälten.
- En tillagd bok kan markeras som favorit precis som övriga böcker.

## 6. Hindra ofullständiga böcker

**Som** student
**vill jag** inte kunna lägga till en bok utan titel eller författare
**så att** katalogen inte fylls med ofullständiga uppgifter.

Acceptanskriterier:
- Knappen "Lägg till ny bok" är inaktiverad när titel eller författare är tom.
- Knappen blir aktiv först när båda fälten är ifyllda.

## 7. Se statistik

**Som** student
**vill jag** se hur många böcker som finns och hur många som är hjärtmarkerade
**så att** jag får en överblick över listan.

Acceptanskriterier:
- Under "Statistik" visas "Listan har X böcker." där X är antalet böcker i katalogen (13 från start).
- Där visas också "Våra användare har hjärtmarkerat Y böcker." där Y är antalet favoriter.
- Siffrorna uppdateras när jag lägger till böcker eller ändrar favoriter.

## 8. Navigera mellan vyerna

**Som** student
**vill jag** kunna växla mellan Katalog, Lägg till bok, Mina böcker och Statistik
**så att** jag snabbt hittar det jag vill göra.

Acceptanskriterier:
- Menyn har knapparna "Katalog", "Lägg till bok", "Mina böcker" och "Statistik".
- Ett klick på en knapp visar motsvarande vy.
- Knappen för den vy som visas är inaktiverad.
- Mina favoriter och tillagda böcker finns kvar när jag byter vy.
