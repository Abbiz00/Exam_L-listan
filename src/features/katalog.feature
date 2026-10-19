# User story:
# Som student
# vill jag se en lista över alla böcker i katalogen
# så att jag kan hitta böcker som verkar intressanta att läsa.

Feature: Se katalogen

  Scenario: Katalogen visas när sidan öppnas
    Given att jag är på startsidan
    Then ska vyn "Katalog" visas
    And knappen "Katalog" ska vara inaktiverad
    And katalogen ska innehålla 13 böcker

  Scenario: Varje bok visas med titel, författare och hjärta
    Given att jag är på startsidan
    Then ska boken "Agile Is a Feeling" av "Jeff Sutherland" visas i katalogen
    And boken "Agile Is a Feeling" ska ha ett hjärta
