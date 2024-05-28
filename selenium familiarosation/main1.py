
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the (fake) newsletter registration page
driver.get("https://secure-retreat-92358.herokuapp.com/")

# Find the first name, last name, and email fields
first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")

# Fill out the form
first_name.send_keys("Angela")
last_name.send_keys("Yu")
email.send_keys("angela@email.com")

# Locate the "Sign Up" button. Then click on it
submit = driver.find_element(By.CSS_SELECTOR, value="form button")
submit.click()


Raw
interaction.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to Wikipedia
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Hone in on anchor tag using CSS selectors
article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# article_count.click()

# Find element by Link Text
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# Find the "Search" <input> by Name
search = driver.find_element(By.NAME, value="search")

# Sending keyboard input to Selenium
search.send_keys("Python", Keys.ENTER)



Raw
main.py
from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

# Python.org
driver.get("https://www.python.org/")

# Amazon's Instant Pot
# driver.get("https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/?th=1")

# By.CLASS_NAME (uses amazon.com website)
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")

# Locating strategies for a single element
# By.NAME
search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))

# By.ID
button = driver.find_element(By.ID, value="submit")
# print(button.size)

# By.CSS_SELECTOR
documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)

# By.XPath
bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

# Finding multiple elements
tier_1 = driver.find_elements(By.CLASS_NAME, value="tier-1")

# Challenge: Print the event dates from python.org
event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }
print(events)

# driver.close()
driver.quit()



