from io import StringIO
import streamlit as st
from bs4 import BeautifulSoup
import requests
import os
import openai
from openai import OpenAI
import sys
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

import chromedriver_autoinstaller

st.header("Generate Selenium code from User Flow")
st.write("We generate navigational Selenium code. We do this by using GPT-4 as our reasoning LLM.")

def scrape_html (url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    #all_elements = soup.find_all(True)  # Find all elements
    return soup

def generate_selenium_code_from_user_log(log_data, target_url):
    testLines = log_data.split('\n')

    all_nodes = []
    all_urls = []
    for x in testLines:
        node, fullUrl = x.split('\t')
        node = node[6:]
        fullUrl = fullUrl[10:]
        all_nodes.append(node)
        all_urls.append(fullUrl)
        print(node, fullUrl)
    start_node = target_url + all_urls[0]

    client = OpenAI(
        # This is the default and can be omitted
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    for url in all_urls:
        dest = url.split('/')[-1]
        html_code = scrape_html(start_node)
        prompt = """Task: Given HTML code for a web page, please provide a few Selenium code lines
        that would allow us to click on the button that goes to the page that we will specify. Only output text without
        adding any indication that it is a python code such as quotes or "python".
        Provide only the relevent lines of code without any additional explanations.

        Examples without HTML being provided:

        1. "How can I get to /men page?"
        Answer:
        shopMen = driver.find_element(by=By.XPATH, value="//span[normalize-space()='Shop men']")
        shopMen.click()

        2. "How can I get to /hacked-fashion-chuck-taylor-all-star-85 page?"
        Answer:
        hackyShoes = driver.find_element(by=By.XPATH, value="//span[normalize-space()='Hacked fashion chuck taylor all star']")
        hackyShoes.click()

        3. "How can I get to /hacked-fashion-chuck-taylor-all-star-85?size=26 page?"
        Answer:
        sizeSelect = driver.find_element(by=By.XPATH, value="//a[normalize-space()='XL']")
        sizeSelect.click()

        4. "How can I get to /hacked-fashion-chuck-taylor-all-star-85?size=26&color=8 page?"
        Answer:
        colorSelect = driver.find_element(by=By.XPATH, value="//a[normalize-space()='Blue']")
        colorSelect.click()


        5. "How can I get to /cart page?"
        Answer:
        addToCart = driver.find_element(by=By.XPATH, value="//button[@type='button']")
        addToCart.click()

        If you ever encounter a mandatory field on the html, you have to provide the Selenium code that writes something in those fields.
        More specifically, you will encounter those on the cart page when trying to get to the /checkout page. If asked how to get to '/checkout' page,
        you should provide the answer EXACTLY as written in example 6.

        6. "How can I get to /checkout page?"
        Answer:

        viewCart = driver.find_element(by=By.XPATH, value="//a[normalize-space()='VIEW CART (1)']")
        viewCart.click()

        checkOut = driver.find_element(by=By.XPATH, value="//span[normalize-space()='CHECKOUT']")
        checkOut.click()

        emailBox = driver.find_element(by=By.XPATH, value="//input[@placeholder='Email']")
        emailBox.send_keys("KombuAITest@PearHack.com")

        continueToShipping = driver.find_element(by=By.XPATH, value="//span[normalize-space()='Continue to shipping']")
        continueToShipping.click()

        fullName = driver.find_element(by=By.XPATH, value="//input[@placeholder='Full name']")
        phone = driver.find_element(by=By.XPATH, value="//input[@placeholder='Telephone']")
        address = driver.find_element(by=By.XPATH, value="//input[@placeholder='Address']")
        city = driver.find_element(by=By.XPATH, value="//input[@placeholder='City']")
        country = driver.find_element(by=By.XPATH, value="//select[contains(@id,'address')]")
        postcode = driver.find_element(by=By.XPATH, value="//input[@placeholder='Postcode']")

        fullName.send_keys("AiTest")
        phone.send_keys("AiTest")
        address.send_keys("AiTest")
        city.send_keys("San Francisco")
        postcode.send_keys("94107")

        select = Select(country)
        select.select_by_visible_text('United States')

        province = driver.find_element(by=By.XPATH, value="(//select[@id='address[province]'])[1]")
        selectProvince = Select(province)
        selectProvince.select_by_visible_text('California')

        shipping = driver.find_element(by=By.XPATH, value="//span[normalize-space()='Standard Delivery - $5.00']")
        shipping.click()

        toPayment = driver.find_element(by=By.XPATH, value="//span[normalize-space()='Continue to payment']")
        toPayment.click()

        cashOnDelivery = driver.find_element(by=By.XPATH, value="//div[@class='checkout-payment checkout-step']//div//div[1]//div[1]//div[1]//div[1]//div[1]//a[1]//*[name()='svg']")
        cashOnDelivery.click()

        placeOrder = driver.find_element(by=By.XPATH, value="//span[normalize-space()='Place Order']")
        placeOrder.click()


        Based on these examples and based on the provided HTML code, please answer the following prompt:
        How can I get to /{}?
        Here is the HTML: {}
        """.format(dest, html_code.prettify())
        def get_response(prompt):
            stream = client.chat.completions.create(
                model="gpt-4-turbo",
                messages=[{"role": "user", "content": prompt}],
                stream=True,
            )
            for chunk in stream:
                content = chunk.choices[0].delta.content
                if chunk:
                    yield content or ""

        selenium_codelines = []
        
        st.write_stream(get_response(prompt) if not None else "")
        start_node = target_url + url

file_uploader = st.file_uploader("Upload user flow to automate")
target_url = st.text_input("Enter URL to Scrape")
button = st.button("Generate Selenium code from User Flow")
if button:
    if file_uploader is not None:
        stringio = StringIO(file_uploader.getvalue().decode("utf-8"))
        
        # To read file as string:
        string_data = stringio.read()
        generate_selenium_code_from_user_log(string_data, target_url)