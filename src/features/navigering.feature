# User story:
# Som student
# vill jag kunna växla mellan Katalog, Lägg till bok, Mina böcker och Statistik
# så att jag snabbt hittar det jag vill göra.

Feature: Navigera mellan vyerna

  Scenario Outline: Byta vy via menyn
    Given att jag är på startsidan
    When jag går till "<vy>"
    Then ska vyn "<vy>" visas
    And knappen "<vy>" ska vara inaktiverad

    Examples:
      | vy            |
      | Katalog       |
      | Lägg till bok |
      | Mina böcker   |
      | Statistik     |

  Scenario: Favoriter finns kvar när jag byter vy
    Given att jag är på startsidan
    And att jag har markerat "Agile Is a Feeling" som favorit
    When jag går till "Statistik"
    And jag går till "Katalog"
    Then ska hjärtat för "Agile Is a Feeling" vara markerat
