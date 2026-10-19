# User story:
# Som student
# vill jag kunna markera och avmarkera böcker som favoriter
# så att jag vet vilka böcker jag vill läsa.

Feature: Hantera favoriter

  Scenario: Markera en bok som favorit
    Given att jag är på startsidan
    When jag klickar på hjärtat för "Agile Is a Feeling"
    Then ska hjärtat för "Agile Is a Feeling" vara markerat
    And hjärtat för "The Bugs are Coming" ska inte vara markerat

  Scenario: Favoriten visas under Mina böcker
    Given att jag är på startsidan
    When jag klickar på hjärtat för "Agile Is a Feeling"
    And jag går till "Mina böcker"
    Then ska "Agile Is a Feeling" finnas bland mina favoriter
    And texten "Dina favoriter:" ska visas

  Scenario: Ta bort en bok från favoriter
    Given att jag är på startsidan
    And att jag har markerat "Agile Is a Feeling" som favorit
    When jag klickar på hjärtat för "Agile Is a Feeling"
    And jag går till "Mina böcker"
    Then ska "Agile Is a Feeling" inte finnas bland mina favoriter

  Scenario: Klicka tre gånger på hjärtat
    Given att jag är på startsidan
    When jag klickar på hjärtat för "Agile Is a Feeling"
    And jag klickar på hjärtat för "Agile Is a Feeling"
    And jag klickar på hjärtat för "Agile Is a Feeling"
    Then ska hjärtat för "Agile Is a Feeling" vara markerat

  Scenario: Inga favoriter valda
    Given att jag är på startsidan
    When jag går till "Mina böcker"
    Then ska texten "När du valt, kommer dina favoritböcker att visas här." visas
    And listan med favoriter ska vara tom

  Scenario: Flera favoriter visas i en numrerad lista
    Given att jag är på startsidan
    When jag klickar på hjärtat för "Agile Is a Feeling"
    And jag klickar på hjärtat för "The Bugs are Coming"
    And jag går till "Mina böcker"
    Then ska listan med favoriter innehålla 2 böcker
