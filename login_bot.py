from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

username = driver.find_element(by='id', value='username')
password = driver.find_element(by='id', value='password')
login = driver.find_element(by='css selector', value='button[type="submit"]')

username.send_keys('')
password.send_keys('')

login.click()

input("Press enter to close browser and exit...")