import random
import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from behave import *
#from selenium.webdriver.common import keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Remote as WebDriver, Keys
from selenium.webdriver.support import expected_conditions as EC
from behave_tests.utils.read_properties import configs
from behave_tests.library.projects.ASAP_Project.create_appointment_page import LocatorsCreateAppointmentPage
use_step_matcher("re")

from behave_tests.library.projects.techapp.techapp_locators import TechAppLocators



@when('I click on Create Appointment Page Button')
def click_create_Appointment_page_btn(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)
    page = LocatorsCreateAppointmentPage(context)

    # Verify Create Appointment Page Button is clicked
    error_text = "Create Appointment Page Button is not found/clickable"
    time.sleep(2)
    wait.until(EC.visibility_of_element_located(page.create_appointment_btn), error_text).click()
    time.sleep(5000)

@when('I enter value 88 to Billmax User Number')
def enter_billmax_user_number(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)
    page = LocatorsCreateAppointmentPage(context)

    # Verify Sooner Service Text Area value is entered
    error_text = "Sooner Service Text Area is not found/clickable"
    time.sleep(1)
    wait.until(EC.visibility_of_element_located(page.billmax_user_number), error_text).click()
    time.sleep(1)
    error_text1 = "Sooner Service Text Area value is not entered"
    wait.until(EC.visibility_of_element_located(page.billmax_user_number), error_text1).send_keys("290262")


@when('I click on Get User Button')
def click_get_user_btn(context):
    driver = context.driver

    wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)
    page = LocatorsCreateAppointmentPage(context)

    # Verify Get User Button Button is clicked
    error_text = "Get User Button is not found/clickable"
    time.sleep(2)
    wait.until(EC.visibility_of_element_located(page.get_user_btn), error_text).click()


@when('I validate New Appointment Button is displayed')
def validate_new_appointment_btn(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)
    page = LocatorsCreateAppointmentPage(context)

    # Verify New Appointment Button is displayed
    try:
        time.sleep(1)
        wait.until(EC.visibility_of_element_located(page.new_appointment_btn))

    except TimeoutException:
        error_text = "New Appointment Button is not displayed"
        assert False, error_text



@when('I click on New Appointment Button')
def click_new_appointment_btn(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)
    page = LocatorsCreateAppointmentPage(context)

    # Verify New Appointment Button is clicked
    error_text = "New Appointment Button is not found/clickable"
    time.sleep(1)
    wait.until(EC.visibility_of_element_located(page.new_appointment_btn), error_text).click()





@when('I click on Primary Service type Button')
def click_primary_service_type_btn(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)
    page = LocatorsCreateAppointmentPage(context)

    # Verify Primary Service type Button is clicked
    error_text = "Primary Service type Button is not found/clickable"
    time.sleep(1)
    wait.until(EC.visibility_of_element_located(page.primary_service_type), error_text).click()









@when('I click on Service Call Option')
def click_service_call_option(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)
    page = LocatorsCreateAppointmentPage(context)

    # Verify Service Call Option is clicked
    error_text = "Service Call Option is not found/clickable"
    time.sleep(1)
    wait.until(EC.visibility_of_element_located(page.service_call_option), error_text).click()

@when('I click on Secondary Service Type Button')
def click_secondary_service_type_btn(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)
    page = LocatorsCreateAppointmentPage(context)

    # Verify Secondary Service type Button is clicked
    error_text = "Secondary Service type Button is not found/clickable"
    time.sleep(1)
    wait.until(EC.visibility_of_element_located(page.secondary_service_type), error_text).click()

@then('I click on FTTX Option displayed')
def click_standard_option(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)
    page = LocatorsCreateAppointmentPage(context)

    # Verify Standard Option is clicked
    error_text = "FTTX Option is not found/clickable"
    time.sleep(1)
    wait.until(EC.visibility_of_element_located(page.FTTX_option), error_text).click()





@when('I click on Job Items Button')
def click_job_items(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)
    page = LocatorsCreateAppointmentPage(context)

    # Verify Job Items Button is clicked
    error_text = "Job Items Button is not found/clickable"
    time.sleep(1)
    wait.until(EC.visibility_of_element_located(page.job_items_btn), error_text).click()


@when('I select Inground Job Item from Dropdown')
def select_job_items(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)
    page = LocatorsCreateAppointmentPage(context)

    # Verify existing Job Items Button is changed
    error_text = "Inground Job Items Button is not found/changes"
    time.sleep(1)
    wait.until(EC.visibility_of_element_located(page.Inground), error_text).click()
    actions = ActionChains(driver)
    actions.key_down(Keys.TAB)
    actions.perform()

    #driver.execute_script("arguments[0].scrollIntoView();", page.future_date_needed_yes_option)

    time.sleep(3)

"""
@when('I click on Future Date Needed Yes Option')
def click_future_date_option(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)
    page = LocatorsCreateAppointmentPage(context)

    # Verify Future Date Needed is clicked
    error_text = "Future Date Needed is not found/clickable"
    time.sleep(1)
    wait.until(EC.visibility_of_element_located(page.future_date_needed_yes_option), error_text).click()

"""


"""
@when('I select the Future Date')
def select_future_date(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)
    page = LocatorsCreateAppointmentPage(context)

    # Verify Future Date Selector is clicked
    error_text = "Future Date Selector is not found/clickable"
    time.sleep(1)
    #wait.until(EC.visibility_of_element_located(page.future_date_selector), error_text).click()
    wait.until(EC.visibility_of_element_located(page.date_selector), error_text).send_keys('05/08/2024')
    time.sleep(1)
    #wait.until(EC.visibility_of_element_located(page.next_month), error_text).click()
    #random_integer = random.randint(1, 30)
    time.sleep(1)
    #wait.until(EC.visibility_of_element_located(page.calendar_date), error_text).click()
"""

@when('I click on the Get Available Dates Button')
def click_on_get_availability(context):

    driver = context.driver
    wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)
    page = LocatorsCreateAppointmentPage(context)

    # Verify Availability Dates Button is clicked
    error_text = "Availability Button is not found/clickable"
    time.sleep(1)
    wait.until(EC.visibility_of_element_located(page.get_availability_btn), error_text).click()

@when('I click on the Available Appointment button')
def click_on_available_button(context):

    driver = context.driver
    wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)
    page = LocatorsCreateAppointmentPage(context)

    # Verify Availability Dates Button is clicked
    error_text = "Appointment Available Button is not found/clickable"
    time.sleep(1)
    wait.until(EC.visibility_of_element_located(page.available_apptmntButton), error_text).click()

@when('I click on the Available Appointment Dates')
def click_on_appointmentDate(context):

    driver = context.driver
    wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)
    page = LocatorsCreateAppointmentPage(context)

    # Verify Availability Dates Button is clicked
    error_text = "Appointment Date is not found/clickable"
    time.sleep(1)
    wait.until(EC.visibility_of_element_located(page.appointment_date), error_text).click()
    time.sleep(4)

@when('I click on the Select Dates Button')
def click_on_SelectDates_Button(context):

    driver = context.driver
    wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)
    page = LocatorsCreateAppointmentPage(context)

    # Verify Availability Dates Button is clicked
    error_text = "Select Dates Button is not found/clickable"
    time.sleep(4)
    wait.until(EC.visibility_of_element_located(page.schedule_appointment_btn), error_text).click()

@then('I click on the Schedule Appointment Button')
def click_schedule_appointment_btn(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)
    page = LocatorsCreateAppointmentPage(context)

    # Verify Schedule Appointment Button is clicked
    error_text = "Schedule Appointment Button is not found/clickable"
    time.sleep(4)
    wait.until(EC.visibility_of_element_located(page.finalize_btn), error_text).click()




# technician app steps

@given('The current day appointment, associated with that technician, is visible on my route page')
def verify_techapp_appointment(context):

    driver = context.driver
    wait = WebDriverWait(driver, timeout=20, poll_frequency=0.2)
    page = TechAppLocators(context)
    wait.until(EC.element_to_be_clickable(page.CurrentDate),"Current date is not visible").click()

    wait.until(EC.visibility_of_element_located(page.techAppointment),
               "Appointments is not visible associated with that technician")


@when('I click on appointmentt')
def click_on_appointment(context):

    driver = context.driver
    wait = WebDriverWait(driver, timeout=60, poll_frequency=0.5)
    page = TechAppLocators(context)

    time.sleep(3)
    wait.until(EC.element_to_be_clickable(page.techAppointment),
               "Appointment is not visible").click()
    time.sleep(4)


@then('I should navigate to job details page')
def navigate_to_job_detail_page(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=20, poll_frequency=0.5)

    wait.until(EC.url_contains('technicianapp/jobdetails'),
               "Url does not contain technicianapp/jobdetails")


@when('I click on the Line Icon')
def click_on_Line_Icon(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=20, poll_frequency=0.5)
    page = TechAppLocators(context)
    time.sleep(2)
    wait.until(EC.element_to_be_clickable(page.LineIcon),
               "Line Icon is not visible").click()


@when('I click on On My Way Button')
def click_on_OnMyWay_Button(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=20, poll_frequency=0.5)
    page = TechAppLocators(context)

    wait.until(EC.element_to_be_clickable(page.On_My_Way_Button),
               "OnMyWay Button is not visible").click()
    time.sleep(2)


@when('I click on Start Appointment')
def click_on_StartAppointmentButton(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=25, poll_frequency=0.5)
    page = TechAppLocators(context)
    wait.until(EC.element_to_be_clickable(page.StartAppointmentButton),
               "Start Appointment Button is not clickable").click()


@when('I click on Confirm Button')
def click_on_ConfirmPopApButton(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=20, poll_frequency=0.5)
    page = TechAppLocators(context)

    wait.until(EC.element_to_be_clickable(page.ConfirmPopApButton),
               "Confirm Button is not clickable").click()



@When('I select Add Fiber Service Call Cert Task from task list')
def verify_taskName_in_TaskList(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=600, poll_frequency=0.5)
    page = TechAppLocators(context)

    wait.until(EC.element_to_be_clickable(page.TaskField),
             "Task Field is not clickable").send_keys('Add Fiber Service Call Cert')

    time.sleep(4)

    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_DOWN)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(2)


@when('I click on Start Task')
def click_on_Start_Task(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=20, poll_frequency=0.5)
    page = TechAppLocators(context)

    wait.until(EC.element_to_be_clickable(page.StartTaskButton),
               "Start Task Button is disabled").click()


@when('I enter text in the Cable Test field')
def enter_text_In_CableTest(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=20, poll_frequency=0.5)
    page = TechAppLocators(context)

    wait.until(EC.visibility_of_element_located(page.CableTest),
              "Cable Test Field is not visible").send_keys('4')



@when('I enter text in the second Cable Test field')
def enter_text_In_Second_CableTest(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=20, poll_frequency=0.5)
    page = TechAppLocators(context)

    wait.until(EC.visibility_of_element_located(page.CableTest_Two),
              "Cable Test Second Field is not visible").send_keys('2')
    #time.sleep(6)


@when('I select options from Check Bulkhead field')
def select_Options_CheckBulkhead(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=20, poll_frequency=0.5)
    page = TechAppLocators(context)

    wait.until(EC.visibility_of_element_located(page.BulkheadCheck),
               "Check Bulkhead field is not visible").click()

    wait.until(EC.visibility_of_element_located(page.BulkheadOptionYes),
               "Bulkhead yes option not visible").click()
    time.sleep(1)


@When('I click on the Continue Button')
def click_on_continueButton(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=20, poll_frequency=0.5)
    page = TechAppLocators(context)

    wait.until(EC.element_to_be_clickable(page.ContinueButton),
               "Continue Button is not clickable").click()


@Then('I should navigate to the next page')
def verify_text(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=20, poll_frequency=0.5)
    page = TechAppLocators(context)

    Page2text = wait.until(EC.visibility_of_element_located(page.PageText),
                           "Page2 text not visible").text
    assert Page2text == 'Step 2 of 4'


@when('I select option for Test Cable')
def select_option_testCable(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=20, poll_frequency=0.5)
    page = TechAppLocators(context)

    wait.until(EC.element_to_be_clickable(page.TestCable),
               "Test Cable field is not clickable").click()
    wait.until(EC.element_to_be_clickable(page.TestCableOptionYes),
               "Test Cable Yes Option is not clickable").click()


@when('I select option for Check Cat5 Cable')
def select_option_CheckCat5Cable(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=20, poll_frequency=0.5)
    page = TechAppLocators(context)

    wait.until(EC.element_to_be_clickable(page.Cat5Cable),
               "Check Cat5 Cable field is not clickable").click()
    wait.until(EC.element_to_be_clickable(page.Cat5CableYes),
               "Check Cat5 Cable Yes Option is not clickable").click()


@when('I enter value for light level')
def enter_value_lightLevel(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=20, poll_frequency=0.5)
    page = TechAppLocators(context)

    wait.until(EC.visibility_of_element_located(page.CheckOnt),
               "Check Ont field is not visible").send_keys('8')
    time.sleep(1)



@Then('I should navigate to third page')
def verify_text(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=20, poll_frequency=0.5)
    page = TechAppLocators(context)

    Page3text = wait.until(EC.visibility_of_element_located(page.PageText),
                           "Page3 text not visible").text
    assert Page3text == 'Step 3 of 4'


@when('I enter speeds down value')
def enter_speeds_down_value(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=20, poll_frequency=0.5)
    page = TechAppLocators(context)

    wait.until(EC.visibility_of_element_located(page.SpeedDown),
              "Speeds down field not visible").send_keys('6')


@when('I enter speeds up value')
def enter_speeds_up_value(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=20, poll_frequency=0.5)
    page = TechAppLocators(context)

    wait.until(EC.visibility_of_element_located(page.SpeedUp),
             "Speeds up field not visible").send_keys('8')


@when('I enter Ping value')
def enter_ping_value(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=20, poll_frequency=0.5)
    page = TechAppLocators(context)

    wait.until(EC.visibility_of_element_located(page.ping),
             "Ping field not visible").send_keys('2')
    time.sleep(1)


@When('I click on Continue')
def click_on_continueButton(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=20, poll_frequency=0.5)
    page = TechAppLocators(context)

    wait.until(EC.element_to_be_clickable(page.ContinueButton),
               "Continue Button is not clickable").click()
    time.sleep(1)


@Then('I should navigate to last page')
def verify_text(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=20, poll_frequency=0.5)
    page = TechAppLocators(context)

    Page4text = wait.until(EC.visibility_of_element_located(page.PageText),
                           "Page4 text not visible").text
    assert Page4text == 'Step 4 of 4'


@when('I select Parts Replaced from list')
def select_partsReplaced(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=20, poll_frequency=0.5)
    page = TechAppLocators(context)

    wait.until(EC.element_to_be_clickable(page.partsReplaced),
               "Parts replaced field not visible").click()

    wait.until(EC.element_to_be_clickable(page.equipmentName),
               "Equipment name not visible").click()
    actions = ActionChains(driver)
    actions.key_down(Keys.TAB)
    actions.perform()


@when('I select option for whether fiber needs to be buried')
def select_option_whether_buried(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=20, poll_frequency=0.5)
    page = TechAppLocators(context)
    wait.until(EC.element_to_be_clickable(page.fiberBuried),
               "Fiber buried field not visible").click()
    wait.until(EC.element_to_be_clickable(page.fiberBuriedOptionYes),
               "Fiber buried Option yes not visible").click()


@When('I click on Complete Fiber Cert')
def click_on_complete_fiber_cert(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=20, poll_frequency=0.5)
    page = TechAppLocators(context)

    wait.until(EC.element_to_be_clickable(page.ContinueButton),
               "Complete Fiber Cert Button not clickable").click()


@then('I should be navigated to Task List page')
def Verify_Navigation_to_task_List_Page(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=30, poll_frequency=0.5)
    page = TechAppLocators(context)

    wait.until(EC.visibility_of_element_located(page.TaskField),
               "Task field not visible")
    #time.sleep(4)


@when('I verify message -Task completed successfully')
def verify_task_completionMessage(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=120, poll_frequency=0.5)
    page = TechAppLocators(context)
    print('inside verify message function')
    Message = wait.until(EC.visibility_of_element_located(page.TaskCompleteMessage),
                         "Message is not visible").text
    #print(Message)
    assert Message == 'Task completed successfully.'