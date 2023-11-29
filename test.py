from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
# Configure Chrome options
chrome_options = ChromeOptions()
# Run Chrome in headless mode (no GUI)
# chrome_options.add_argument("--headless")

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Set up the Chrome web driver
driver = webdriver.Chrome(service=ChromeService(
    "./chromedriver.exe"), options=chrome_options)

# URL of the web page you want to scrape

url = f"https://rarible.com/blog/?utm_source=rarible.com&utm_medium=landing-page&utm_campaign=editorial_blog"
driver.get(url)
time.sleep(2)
# Define the scroll amount and duration for smooth scrolling
scroll_amount = 5000  # Adjust this value as needed
scroll_duration = 0.0001  # Adjust this value as needed
# scroll_iterations = 5
# Get the initial height of the page
last_height = driver.execute_script("return window.scrollY")
while True:
    driver.execute_script("window.scrollTo(0, window.scrollY + window.innerHeight);")
    time.sleep(2)    
    new_height = driver.execute_script("return window.scrollY")
    if new_height == last_height:
        break
        
    last_height = new_height  
# articles = driver.find_element(By.CLASS_NAME, "post-feed")
# article_elements = articles.find_elements(By.CLASS_NAME, "post-card")
# articles_list = []
# for article_element in article_elements:
#     article = {
#         "post_tags": article_element.find_element(By.CLASS_NAME, "post-card-tags").text,
#         "post_title": article_element.find_element(By.CLASS_NAME, "post-card-title").text,
#         "post_excerpt": article_element.find_element(By.CLASS_NAME, "post-card-excerpt").text,
#         "post_date": article_element.find_element(By.CLASS_NAME, "post-card-meta-date").text,
#         "post_length": article_element.find_element(By.CLASS_NAME, "post-card-meta-length").text ,
#         "post_image_header": article_element.find_element(By.TAG_NAME, "img").get_attribute("src")
#     } 
#     articles_list.append(article)
# with open("test.json", "w") as json_file:
#     json.dump(articles_list, json_file, indent=4)

driver.close()