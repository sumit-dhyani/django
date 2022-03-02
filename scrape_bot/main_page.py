
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import os
# it is working currently scraping the employee information first upto 5 pages
#now scrapping experience and education details.
# IT will only count till 5 pages as it has become very slow

class scrapping:
    def __init__(self,url):
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')
        self.driver=webdriver.Chrome(executable_path='C:/Selenium/chromedriver.exe')
        self.driver.get(url)
        self.url=url
        self.count=0
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        try:
            emp=self.driver.find_element(By.XPATH,"//a[contains(@class,'face-pile__cta')]").get_attribute('href')
            self.driver.get(emp)
            self.count=1
        except:
            print("will be opened later")
    def sign_in(self):

        # As due to many tests my ip was flagged and 
        # i am getting different login page now than the one which was working before
        
        try:
            self.driver.find_element(By.XPATH,"//a[contains(@class,'main__sign-in-link')]").click()
            self.driver.find_element(By.XPATH,"//input[contains(@id,'username')]").send_keys(7983138711)
            self.driver.find_element(By.XPATH,"//input[contains(@id,'password')]").send_keys('Korebi@321')
            self.driver.find_element(By.XPATH,"//button[contains(@class,'btn__primary--large from__button--floating')]").click()
        except:

            self.driver.find_element(By.XPATH,"//button[contains(@class,'authwall-join-form__form-toggle--bottom form-toggle')]").click()
            self.driver.find_element(By.XPATH,"//input[contains(@id,'session_key')]").send_keys(7983138711)
            self.driver.find_element(By.XPATH,"//input[contains(@id,'session_password')]").send_keys('Korebi@321')
            self.driver.find_element(By.XPATH,"//button[contains(@class,'sign-in-form__submit-button')]").click()

    def emp_overview(self):
        # self.names=[]
        name=[]
        bio=[]
        city=[]
        url=[]
        if self.count==1:
            print("no need to open again ")
        else:
            self.driver.get(self.url)
            emp=self.driver.find_element(By.XPATH,"//div[contains(@class,'display-flex mt2 mb1')]/a").get_attribute('href') 
            self.driver.get(emp) # this will open the employee list page
        # pagination=self.driver.find_elements(By.XPATH,"//li[contains(@class,'artdeco-pagination__indicator artdeco-pagination__indicator--number ember-view')]/button/span")
        # Pages_count=int(pagination[len(pagination)-1].text) # this will count total number of pages
        # There is a count variable above which gets the number of pages and loop that many times
        # i am limiting it to 5 for now as due to many tests my Ip was blocked by linked in once
        # also it has become very slow too
        for i in range(1,6):
            blocks=self.driver.find_elements(By.XPATH,"//li[contains(@class,'reusable-search__result-container')]")
            for b in blocks:
                try:
                    n=b.find_element(By.XPATH,".//span[contains(@dir,'ltr')]/span[contains(@aria-hidden,'true')]").text
                    name.append(n)
                except:
                    n="Linked In Member. Profile not visible"
                    name.append(n)
                s=b.find_element(By.XPATH,".//div[contains(@class,'t-black t-normal')]").text
                bio.append(s)
                c=b.find_element(By.XPATH,".//div[contains(@class,'t-14 t-normal')]").text
                city.append(c)
                u=b.find_element(By.XPATH,".//span[contains(@class,'t-16')]/a").get_attribute('href')
                url.append(u)
                if u=="https://www.linkedin.com/search/results/people/headless?currentCompany=%5B10369067%5D&origin=COMPANY_PAGE_CANNED_SEARCH" or u=="https://www.linkedin.com/search/results/people/headless?currentCompany=%5B10369067%5D&origin=OTHER":
                    print("profile not accessible")
                else:
                    self.education(n,u)
            self.driver.find_element(By.XPATH,"//button[contains(@aria-label,'Next')]").click()
            
        
        df=pd.DataFrame({'Name':name,'User url':url,'bio':bio,'Location':city})
        df.to_csv("C:/Users/Acer/OneDrive/Desktop/Linked In/New folder/output.csv",index=False) 
        
        self.driver.close()

    def education(self,name,url):
        driver=self.driver
        driver.get(url)
        driver.implicitly_wait(10)
        college_name=[]
        course=[]  #It is taking some time due to many tests on linked in 
        start=[]
        end=[]
        description=[]
        # name=driver.find_element(By.XPATH,"//main/section[1]/div[2]/div[2]/div[1]/div/h1").text
       
        for d in driver.find_elements(By.XPATH,"//main/section[5]/div[3]/ul/li"):
            college_name.append(d.find_element(By.XPATH,".//span[contains(@class,'t-bold mr1')]/span[1]").text)
            try:
                course.append(d.find_element(By.XPATH,".//a[contains(@class,'flex-column full-width')]/span[1]/span[1]").text)
            except:
                course.append("")
            try:
                    duration=d.find_element(By.XPATH,".//a[contains(@class,'flex-column full-width')]/span[2]/span[1]").text.split('-')
                    start.append(duration[0])
                    end.append(duration[1])
            except:
                start.append("")
                end.append("")
            try:
                description.append(d.find_element(By.XPATH,".//div[contains(@class,'pv-shared-text-with-see-more t-14 t-normal t-black display-flex align-items-center')]/div/span[1]").text)
            except:
                description.append("")
        df=pd.DataFrame({'college':college_name,'course':course,'start':start,'end':end,'description':description})
        path_s='C:/Users/Acer/OneDrive/Desktop/Linked In/New folder/'+name
        try:
            os.mkdir(path_s)# To make the directory with the name of employee
        except:
            print("path is already created")
        path_s+='/education.csv'
        df.to_csv(path_s,index=False)
        self.experience(name)
        driver.back()
        

    # This will extract information about experience
    def experience(self,name):
        position=[]
        company=[]
        duration=[]
        location=[]
        company_link=[]

        for d in self.driver.find_elements(By.XPATH,"//main/section[4]/div[3]/ul/li"):
                try:
                    position.append(d.find_element(By.XPATH,".//span[contains(@class,'t-bold mr1')]/span[1]").text)
                except:
                    position.append("")
                # Here i have used try except with every statement as sometimes there is no data which will cause errors
                try:
                    company.append(d.find_element(By.XPATH,".//div[contains(@class,'display-flex flex-column full-width')]/span[1]/span[1]").text)
                except:
                    company.append("")
                try:
                    duration.append(d.find_element(By.XPATH,".//div[contains(@class,'display-flex flex-column full-width')]/span[2]/span[1]").text)
                except:
                    duration.append("")
                try:
                    location.append(d.find_element(By.XPATH,".//div[contains(@class,'display-flex flex-column full-width')]/span[3]/span[1]").text)
                except:
                    location.append("")
                company_link.append(d.find_element(By.XPATH,".//a[contains(@data-field,'experience_company_logo')]").get_attribute('href'))
        df=pd.DataFrame({'Position':position,'Company':company,'duration':duration,'location':location,'company_link':company_link })
        path_s='C:/Users/Acer/OneDrive/Desktop/Linked In/New folder/'+name
        # os.mkdir(path_s)
        path_s+='/experience.csv'
        df.to_csv(path_s,index=False)