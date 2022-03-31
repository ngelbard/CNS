from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

#CNS
#s = Service("/Users/ngelbard/Downloads/chromedriver")
#Laptop
s = Service("/Users/nolangelbard/Downloads/chromedriver")

driver = webdriver.Chrome(service=s)

counties = {
"24001 Allegany",
"24003 Anne Arundel",
"24510 Baltimore City",
"24005 Baltimore County",
"24009 Calvert",
"24011 Caroline",
"24013 Carroll",
"24015 Cecil",
"24017 Charles",
"24019 Dorchester",
"24021 Frederick",
"24023 Garrett",
"24025 Harford",
"24027 Howard",
"24029 Kent",
"24031 Montgomery",
"24033 Prince George's",
"24035 ueen Anne's",
"24037 Somerset",
"24039 St. Mary's",
"24041 Talbot",
"24043 Washington",
"24045 Wicomico",
"24047 Worcester"}

covid_links = []
for value in counties:
    #open webpage
    covid_links.append("https://covid.cdc.gov/covid-data-tracker/#county-view?list_select_state=Maryland&data-type=&null=&list_select_county=" + value[:5])

cases = []
for link in covid_links:
    driver.get(link)    
    # Wait a few seconds for load
    elem = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "CCL_cases_per_100K_7_day_count_change")))
    #get covid data
    path = driver.find_element(by=By.XPATH, value='//*[@id="CCL_cases_per_100K_7_day_count_change"]')
    outer = path.get_attribute('outerHTML')
    results = BeautifulSoup(outer, "html.parser")
    cases.append(results.find('span').text)

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

