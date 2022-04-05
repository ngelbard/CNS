from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

#CNS
#s = Service("/Users/ngelbard/Downloads/chromedriver")
#Laptop
#s = Service("/Users/nolangelbard/Downloads/chromedriver")
chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

counties = [
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
"24035 Queen Anne's",
"24037 Somerset",
"24039 St. Mary's",
"24041 Talbot",
"24043 Washington",
"24045 Wicomico",
"24047 Worcester"]

covid_links = []
for value in counties:
    #open webpage
    covid_links.append("https://covid.cdc.gov/covid-data-tracker/#county-view?list_select_state=Maryland&data-type=CommunityLevels&list_select_county=" + value[:5] + "&null=CommunityLevels")


def get_case_rate(link):
    driver.get('https://www.google.com')
    driver.get(link)    
    # Wait a few seconds for load
    elem = WebDriverWait(driver, 45).until(EC.presence_of_element_located((By.ID, "CCL_cases_per_100K_7_day_count_change")))
    #get covid data
    path = driver.find_element(by=By.XPATH, value='//*[@id="cases-timeseries-wrapper"]/div/div[1]/div/div[1]/div[2]/div[2]/span')
    outer = path.get_attribute('outerHTML')
    results = BeautifulSoup(outer, "html.parser")
    return results.find('span').text

def get_case_number(link):
    driver.get('https://www.google.com')
    driver.get(link)    
    # Wait a few seconds for load
    elem = WebDriverWait(driver, 45).until(EC.presence_of_element_located((By.ID, "CCL_cases_per_100K_7_day_count_change")))
    #get covid data
    path = driver.find_element(by=By.XPATH, value='//*[@id="initialMetric-cases-timeseries"]')
    outer = path.get_attribute('outerHTML')
    results = BeautifulSoup(outer, "html.parser")
    return results.find('span').text

def get_community_level(link):
    driver.get('https://www.google.com')
    driver.get(link)    
    # Wait a few seconds for load
    elem = WebDriverWait(driver, 45).until(EC.presence_of_element_located((By.ID, "CCL_community_burden_level_integer")))
    #get community level
    path2 = driver.find_element(by=By.XPATH, value='//*[@id="CCL_community_burden_level_integer"]')
    outer2 = path2.get_attribute('outerHTML')
    results2 = BeautifulSoup(outer2, "html.parser")
    return results2.find('div').text


df = pd.read_csv("covid_counties.csv")
df.loc[0, 'VALUE'] = get_case_rate(covid_links[0])
df.loc[1, 'VALUE'] = get_case_rate(covid_links[1])
df.loc[2, 'VALUE'] = get_case_rate(covid_links[2])
df.loc[3, 'VALUE'] = get_case_rate(covid_links[3])
df.loc[4, 'VALUE'] = get_case_rate(covid_links[4])
df.loc[5, 'VALUE'] = get_case_rate(covid_links[5])
df.loc[6, 'VALUE'] = get_case_rate(covid_links[6])
df.loc[7, 'VALUE'] = get_case_rate(covid_links[7])
df.loc[8, 'VALUE'] = get_case_rate(covid_links[8])
df.loc[9, 'VALUE'] = get_case_rate(covid_links[9])
df.loc[10, 'VALUE'] = get_case_rate(covid_links[10])
df.loc[11, 'VALUE'] = get_case_rate(covid_links[11])
df.loc[12, 'VALUE'] = get_case_rate(covid_links[12])
df.loc[13, 'VALUE'] = get_case_rate(covid_links[13])
df.loc[14, 'VALUE'] = get_case_rate(covid_links[14])
df.loc[15, 'VALUE'] = get_case_rate(covid_links[15])
df.loc[16, 'VALUE'] = get_case_rate(covid_links[16])
df.loc[17, 'VALUE'] = get_case_rate(covid_links[17])
df.loc[18, 'VALUE'] = get_case_rate(covid_links[18])
df.loc[19, 'VALUE'] = get_case_rate(covid_links[19])
df.loc[20, 'VALUE'] = get_case_rate(covid_links[20])
df.loc[21, 'VALUE'] = get_case_rate(covid_links[21])
df.loc[22, 'VALUE'] = get_case_rate(covid_links[22])
df.loc[23, 'VALUE'] = get_case_rate(covid_links[23])
df.loc[0, 'CASES'] = get_case_number(covid_links[0])
df.loc[1, 'CASES'] = get_case_number(covid_links[1])
df.loc[2, 'CASES'] = get_case_number(covid_links[2])
df.loc[3, 'CASES'] = get_case_number(covid_links[3])
df.loc[4, 'CASES'] = get_case_number(covid_links[4])
df.loc[5, 'CASES'] = get_case_number(covid_links[5])
df.loc[6, 'CASES'] = get_case_number(covid_links[6])
df.loc[7, 'CASES'] = get_case_number(covid_links[7])
df.loc[8, 'CASES'] = get_case_number(covid_links[8])
df.loc[9, 'CASES'] = get_case_number(covid_links[9])
df.loc[10, 'CASES'] = get_case_number(covid_links[10])
df.loc[11, 'CASES'] = get_case_number(covid_links[11])
df.loc[12, 'CASES'] = get_case_number(covid_links[12])
df.loc[13, 'CASES'] = get_case_number(covid_links[13])
df.loc[14, 'CASES'] = get_case_number(covid_links[14])
df.loc[15, 'CASES'] = get_case_number(covid_links[15])
df.loc[16, 'CASES'] = get_case_number(covid_links[16])
df.loc[17, 'CASES'] = get_case_number(covid_links[17])
df.loc[18, 'CASES'] = get_case_number(covid_links[18])
df.loc[19, 'CASES'] = get_case_number(covid_links[19])
df.loc[20, 'CASES'] = get_case_number(covid_links[20])
df.loc[21, 'CASES'] = get_case_number(covid_links[21])
df.loc[22, 'CASES'] = get_case_number(covid_links[22])
df.loc[23, 'CASES'] = get_case_number(covid_links[23])
df.loc[0, 'LEVEL'] = get_community_level(covid_links[0])
df.loc[1, 'LEVEL'] = get_community_level(covid_links[1])
df.loc[2, 'LEVEL'] = get_community_level(covid_links[2])
df.loc[3, 'LEVEL'] = get_community_level(covid_links[3])
df.loc[4, 'LEVEL'] = get_community_level(covid_links[4])
df.loc[5, 'LEVEL'] = get_community_level(covid_links[5])
df.loc[6, 'LEVEL'] = get_community_level(covid_links[6])
df.loc[7, 'LEVEL'] = get_community_level(covid_links[7])
df.loc[8, 'LEVEL'] = get_community_level(covid_links[8])
df.loc[9, 'LEVEL'] = get_community_level(covid_links[9])
df.loc[10, 'LEVEL'] = get_community_level(covid_links[10])
df.loc[11, 'LEVEL'] = get_community_level(covid_links[11])
df.loc[12, 'LEVEL'] = get_community_level(covid_links[12])
df.loc[13, 'LEVEL'] = get_community_level(covid_links[13])
df.loc[14, 'LEVEL'] = get_community_level(covid_links[14])
df.loc[15, 'LEVEL'] = get_community_level(covid_links[15])
df.loc[16, 'LEVEL'] = get_community_level(covid_links[16])
df.loc[17, 'LEVEL'] = get_community_level(covid_links[17])
df.loc[18, 'LEVEL'] = get_community_level(covid_links[18])
df.loc[19, 'LEVEL'] = get_community_level(covid_links[19])
df.loc[20, 'LEVEL'] = get_community_level(covid_links[20])
df.loc[21, 'LEVEL'] = get_community_level(covid_links[21])
df.loc[22, 'LEVEL'] = get_community_level(covid_links[22])
df.loc[23, 'LEVEL'] = get_community_level(covid_links[23])
df.to_csv("covid_counties.csv", index=False)

driver.quit()