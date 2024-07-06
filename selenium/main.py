from time import sleep
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://app.prizepicks.com/'
path = '/Users/alex/Downloads/chromedriver_mac64/chromedriver'

driver = webdriver.Chrome(path)
driver.get(url)

sounds_good = driver.find_element('xpath', '/html/body/div[2]/div[3]/div/div/div[3]/button')
sounds_good.click()
mlb_live = driver.find_element('xpath', '//div[@class="name"][normalize-space()="MLBLIVE"]')
mlb_live.click()
props = WebDriverWait(driver, 20).until(
 EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.projection')))

pitchers = []

for prop in props:
    name = prop.find_element('xpath', './/div[@class="name"]').text
    team = prop.find_element('xpath', './/div[@class="team-position"]').get_attribute('innerHTML')
    innings = prop.find_element('xpath', './/div[@class="opponent"]').get_attribute('innerHTML')
    K = prop.find_element('xpath', './/div[@class="presale-score"]').get_attribute('innerHTML')

    print(name, team, innings, K)

    player = {
        'Name': name,
        'Team': team,
        'Innings': innings,
        'K': K,
        }

    pitchers.append(player)

#Put the list in a dataframe
df = pd.DataFrame(pitchers)


time.sleep(3)