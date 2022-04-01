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
x = "https://state-of-maryland.github.io/COVID19_Cases_DashboardBlackBox/StatisticsSummary.html"

#Total Cases
def get_total_cases(link):
    driver.get(link)
    elem = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "NumberofConfirmedCases")))
    path = driver.find_element(by=By.XPATH, value='//*[@id="NumberofConfirmedCases"]')
    outer = path.get_attribute('outerHTML')
    results = BeautifulSoup(outer, "html.parser")
    return results.find('span').text



#total deaths
def get_total_deaths(link):
    driver.get(link)
    elem = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "NumConfirmedDeaths")))
    path = driver.find_element(by=By.XPATH, value='//*[@id="NumConfirmedDeaths"]')
    outer = path.get_attribute('outerHTML')
    results = BeautifulSoup(outer, "html.parser")
    return results.find('span').text



#currenlty hospital
def get_hospital_total(link):
    driver.get(link)
    elem = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "CurrentHospitalized")))
    path = driver.find_element(by=By.XPATH, value='//*[@id="CurrentHospitalized"]')
    outer = path.get_attribute('outerHTML')
    results = BeautifulSoup(outer, "html.parser")
    return results.find('span').text



df = pd.read_csv("datachart.csv")

#Moving Yesterdays Totals
df.loc[2, 'Cases Yesterday'] = df.loc[1, 'Cases Yesterday']
df.loc[2, 'Currently Hospitalized'] = df.loc[0, 'Currently Hospitalized']
df.loc[2, 'Confirmed Deaths'] = df.loc[0, 'Confirmed Deaths']

#Change in total cases
df.loc[0, 'Cases Yesterday'] = (int(get_total_cases(x).replace(",", "")) - int((df.loc[2, 'Cases Yesterday'][0:-12]).replace(",", ""))

#total Hospitalized
df.loc[0, 'Currently Hospitalized'] = get_hospital_total(x)

#total Dead
df.loc[0, 'Confirmed Deaths'] = get_total_deaths(x)

#total cases yesterday
df.loc[1, 'Cases Yesterday'] = str(get_total_cases(x)) + " total cases"

#change in hospitalizations
df.loc[1, 'Currently Hospitalized'] = "24hr Change: " + str((int(get_hospital_total(x).replace(",", "")) - int(df.loc[2, 'Currently Hospitalized'])))

#change in deaths
df.loc[1, 'Confirmed Deaths'] = "24hr Change: " + str((int(get_total_deaths(x).replace(",", "")) - int(df.loc[2, 'Confirmed Deaths'])))

df.to_csv("datachart.csv", index=False)

driver.quit()