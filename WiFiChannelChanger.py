from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("http://192.168.1.1/login.lp")

#Provide the username and the password
element = driver.find_element_by_id("user")
element.send_keys("") # Username here
element = driver.find_element_by_id("password")
element.send_keys("") # Password here

#Click the login button
element = driver.find_element_by_name("ok").click()

#Navigate to channel configuration
element = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/a").click()
element = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td[2]/a[2]").click()

#Read the current selected channel
select = Select(driver.find_element_by_name('36'))
selected_option = select.first_selected_option
print ("Current WiFi Channel: " + selected_option.text)

#Change from channel 11 to 6 or from any channel to 11
if selected_option.text == '11':
    select = Select(driver.find_element_by_name('36'))
    select.select_by_visible_text('6')
else:
    select = Select(driver.find_element_by_name('36'))
    select.select_by_visible_text('11')
selected_option = select.first_selected_option
print ("New WiFi Channel: " + selected_option.text)

#Apply the change
element = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/div/div[1]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/form/table[2]/tbody/tr/td[2]/table/tbody/tr[13]/td/input[1]").click()

#Close the browser/tab
driver.close()