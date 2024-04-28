import streamlit as st

import csv
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import chromedriver_autoinstaller

def random_user_flow(url, num_actions):
    # Initialize the WebDriver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless') # ensure GUI is off
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chromedriver_autoinstaller.install()

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    actions_performed = 0

    all_links = driver.find_elements(By.TAG_NAME, 'a')  # Finds all anchor tags
    flow = []

    for i in range(1,num_actions+1):
        driver.get(url)
        flow.append(url)
        old_url = url
        st.write(f"Step {i}: {url}")
        all_links = driver.find_elements(By.TAG_NAME, 'a')  # Finds all anchor tags
        url = random.choice(all_links).get_attribute('href')
        if "#" in url or old_url == url:
            while "#" in url or old_url == url:
                url = random.choice(all_links).get_attribute('href')
    return flow

st.header("Understand User Flows")

st.write("Kombu can understand all possible user flows of a webapp! From these, we gather the common webapp use cases. We later generate the Selenium code for these flows in Step 2, and monitor their health in Step 3.")

target_url = st.text_input("Enter URL to Scrape")
col1, col2 = st.columns(2)
with col1:
    number_of_generations = st.number_input("Number of flows to generate", 1, 5)
with col2:
    number_of_actions = st.number_input("Number of actions per flow", 1, 10)
button = st.button("Submit")
flows = []
if button:
    for i in range(1, number_of_generations+1):
        with st.expander(f"Generation {i}:", expanded=False):
            flows.append(random_user_flow(target_url, number_of_actions))