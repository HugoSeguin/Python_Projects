#Xpath
#Would need to download selenuim before
from selenium import webdriver
from selenium.webdriver.chrome.options import options
from selenium.webdriver.chrome.service import service
import pandas as pd 
from datetieme import datetime
import os 
import sys

#get the path of the executable that ognna create 
application_path = os.path.dirname(sys.executable)

now = datetime.now()
Mot_day_year = now.strftime("%m%d%Y")



webiste = "https://www.thesun.co.uk/sport/football"
#path to seleinum
path = "/users/hugoseguin/downloads/chromedriver"

#headless mode
options = Options()
options.headless = True


#Create a driver
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options= options)
driver.get(website)

#So the by says how we gonna ceess and vlaue is what we are accessing

container = driver.find_elements(by-"xpath", value='//div[@class="teaser__copy-ontainer"]')

titles = []
subtitles = []
links = []


for container in containers:
    title = contianer.find_elemtn(by="xpath", values='./a/h2').text
    subtitle= contianer.find_elemtn(by="xpath", values='./a/p').text

    link = contianer.find_elemtn(by="xpath", value='./a')get_attribute("href")
    title.append(title)
    subtitle.append(subtitle)
    links.append(links)

my_dict = {'titles':titles, 'subtitle': subtitle, 'link': link}
df_headlines = pd.DataFrame()
file_name = f'headline-{month_day_year}.csv'

final_path = os.path.join(application_path,file_name)

df_headlines.to_csv()

driver.quit()

#chron tab
#09** to run at 9
# then do path so can do path of exectuable
#press exc to save command and do :wq to write and quite tab
#crontab -l so can tell operating system to run executable at 9am everyday
