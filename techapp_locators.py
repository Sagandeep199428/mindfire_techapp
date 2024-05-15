from selenium.webdriver.common.by import By


class TechAppLocators(object):

    def __init__(self, context=None):
        self.techappMenuButton = (By.XPATH, "//span[normalize-space()='Technician App']")
        self.dashboardMenuButton = (By.XPATH, "//span[normalize-space()='Dashboard']")
        self.HeadingText = (By.CSS_SELECTOR, 'h6[class*="MuiTypography-root MuiTypography-h6 "]')
        #self.MyAppointmentsButton = (By.CSS_SELECTOR, "#techapp-dash-myapp-btn")
        self.MyAppointmentsButton = (By.XPATH, '//button[@id="techapp-dash-myapp-btn"]')
        self.map = (By.XPATH, "//div[@role='application']//canvas")
        self.appointmentsHeadline = (By.XPATH, "//h6[normalize-space()='Appointments']")
        self.vehicleNumber = (By.CSS_SELECTOR, 'svg[data-testid="ToysOutlinedIcon"]')
        self.techAppointmentdate=(By.CSS_SELECTOR,'p[id="date-click_1"]')
        self.techAppointment = (By.CSS_SELECTOR, " div[class*='tech-app-card-shadow']")
        self.customerName = (By.CSS_SELECTOR, 'h5[ class *="MuiTypography-root MuiTypography-h5"]')
        self.customerPhoneNumber= (By.CSS_SELECTOR, 'svg[data-testid="PhoneEnabledOutlinedIcon"]')
        self.customerAddress= (By.CSS_SELECTOR, 'svg[data-testid="LocationOnOutlinedIcon"]')
        self.customerEmail= (By. CSS_SELECTOR, 'svg[data-testid="EmailOutlinedIcon"]')
        self.customerTenure = (By.CSS_SELECTOR, "p> em ")
        self.customerPhoneNumber = (By.CSS_SELECTOR, 'svg[data-testid="PhoneEnabledOutlinedIcon"]')
        self.customerAddress = (By.CSS_SELECTOR, 'svg[data-testid="LocationOnOutlinedIcon"]')
        self.customerEmail = (By.CSS_SELECTOR, 'svg[data-testid="EmailOutlinedIcon"]')
        self.customerTenure = (By.CSS_SELECTOR, "p> em ")
        self.ptoDashboard = (By.CSS_SELECTOR, 'div[class*="MuiCardContent-root "]>div[class*="flex flex-col space"]')
        self.menu = (By.CSS_SELECTOR, 'button[aria-label="menu"] svg')
        self.company_holiday_page = (By.XPATH, "//div[@class='MuiContainer-root MuiContainer-maxWidthTrue css-1hjhp5b']")
        self.company_holiday_btn = (By.XPATH, "//span[normalize-space()='Company Holidays']")
        self.upcoming_holiday_btn = (By.CSS_SELECTOR, 'div[class*="pt"]>div')
        self.add_team_off_day_btn = (By.XPATH, "//span[normalize-space()='Add Team / Zone Days Off']")
        self.date_btn = (By.XPATH, "//button[@aria-label='Choose date']")
        self.input_field = (By.XPATH, "//input[@id='title']")
        self.next_month = (By.XPATH, "//button[@title='Next month']")
        self.date_picker = (By.XPATH, "//button[contains(@class,'MuiButtonBase-root MuiPickersDay-root')]")
        self.create_btn = (By.XPATH, "//button[normalize-space()='Create']")
        self.myTimeoff = (By.XPATH,'//div[contains(text(), "My Time-Off")]')
        self.vehicleNumber_input = (By.XPATH, "/html[1]/body[1]/div[1]/main[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
        self.clock_in = (By.XPATH, "//button[normalize-space()='CLOCK IN']")
        self.techNotes=(By.XPATH,'//p[contains(text(), "Tech Notes")]')

        self.vehicleNumberText = (By.CSS_SELECTOR, "input[type='text']")
        self.clockinButton = (By.XPATH, "//button[normalize-space()='CLOCK IN']")
        self.startBreak = (By.XPATH, "//button[normalize-space()='start break']")
        self.endBreak = (By.XPATH, "//button[normalize-space()='end break']")
        self.clockinText = (By.XPATH, "//p[contains(text(),'Clocked in')]")
        self.clockOut = (By.XPATH, "//button[normalize-space()='Clock Out']")
        self.startBreakText = (By.XPATH, "//p[contains(text(),'Started')]")
        self.endBreakText = (By.XPATH, "//p[contains(text(),'Ended Break')]")

        # Show first appointment
        self.customerName = (By.XPATH, "//h3[@id='firstapp-cname']")
        self.jobStatus = (By.XPATH, "//p[@id='firstapp-status']")
        self.jobType = (By.XPATH, "//p[@id='firstapp-status']")
        self.jobPoints = (By.XPATH, "//p[@id='firstapp-status']")

        # adding locators for add fiber certs task completion
        #self.CurrentDate = (By.XPATH, ('//div[@class="flex mb-5 justify-left"]/p[1]'))
        self.CurrentDate = (By.XPATH, ('//p[@id = "date-click_0"]'))

        #self.CurrentDate = (By.XPATH, ('//p[@class ="MuiTypography-root MuiTypography-body1 mr-4 cursor-pointer css-18aqwmb"]'))
        #self.LineIcon = (By.XPATH, '(//div[starts-with(@class ,  "m-2 cursor-pointer")])[1]')
        self.LineIcon = (By.XPATH, "//div[@class = 'css-e6eurf']")
        self.On_My_Way_Button = (By.XPATH, '//button[@id ="on-my-way"]')
        self.StartAppointmentButton = (By.XPATH, '//button[@id="start-appointment"]')
        self.PopInput = (By.XPATH,'(//input[starts-with(@class, "MuiInputBase-input MuiInput-input MuiInputBase-inputAdornedEnd MuiAutocomplete-input MuiAutocomplete-inputFocused")])[1]')
        self.PopInput_two = '(//input[starts-with(@class, "MuiInputBase-input MuiInput-input MuiInputBase-inputAdornedEnd MuiAutocomplete-input MuiAutocomplete-inputFocused")])[1]'
        self.APInput = (By.XPATH, '(//input[starts-with(@class, "MuiInputBase-input MuiInput-input MuiInputBase-inputAdornedEnd MuiAutocomplete-input MuiAutocomplete-inputFocused")])[2]')
        self.Alert = (By.XPATH, '//div[starts-with(@class,"MuiAlert-message")]')
        self.Alert2 = '//div[starts-with(@class,"MuiAlert-message")]'
        self.AlertMessage = '//div[starts-with(@class,"MuiAlert-message")]/div'
        #message = 'Looks like the user POP and AP are missing. Please enter them.'
        self.PopAPMessage = (By.XPATH, "//div[contains(text(), 'Pop and AP update completed successfully.')]")
        self.JobMessage = (By.XPATH, "//div[contains(text(), 'Job status updated successfully')]")
        self.ConfirmPopApButton = (By.XPATH, '//button[@id="pop-ap"]')
        self.Package = (By.XPATH, '//div[@id="select-package"]')
        self.PackageName = (By.XPATH,
                  '//li[@class ="MuiButtonBase-root MuiMenuItem-root MuiMenuItem-gutters MuiMenuItem-root MuiMenuItem-gutters css-1hluj7q"]')
        # self.expandButton = (By.XPATH, '//*[@class = "MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv"])[11]]')
        self.TaskField = (By.XPATH, '//input[@id="task-autocomplete"]')
        self.StartTaskButton = (By.XPATH, '//button[@id="start-task"]')

        self.CableTest = (By.XPATH, '//input[@id="lightLevelAp"]')
        self.CableTest_Two = (By.XPATH, '//input[@id="lightLevelNid"]')
        self.BulkheadCheck = (By.XPATH, '//div[@class="MuiSelect-select MuiSelect-standard MuiInputBase-input MuiInput-input css-1ni8cox"]')
        self.BulkheadOptionYes = (By.XPATH, '//ul[@class = "MuiList-root MuiList-padding MuiMenu-list css-r8u8y9"]/li[1]')
        self.ContinueButton = (By.XPATH, '//button[@id="fibercertcontinue"]')

        self.PageText = (By.XPATH, '//p[@class="MuiTypography-root MuiTypography-caption MuiTypography-alignLeft mb-5 css-1qr4uxy"]')

        self.TestCable = (By.XPATH, '//div[@id="cableOntNidChecked"]')
        self.TestCableOptionYes = (By.XPATH, '//ul[@class="MuiList-root MuiList-padding MuiMenu-list css-r8u8y9"]/li[1]')
        self.Cat5Cable = (By.XPATH, '//div[@id="cableOntRouterChecked"]')
        self.Cat5CableYes = (By.XPATH, '//ul[@class = "MuiList-root MuiList-padding MuiMenu-list css-r8u8y9"]/li[1]')
        self.CheckOnt = (By.XPATH, '//input[@id="lightLevelOnt"]')

        self.SpeedDown = (By.XPATH, '//input[@id="speedDown"]')
        self.SpeedUp = (By.XPATH, '//input[@id="speedUp"]')
        self.ping = (By.XPATH, '//input[@id="ping"]')

        self.partsReplaced = (By.XPATH, '//div[@id="partsReplaced"]')

        #self.partsReplaced = (By.XPATH,
                             # '//div[@class ="MuiSelect-select MuiSelect-standard MuiSelect-multiple MuiInputBase-input MuiInput-input css-1ni8cox"]')
        self.equipmentName = (By.XPATH, '//ul[@class="MuiList-root MuiList-padding MuiMenu-list css-r8u8y9"]/li[2]')
        self.fiberBuried = (By.XPATH, '//div[@id="fiberNeedBury"]')
        self.fiberBuriedOptionYes = (By.XPATH, '//ul[@class="MuiList-root MuiList-padding MuiMenu-list css-r8u8y9"]/li[1]')
        self.TaskCompleteMessage = (By.XPATH, '//div[contains(text() ,"Task completed successfully")]')















