Feature:Login functionality
  Background: Common steps
    Given Lanching the chrome browser
    When I open the Amazon home page

  @run_single1_scenario
  Scenario: Validating the login page by providing the valid details
    And Enter the username
    And click the continue button
    And Enter the password
    And click the login button
    Then user should sucessfully login into the Amazon page
  @run_single2_scenario
  Scenario: Login into invalid email
    And Enter the username "shivaiahgarivikasgoud@gail.com"
    And click the continue button
    Then The email error message have to display

  @run_single3_scenario
  Scenario: Login into valid email and invalid password
    And Enter the username "shivaiahgarivikasgoud@gmail.com"
    And click the continue button
    And Enter the password "Vikas"
    And click the login button
    Then The password error message have to display

  @run_single4_scenario
  Scenario Outline: Validating the login page by providing the valid and invalid details
    And Enter the username "<username>"
    And click the continue button
    Then The email error message have to display
    Examples:
      | username |
      | shivaiahga@gail.com |
      | vikkydada421@.com.or|
      | 6475599449jffmkf    |



  @run_single5_scenario
  Scenario Outline: Validating the login page by providing the valid and invalid details
    And Enter the username "<username>"
    And click the continue button
    And Enter the password "<password>"
    And click the login button
    Then The password error message have to display

    Examples:
     |     username        | password    |
     | shivaiahgarivikasgoud@gmail.com |Vikas786    |
     | vikkydada421@gmail.com| VikasVikas  |
     | 9951962196          |  Vikas |


