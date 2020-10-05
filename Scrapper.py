import sys
import time
import requests
import json
sys.path.insert(0, '/usr/lib/chromium-browser/chromedriver')
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
wd = webdriver.Chrome('chromedriver', chrome_options=chrome_options)

#directing discord to the right place
baseurl = "https://discordapp.com/api/webhooks/"
chanID = //your channel here
authcode = "/" //your auth code here
nvidialink = "https://www.nvidia.com/en-us/shop/geforce/gpu/?page=1&limit=9&locale=en-us&category=GPU&gpu=RTX%203080"

#Check stock + time
#Ping when there is stock
yes = {"content": 'Stock Avalible <@!"Ping user ID here> \n' + nvidialink}



avail = False
while not avail:
    wd.get("https://www.nvidia.com/en-us/shop/geforce/gpu/?page=1&limit=9&locale=en-us&category=GPU&gpu=RTX%203080")
    time.sleep(10)
    target = wd.find_elements_by_css_selector(
        "a[class='featured-buy-link link-btn brand-green  cta-button stock-grey-out']")
    for t in target:
        if t.get_attribute("href") != "javascript:void(0);":
            avail = True
    no = {"content": time.strftime("%m-%d-%Y %H:%M:%S", time.gmtime()) + " No Stock Available"}
    send = requests.post(baseurl + str(chanID) + authcode, json=no)

send = requests.post(baseurl + str(chanID) + authcode, json=yes)


