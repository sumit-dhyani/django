from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


driver=webdriver.Firefox(executable_path='C:/Selenium/geckodriver.exe')

driver.get("https://www.linkedin.com/in/parthnigam?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAABoVEFABQqP9R6-h0QiX_CoSLSmdlmyEvY0")
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//button[contains(@class,'authwall-join-form__form-toggle--bottom form-toggle')]").click()

driver.find_element(By.XPATH,"//input[contains(@id,'session_key')]").send_keys(7983138711)
driver.find_element(By.XPATH,"//input[contains(@id,'session_password')]").send_keys('Korebi@321')
driver.find_element(By.XPATH,"//button[contains(@class,'sign-in-form__submit-button')]").click()
driver.get("https://www.linkedin.com/in/parthnigam?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAABoVEFABQqP9R6-h0QiX_CoSLSmdlmyEvY0")

experience=driver.find_elements(By.XPATH,"//section[contains(@id,'ember409')]//li[contains(@class,'pvs-list__item--one-column')]")
for ex in experience:
            name=ex.find_element(By.XPATH,"//span[contains(@aria-hidden,'true'")
            print(name)
# class emp_details:
#      def __init__(self,url):
#         # chrome_options = webdriver.ChromeOptions()
#         # chrome_options.add_argument('--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')
#         self.driver=webdriver.Chrome(executable_path='C:/Selenium/chromedriver.exe')
#         self.driver.get(url)
#         self.url=url
#         self.driver.implicitly_wait(5)

#     def process(self,name):
#         driver=self.driver
#         experience=driver.find_elements(By.XPATH,"//section[contains(@id,'ember409')]//li[contains(@class,'pvs-list__item--one-column')]")
#         for ex in experience:
#             name=ex.find_element(By.XPATH,"//span[contains(@aria-hidden,'true'")
#             print(name)