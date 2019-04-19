#from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
import wget


driver = webdriver.Chrome(executable_path='chromedriver.exe')
save_Video_Location = 'E:/Users/Jun/Desktop/'
Current_ep = '0'
Episode_Index = 0
last_Episode = 0
delay = 5
starting_EP = 0




class Wait_For_Next_Page(object):
    def __call__(self, driver):
        try:
            return Current_ep != driver.find_elements_by_class_name('selectEpisode').text
        except StaleElementReferenceException:
            return False


def ClickEPLink(epnum=0):
    global Episode_Index
    global last_Episode

    # get all element
    list_of_Ele = driver.find_elements_by_class_name('episodeSub')

    # due to number are retrieved backward, we need to do some math
    Episode_Index = len(list_of_Ele) - epnum

    last_Episode = len(list_of_Ele)

    # click on the episode
    list_of_Ele[Episode_Index].find_element_by_tag_name('a').click()

    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'selectServer')))


def ChangeServer():
    select = Select(driver.find_element_by_id('selectServer'))

    # select by visible text
    openLoad_link = select.select_by_visible_text('Openload').get_attribute("value")
    driver.get(openLoad_link)
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'centerDivVideo')))
    # select by value
    # select.select_by_value('1')


def main():
    global starting_EP
    global Current_ep
    global Episode_Index
    global Current_ep
    # url = 'http://kissasian.ch/'
    url = 'http://kissasian.ch/Drama/While-You-Were-Sleeping'
    # urllib.request.urlopen( req )
    # req = requests.get(url, headers={'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"})
    # r = req.raise_for_status()

    # soup = BeautifulSoup(r.read(),"html.parser")

    # print (soup.prettify()[0:1000])

    # get to the site and wait for page to load
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//table[@class='listing']")))

    try:
        if starting_EP == 1:
            starting_EP = 0

        ClickEPLink(starting_EP)

        Current_ep = driver.find_elements_by_class_name('selectEpisode').text

        while Episode_Index != 0:
            # Change Server to openload
            ChangeServer()

            # download video  wget.download(mp4_address,out="path/to/output/file")
            # get video srcstarting_EP
            mp4_address = driver.find_elements_by_tag_name('video').get_attribute('src')

            # save video
            wget.download(mp4_address, out=save_Video_Location + 'while ' + Current_ep)

            # next Ep
            # get the current ep
            Current_ep = driver.find_elements_by_class_name('selectEpisode').text

            # get btnNext and click the parent link
            WebDriverWait(driver.find_element_by_id('btnNext').find_element_by_xpath('..').click(), 3).until(
                Wait_For_Next_Page())
            Episode_Index -= 1

    except TimeoutException:
        print("Loading took too much time!")
    finally:
        driver.close()

if __name__== "__main__":
    main()