from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Firefox()
driver.get("http://www.fbi.gov")
assert "FBI" in driver.title

links = []
links = driver.find_elements(By.TAG_NAME, 'a')

for link in links:
    print(link.get_attribute('href'))

print("The number of links on this page are: ", len(links))
# print(hrefs)




# driver.close()