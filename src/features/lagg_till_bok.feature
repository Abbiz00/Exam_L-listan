# User story:
# Som student
# vill jag kunna lägga till en bok som saknas i katalogen
# så att fler kan hitta och läsa den.

Feature: Lägga till en ny bok

  Scenario: Lägga till en bok
    Given att jag är på startsidan
    And jag går till "Lägg till bok"
    When jag fyller i titeln "Clean Code"
    And jag fyller i författaren "Robert C. Martin"
    And jag klickar på "Lägg till ny bok"
    And jag går till "Katalog"
    Then ska boken "Clean Code" av "Robert C. Martin" visas i katalogen
    And katalogen ska innehålla 14 böcker

  Scenario: Fälten töms efter att boken lagts till
    Given att jag är på startsidan
    And jag går till "Lägg till bok"
    When jag fyller i titeln "Clean Code"
    And jag fyller i författaren "Robert C. Martin"
    And jag klickar på "Lägg till ny bok"
    Then ska fältet för titel vara tomt
    And fältet för författare ska vara tomt

  Scenario: En tillagd bok kan bli favorit
    Given att jag är på startsidan
    And att jag har lagt till boken "Clean Code" av "Robert C. Martin"
    When jag går till "Katalog"
    And jag klickar på hjärtat för "Clean Code"
    And jag går till "Mina böcker"
    Then ska "Clean Code" finnas bland mina favoriter

  Scenario Outline: Lägga till olika böcker
    Given att jag är på startsidan
    And jag går till "Lägg till bok"
    When jag fyller i titeln "<titel>"
    And jag fyller i författaren "<författare>"
    And jag klickar på "Lägg till ny bok"
    And jag går till "Katalog"
    Then ska boken "<titel>" av "<författare>" visas i katalogen

    Examples:
      | titel                    | författare       |
      | Clean Code               | Robert C. Martin |
      | Refactoring              | Martin Fowler    |
      | The Pragmatic Programmer | Andy Hunt        |

  Scenario: Knappen är inaktiverad när inget är ifyllt
    Given att jag är på startsidan
    When jag går till "Lägg till bok"
    Then ska knappen "Lägg till ny bok" vara inaktiverad

  Scenario: Knappen är inaktiverad när författare saknas
    Given att jag är på startsidan
    And jag går till "Lägg till bok"
    When jag fyller i titeln "Clean Code"
    Then ska knappen "Lägg till ny bok" vara inaktiverad

  Scenario: Knappen är inaktiverad när titel saknas
    Given att jag är på startsidan
    And jag går till "Lägg till bok"
    When jag fyller i författaren "Robert C. Martin"
    Then ska knappen "Lägg till ny bok" vara inaktiverad

  Scenario: Knappen blir aktiv när båda fälten är ifyllda
    Given att jag är på startsidan
    And jag går till "Lägg till bok"
    When jag fyller i titeln "Clean Code"
    And jag fyller i författaren "Robert C. Martin"
    Then ska knappen "Lägg till ny bok" vara aktiv
