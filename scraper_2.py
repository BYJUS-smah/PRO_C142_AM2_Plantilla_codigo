from selenium import webdriver
from bs4 import BeautifulSoup
#add requests module

import time
import csv
START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"
browser = webdriver.Edge("./msedgedriver.exe")
browser.get(START_URL)
time.sleep(10)

#add hyperlink in headers
headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]
planet_data = []

def scrape():
    for i in range(1, 490):
        #Write while loop here

        for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            #Create hyperlink here

        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
        #print page number 

#Create a new function here

scrape()

#Call the function for each exoplanet


# Create a list called final_planet_data and store elementwise data


#Create final_csv and write all the scraped data into it