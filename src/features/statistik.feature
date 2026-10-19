# User story:
# Som student
# vill jag se hur många böcker som finns och hur många som är hjärtmarkerade
# så att jag får en överblick över listan.

Feature: Se statistik

  Scenario: Statistik från start
    Given att jag är på startsidan
    When jag går till "Statistik"
    Then ska statistiken visa 13 böcker
    And statistiken ska visa 0 hjärtmarkerade böcker

  Scenario Outline: Statistiken räknar favoriter
    Given att jag är på startsidan
    When jag klickar på hjärtat för "<bok>"
    And jag går till "Statistik"
    Then ska statistiken visa <antal> hjärtmarkerade böcker

    Examples:
      | bok                 | antal |
      | Agile Is a Feeling  | 1     |
      | The Bugs are Coming | 1     |

  Scenario: Statistiken räknar två favoriter
    Given att jag är på startsidan
    And att jag har markerat "Agile Is a Feeling" som favorit
    And att jag har markerat "The Bugs are Coming" som favorit
    When jag går till "Statistik"
    Then ska statistiken visa 2 hjärtmarkerade böcker

  Scenario: Statistiken räknar tillagda böcker
    Given att jag är på startsidan
    And att jag har lagt till boken "Clean Code" av "Robert C. Martin"
    When jag går till "Statistik"
    Then ska statistiken visa 14 böcker
