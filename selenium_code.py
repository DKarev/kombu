from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

import chromedriver_autoinstaller

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless') # ensure GUI is off
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# set path to chromedriver as per your configuration
chromedriver_autoinstaller.install()

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://demo.evershop.io/")

homeButton = driver.find_element(by=By.XPATH, value="//a[@class='logo-icon']")

homeButton.click()

menLink = driver.find_element(by=By.XPATH, value="//a[@href='/men']")

menLink.click()

nikeReactPhantom = driver.find_element(by=By.XPATH, value="//span[normalize-space()='Nike react phantom run flyknit 2']")
nikeReactPhantom.click()

sizeSelect = driver.find_element(by=By.XPATH, value="//a[normalize-space()='X']")
sizeSelect.click()

colorSelect = driver.find_element(by=By.XPATH, value="//a[normalize-space()='Green']")
colorSelect.click()

miniCart = driver.find_element(by=By.XPATH, value="//a[@class='mini-cart-icon']")
miniCart.click()

homeButton = driver.find_element(by=By.XPATH, value="//a[@class='logo-icon']")
homeButton.click()

shopWomen = driver.find_element(by=By.XPATH, value="//a[normalize-space()='Women']")
shopWomen.click()

alphaedgeShoes = driver.find_element(by=By.XPATH, value="//a[@href='/women/alphaedge-4d-reflective-shoes-23']")
alphaedgeShoes.click()

sizeSelect = driver.find_element(by=By.XPATH, value="//a[normalize-space()='XL']")
sizeSelect.click()

colorSelect = driver.find_element(by=By.XPATH, value="//a[normalize-space()='White']")
colorSelect.click()

addToCart = driver.find_element(by=By.XPATH, value="//a[@class='mini-cart-icon']")
addToCart.click()

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