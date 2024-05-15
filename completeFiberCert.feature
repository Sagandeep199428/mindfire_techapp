

@testingTechapp
Feature: Testing


Scenario: Login to ASAP and navigate to Create Appointment Page
    Given I navigate to "TECH" url
    When  I click on Login Button
    And   I enter "user-1" username
    And   I click on next Button
    And   I enter "user-1" password
    And   I click on submit button
    And   I click on Stay SignedIn as No
    #And   I navigate to homePage
    And   I click on Hamburger Menu Button
    And   I click on Appointments Menu List button
    When   I click on Create Appointment Page Button
    When   I enter value 88 to Billmax User Number
    And    I click on Get User Button
    And    I click on New Appointment Button
    And    I click on Primary Service type Button
    And    I click on Service Call Option
    And    I click on Secondary Service Type Button
    Then   I click on FTTX Option displayed
    When    I click on Job Items Button
    And     I select Inground Job Item from Dropdown
    #And    I click on Optional Supervisor
    #And    I select Optional Supervisor
    #And    I click on Future Date Needed Yes Option
    #And    I select the Future Date
    And    I click on the Get Available Dates Button
    And    I click on the Available Appointment button
    And    I click on the Available Appointment Dates
    And    I click on the Select Dates Button
    Then   I click on the Schedule Appointment Button




#Feature: Technician App Job Details Page
#@STA-343
    Scenario: Verify Fiber cert completion
        Given I navigate to "TECH" url
        When  I click on Login Button
        And   I enter "user-2" username
        And   I click on next Button
        And   I enter "user-2" password
        And   I click on submit button
        And   I click on Stay SignedIn as No
        Then I verify that I am navigated to the Technician app my dashboard page
        When I click the My Appointments button
        Then I verify that i am navigated to map my route page and my appointments section is displayed
        Given The current day appointment, associated with that technician, is visible on my route page
        When  I click on appointmentt
        Then  I should navigate to job details page
        When  I click on the Line Icon
        And   I click on On My Way Button
        And   I click on Start Appointment
        And   I click on Confirm Button
        When  I select Add Fiber Service Call Cert Task from task list
        And   I click on Start Task
        And   I enter text in the Cable Test field
        And   I enter text in the second Cable Test field
        And   I select options from Check Bulkhead field
        When  I click on the Continue Button
        Then  I should navigate to the next page
        When   I select option for Test Cable
        And   I select option for Check Cat5 Cable
        And   I enter value for light level
        When  I click on the Continue Button
        Then  I should navigate to third page
        When   I enter speeds down value
        And   I enter speeds up value
        And   I enter Ping value
        When  I click on the Continue Button
        Then  I should navigate to last page
        When   I select Parts Replaced from list
        And   I select option for whether fiber needs to be buried
        And   I click on Complete Fiber Cert
        Then  I should be navigated to Task List page
        When  I verify message -Task completed successfully





