

# Python script to automate signup proces for leftover vaccines in Region hovedstaden (REGIONH)

# REQUIREMENTS
# selenium - pip install selenium

# INSTRUCTIONS


NAME = "NAME"
ALDER = "AGE"
PHONE = "123456789"
POSTNR = 'POSTNR + BY'
ADDRESSE = 'ADRESSE'

# Change the strings below to match your information. Only one location can be submitted, so if you need to submit multiple locations, comment/uncomment lines and run again.
LOCATION = '/html/body/div/form/div[1]/div/table/tbody/tr[2]/td/div/span[1]/label' # Ballerup, Baltorpvej 18
#LOCATION = '/html/body/div/form/div[1]/div/table/tbody/tr[2]/td/div/span[6]/label' # Øksnehallen, Halmtorvet 11, København V
#LOCATION = '/html/body/div/form/div[1]/div/table/tbody/tr[2]/td/div/span[4]/label' # Hillerød, Østergade 8
#LOCATION = '/html/body/div/form/div[1]/div/table/tbody/tr[2]/td/div/span[2]/label' # Bella Center, Ørestad Boulevard/Martha Christensens Vej, København S


#####################################################

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

driver = webdriver.Chrome(ChromeDriverManager().install()) #Check if newest chrome driver is installed
now = datetime.now()
chrome_options = Options()
#chrome_options.add_argument("--headless")

start_url = "https://www.regionh.dk/presse-og-nyt/pressemeddelelser-og-nyheder/Sider/Tilbud-om-daglig-venteliste-til-restvacciner.aspx"
driver.get(start_url)

name_field = '//*[@id="t50100775"]'
dob_field = '//*[@id="n35965768"]'
address_field = '//*[@id="t50088645"]'
phone_field = '//*[@id="n50088775"]'
nextbut = '/html/body/div/form/div[2]/div[3]/input'
vacurl = '//*[@id="PageContent__ControlWrapper_RichHtmlField"]/ul/li/a'
post_field = '//*[@id="t50088674"]'

cookieaccept = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="coiPage-1"]/div[3]/div[1]/div[2]/button')))
cookieaccept.click()
driver.find_element_by_xpath(vacurl).click()

driver.find_element_by_xpath(nextbut).click()
driver.find_element_by_xpath(name_field).send_keys(NAME)
driver.find_element_by_xpath(nextbut).click()
driver.find_element_by_xpath(dob_field).send_keys(ALDER)
driver.find_element_by_xpath(nextbut).click()
driver.find_element_by_xpath(address_field).send_keys(ADDRESSE)
driver.find_element_by_xpath(nextbut).click()
driver.find_element_by_xpath(post_field).send_keys(POSTNR)
driver.find_element_by_xpath(nextbut).click()
driver.find_element_by_xpath(phone_field).send_keys(PHONE)
driver.find_element_by_xpath(nextbut).click()
driver.find_element_by_xpath(LOCATION).click()
driver.find_element_by_xpath(nextbut).click()
driver.find_element_by_xpath(nextbut).click()
driver.find_element_by_xpath(nextbut).click()

print('Mange tak for din registrering og for din interesse i en mulig vaccination med en overskudsvaccine! DATO FOR OPSKRIVNING {}'.format(now.strftime("%d/%m/%Y %H:%M")))

