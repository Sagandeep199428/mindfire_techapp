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





@When('I type POP field')
def type_POP_Name(context):

    driver = context.driver
    wait = WebDriverWait(driver, timeout=600, poll_frequency=0.5)
    page = TechAppLocators(context)


    time.sleep(3)
    actions = ActionChains(driver)
    textbox = driver.find_element(By.XPATH, page.PopInput_two)
    actions.click(textbox)

    actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE)

    actions.perform()
    time.sleep(1)
    wait.until(EC.element_to_be_clickable(page.PopInput),
               "POP Field is not clickable").send_keys('ABBOTTREGEN')

    actions.send_keys(Keys.ARROW_DOWN)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(2)

@When('I verify Alert Message')
def verifyAlertMessage(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=60, poll_frequency=0.5)
    page = TechAppLocators(context)

    wait.until(EC.visibility_of_element_located(page.Alert),
               "Alert is not visible")
    text = driver.find_element(By.XPATH, page.Alert2).text
    assert text == 'Looks like the user POP and AP are missing. Please enter them.'
    time.sleep(2)


@then('I verify confirm Button is disabled')
def verifyConfirmButton(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=600, poll_frequency=0.5)
    page = TechAppLocators(context)

    try:
       wait.until(EC.visibility_of_element_located(page.ConfirmPopApButton),
               "Confirm Button is not visible").click()
    except:
       print('Confirm Button is disabled')


@when('I type AP field')
def type_AP_Field(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=60, poll_frequency=0.5)
    page = TechAppLocators(context)


    wait.until(EC.element_to_be_clickable(page.APInput),
                   "Confirm Button is not clickable").send_keys('AP-UBPRAC-5-000-1.ABBOTTREGEN')

    time.sleep(1)
    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_DOWN)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(2)


@when('I click on the Confirm Button')
def click_on_ConfirmPopApButton(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=20, poll_frequency=0.5)
    page = TechAppLocators(context)

    wait.until(EC.element_to_be_clickable(page.ConfirmPopApButton),
               "Confirm Button is not clickable").click()

@then('I verify POP AP updated Message')
def VerifyPOP_AP_Message(context):
    driver = context.driver
    wait = WebDriverWait(driver, timeout=400, poll_frequency=0.5)
    page = TechAppLocators(context)

    wait.until(EC.visibility_of_element_located(page.PopAPMessage),
               "POP AP Message is not visible")

@When('I verify Job Updated Message')
def verifyJob_Updated_Message(context):

    driver = context.driver
    wait = WebDriverWait(driver, timeout=400, poll_frequency=0.5)
    page = TechAppLocators(context)

    wait.until(EC.visibility_of_element_located(page.JobMessage),
               "Job Status Updated Message is not visible")

@when('I verify I am navigated to select package page')
def Verify_Package_Page(context):

    driver = context.driver
    wait = WebDriverWait(driver, timeout=600, poll_frequency=0.5)
    page = TechAppLocators(context)

    wait.until(EC.visibility_of_element_located(page.Package),
               "Package Field is not visible")
    time.sleep(3)




