

@testingTechapp
Feature: Testing


Scenario: Verify POP AP completion
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
        When   I type POP field
        And    I verify Alert Message
        Then  I verify confirm Button is disabled
        When  I type AP field
        And   I click on the Confirm Button
        Then  I verify POP AP updated Message
        When  I verify Job Updated Message
        And   I verify I am navigated to select package page






