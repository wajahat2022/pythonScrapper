from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set the path to the Chrome browser executable
chrome_exe_path = 'C:\\Users\\RGB PC GAMER\\Downloads\\New folder (9)\\chromedriver-win64\\chrome-win64\\chrome.exe'

# Set the path to the ChromeDriver executable
chromedriver_path = 'C:\\Users\\RGB PC GAMER\\Downloads\\New folder (9)\\chromedriver-win64\\chromedriver.exe'

# Create a Service instance
service = Service(executable_path=chromedriver_path)

# Create a new instance of the Chrome driver
options = Options()
options.binary_location = chrome_exe_path
driver = webdriver.Chrome(service=service, options=options)

# Navigate to Google's homepage
driver.get('https://www.google.com')

# Keep the browser open until the user closes it
while True:
    pass
