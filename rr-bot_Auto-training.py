import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
import os

#Virtual browser
print("Starting virtual browser...")
display = Display(visible=0, size=(1024, 768))
display.start()
time.sleep(2)

#Setup of the driver (Chromedriver)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)



#Set the accounts here
email = "EMAIL_PASSWOED"
password = "PASS"
print("\nLoading Driver...")

def login():
    print("Connecting to RR! ")
    
    #For VK account
    driver.get("https://oauth.vk.com/authorize?client_id=3524629&display=page&scope=notify,friends&redirect_uri=https://rivalregions.com/main/vklogin&response_type=code&state=")
    time.sleep(2)
    inputEmail = driver.find_element_by_name("email")
    inputEmail.send_keys(email)
    inputPassword = driver.find_element_by_name("pass")
    inputPassword.send_keys(password)
    inputPassword.send_keys(Keys.ENTER)
    time.sleep(2)

login() #login to RR



#setup for the bot
def autotrain_bot():
    print("Connected to RR")
    training_link = "https://rivalregions.com/#war/details/383524" #replace it to training link
    time.sleep(6)
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(training_link)
    time.sleep(5)
    train = driver.find_element_by_class_name("button_green.war_w_send_ok")
    train.click()
    time.sleep(2)

    driver.close()


autotrain_bot()
time.sleep(5)
driver.quit()
print("Training per hour done...")
print("The second train will start in 1hour...")


