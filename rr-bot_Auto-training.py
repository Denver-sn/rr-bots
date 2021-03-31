import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display

print("Initiating AutoTraining bot")
time.sleep(2)

#Set the accounts here
email = "YOUR_EMAIL_OR_NUMBER"
password = "PASSWORD"
print("\nLoading Driver...")
display = Display(visible=0, size=(1024, 768))
display.start()
time.sleep(1)

#Setup of the driver (Chromedriver)
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)

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


