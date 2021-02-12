from selenium import webdriver
import pickle
import time

browser = webdriver.Firefox()
browser.get("https://www.avito.ru/sochi/lichnye_veschi?cd=1&d=1")

# for cookie in pickle.load(open('session','rb')):
#     browser.add_cookie(cookie)
# browser.refresh()

sign_in_and_registration_button = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/a")
sign_in_and_registration_button.click()
login_field = browser.find_element_by_xpath("/html/body/div[7]/div/div/div/div/span/div[1]/div[1]/form/div[3]/div/div[1]/div/div/div/label/input")
login_field.send_keys("skrembler@list.ru")
password_field = browser.find_element_by_xpath("/html/body/div[7]/div/div/div/div/span/div[1]/div[1]/form/div[3]/div/div[2]/div/div/div/label/input")
password_field.send_keys("S0_8MDF_AKam")
sign_in_button = browser.find_element_by_xpath("/html/body/div[7]/div/div/div/div/span/div[1]/div[1]/form/div[5]/div/div/div/div/div/button")
sign_in_button.click()
time.sleep(60)
goods = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[3]/div[3]/div[1]/div[4]/div[1]/div[2]/div[1]/a")
new_page = goods.get_attribute("href")
browser.get(new_page)
buy_with_delivery_button =  browser.find_element_by_xpath("/html/body/div[3]/div[1]/div[3]/div[4]/div[2]/div[1]/div/div[2]/div/div[1]/div/span/span/button")
buy_with_delivery_button.click()
phone_filed = browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[1]/div[2]/form/div[2]/div/div[3]/div/div[2]/div[1]/label/input")
print("!!!!!!!!!!!!!!!!",phone_filed.text)

# pickle.dump(browser.get_cookies(),open('session', 'wb'))


