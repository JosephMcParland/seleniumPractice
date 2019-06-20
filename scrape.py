from selenium import webdriver
from selenium.webdriver.common.keys import Keys
q = []
driver = webdriver.Chrome(executable_path= r'/Users/mcparlj/Documents/chromedriver')
driver.get("https://www.bbc.com/")
#assert "skysports" in driver.title
x = driver.find_elements_by_css_selector('h3 .top-story__title')

for a in x:
    q.append(a.text)

#elem.clear()
#elem.send_keys("")
#elem.send_keys(Keys.RETURN)

driver.close()
