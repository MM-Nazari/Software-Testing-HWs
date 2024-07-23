Feature: Generate Blocks

  Scenario: ACoC mode with given characteristics
    Given characteristics are "A=[a1,a2]-B=[b1,b2]"
    And the mode is "ACoC"
    Then generated blocks should be
      |    |    |
      | a1 | b1 |
      | a1 | b2 |
      | a2 | b1 |
      | a2 | b2 |
