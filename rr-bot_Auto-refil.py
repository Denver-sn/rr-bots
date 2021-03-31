
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display


#Setup of the driver (Chromedriver)
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)


#Set the accounts here
email = "YOUR_EMAIL_OR_NUMBER"
password = "PASSWORD"
print("\nLoading Driver...")
display = Display(visible=0, size=(1024, 768))
display.start()
time.sleep(1)


def login():
    print("Initiating AutoRefil bot")
    print("Connecting to RR! ")

    # For VK account
    driver.get(
        "https://oauth.vk.com/authorize?client_id=3524629&display=page&scope=notify,friends&redirect_uri=https://rivalregions.com/main/vklogin&response_type=code&state=")
    time.sleep(2)
    inputEmail = driver.find_element_by_name("email")
    inputEmail.send_keys(email)
    inputPassword = driver.find_element_by_name("pass")
    inputPassword.send_keys(password)
    inputPassword.send_keys(Keys.ENTER)
    time.sleep(2)


login()  # login to RR


#setup for the bot
def auto_refil_bot():
    print("Connected to RR")
    time.sleep(7)
    driver.execute_script("window.open('');")

    refil_link = "https://rivalregions.com/parliament/donew/42/0/0"

    driver.switch_to.window(driver.window_handles[1])
    driver.get(refil_link)
    time.sleep(2)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    driver.quit()


time.sleep(2)
print("refil in 2secs...")
auto_refil_bot()
print("Refil done! next refil in 2hours...")




