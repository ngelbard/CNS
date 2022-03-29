from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import csv

s = Service("/Users/ngelbard/Downloads/chromedriver")

driver = webdriver.Chrome(service=s)
main_page = driver.get("https://covid.cdc.gov/covid-data-tracker/#county-view?list_select_state=all_states&list_select_county=all_counties&data-type=")
#open a webpage
# Wait a few seconds for load
WebDriverWait(driver, 20)
# select the state dropdown
selectState = Select(driver.find_element(By.XPATH, '//*[@id="community-dropdown-wrapper"]/div[1]/div/div[2]'))
# select state by visible text
selectState.select_by_visible_text('Maryland')
selectCounty = Select(driver.find_element(By.XPATH, '//*[@id="community-dropdown-wrapper"]/div[2]/div/div[2]'))
# select state by visible text
selectCounty.select_by_visible_text('Baltimore County')
# Find the submit button
button = driver.find_element(By.ID, 'go-button')
# clicking on the button
button.click()
# find element by xpath -- the status for the county
path = driver.find_element(by=By.XPATH, value='/html/body/div[7]/div[2]/main/div[2]/div[3]/div/div[1]/div/table/tbody/tr[2]/td[2]/span')
outer = path.get_attribute('outerHTML')
results = BeautifulSoup(outer, "html.parser")
print(results.find('span').text)
driver.quit()

#df = pd.read_csv("covid_counties.csv")
#df.loc[0, 'VALUE'] = 
#df.loc[1, 'VALUE'] = 
#df.loc[2, 'VALUE'] = 
#df.loc[3, 'VALUE'] = 
#df.loc[4, 'VALUE'] = 
#df.loc[5, 'VALUE'] = 
#df.loc[6, 'VALUE'] = 
#df.loc[7, 'VALUE'] = 
#df.loc[8, 'VALUE'] = 
#df.loc[9, 'VALUE'] = 
#df.loc[11, 'VALUE'] = 
#df.loc[12, 'VALUE'] = 
#df.loc[13, 'VALUE'] = 
#df.loc[14, 'VALUE'] = 
#df.loc[15, 'VALUE'] = 
#df.loc[16, 'VALUE'] = 
#df.loc[17, 'VALUE'] = 
#df.loc[18, 'VALUE'] = 
#df.loc[19, 'VALUE'] = 
#df.loc[20, 'VALUE'] = 
#df.loc[21, 'VALUE'] = 
#df.loc[22, 'VALUE'] = 
#df.loc[23, 'VALUE'] = 
#df.to_csv("covid_counties.csv", index=False)

