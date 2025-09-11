import csv
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import date

# Define URl variables
affRefiURL = "https://www.affinityplus.org/rates/mortgage-rates"
rmRefiURL = "https://www.rocketmortgage.com/refinance-rates"
blazeRefiURL = "https://blazecu.com/personal/borrow/mortgage/mortgage-refinance"
magnifiRefiURL = "https://mymagnifi.org/rates/rates-mortgages.html"

# Initialize Chrome webdriver
chrome = webdriver.Chrome()

#1 Get Affinity 30 year refi rate
chrome.get(affRefiURL)
time.sleep(3)
rates = chrome.find_element(By.CLASS_NAME, "ratesTable")
rates_list = rates.text.split("\n")
refi_aff = rates_list[23:29]
aff30refi = refi_aff[2].split(" ")[0]
time.sleep(3)

#2 Get Rocket Mortgage 30 year refi rate
chrome.get(rmRefiURL)
time.sleep(3)
rkt_rates = chrome.find_elements(By.CLASS_NAME, "rkt-Heading-24")
rktRefiRate = rkt_rates[1].text
time.sleep(3)

#3 Get Blaze 30 year refi rate
chrome.get(blazeRefiURL)
time.sleep(3)
blazeRates = chrome.find_element(By.CLASS_NAME, "rates-grid")
blaze30Refi = blazeRates.text.split("\n")[-2:-1]
blaze30Refi_rate = blaze30Refi[0].split(" ")[4]
time.sleep(3)

#4 Get Magnifi 30 year refi rate
chrome.get(magnifiRefiURL)
time.sleep(3)
magnifi = chrome.find_element(By.CLASS_NAME, "table-responsive")
magnifi30Refi = magnifi.text.split("\n")[4].split(" ")[-1:][0]
time.sleep(3)

# Get today's date
rateDate = date.today().strftime("%m/%d/%Y")

# Build list of data
rates = [rateDate, aff30refi, rktRefiRate, blaze30Refi_rate, magnifi30Refi]

# Write data to csv
with open("refiRates.csv", "a", newline = '') as file:
    writer = csv.writer(file, delimiter = ',')
    writer.writerow(rates)

reRates = f"""30 Year Refinance Rates\n\nAffinity Plus Rate: {rates[1]}\nRocket Mortgage Rate: {rates[2]}\nBlaze CU Rate: {rates[3]}\nMagnifi Rate: {rates[4]}"""

# YEET
requests.post(f"https://ntfy.sh/30YrRefi4Lenders",
    data = reRates.encode(encoding = 'utf-8'))