import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service



chrome_driver = r"C:\Users\ARJUN RAHUL VIJI\OneDrive\Documents\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(service= Service(chrome_driver))

driver.get("http://orteil.dashnet.org/experiments/cookie/")


cookie = driver.find_element(By.ID, 'cookie')
possibilities = []
differences = []
# game = True
#
tCurrent = time.time()
t = 0
while True:
    cookie.click()

    if time.time() >= tCurrent + 1:
        tCurrent = time.time()
        t += 1
        if t%5 == 0:
            my_cookies = driver.find_element(By.ID, 'money')
            nos = '0123456789'
            shops = driver.find_elements(By.CSS_SELECTOR, '#store b')
            for i in shops:
                di = ''
                for x in i.text:
                    if x in nos:
                        di += x
                    else:
                        continue
                try:
                    di = int(di)
                except ValueError:
                    continue
                possibilities.append(di)
            my_cookies = driver.find_element(By.ID, 'money')
            bitch = ''
            for i in my_cookies.text:
                if i in nos:
                    bitch += i
            money = int(bitch)
            for i in possibilities:
                differences.append(abs(money - i))
            correct = differences.index(min(differences))
            shops[correct].click()
            possibilities.clear()
            differences.clear()



