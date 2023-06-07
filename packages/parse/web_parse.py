import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

def browser_init(bank_buster):
    option = Options()
    option.add_argument("--disable-infobars") 
    option.add_argument("--ignore-certificate-errors")
    option.add_argument("--ignore-ssl-errors")
    option.add_argument("--ignore-certificate-errors-spki-list")
    option.add_argument("disable-blink-features=AutomationControlled");
    option.add_experimental_option("excludeSwitches", ["enable-automation"])
    option.add_experimental_option('useAutomationExtension', False)
    #option.add_experimental_option( "prefs",{'profile.managed_default_content_settings.javascript': 2}) #Disables JavaScript
    browser = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=option)

    main(bank_buster,browser)



def main(bank_buster,browser):
    #Последовательность массива [contractnumber, clientid, inn, fio, ordercode, fedresurs date, arbitr date]
    for index, row in bank_buster.iterrows():
        #Делаем из каждой строки массив и отсылаем в ссылку ИНН[2], остальные значения нужны для формирования файла банкротства
        bank_buster_list = bank_buster.loc[index, :].values.flatten().tolist()
        try:
            # #Открываем страницу федресурса по ИНН и ждем загрузки клиента
            browser.get('https://fedresurs.ru/search/entity?code=' + str(bank_buster_list[2]))
            time.sleep(3)
            shit = browser.find_element(By.CLASS_NAME, 'td_company_name')
            shit.send_keys(Keys.RETURN)

            #Закрываем предыдущую страницу и переходим на новую
            browser.close()
            window_after = browser.window_handles[0]
            browser.switch_to.window(window_after)
            
            #Открываем страницу клиента и ждем загрузки приказов. Тут стоит except если приказа нет, то выносит клиента в отдельный файл
            try:
                time.sleep(5)
                browser.find_element(By.XPATH, '//a[contains(@href,"bankruptreport")]').click()
                browser.close()
                window_after = browser.window_handles[0]
                browser.switch_to.window(window_after)
                
            #Если отчет о банкротстве не найден, то ищется номер приказа по сообщению о банкротстве  
            except NoSuchElementException:
                print('INFO: bankruptreport not found')
                bankname = browser.find_elements(By.XPATH, "//div[@class='info']//span[contains(text(),'Дела о банкротстве')]")
                if bankname:
                    #Разворачивает дроп-меню чтобы получить номер приказа
                    browser.find_element(By.XPATH, "//a/span").click()
                    time.sleep(3)
                    order = browser.find_element(By.XPATH, "//table[@class='info_table bankrot_case']/tbody/tr/td[1]/p").text
                    bank_buster_list.insert(4,str(order))
                else:
                    print('ERROR: Order not found on client in fedresurs: ' + str(bank_buster_list))
                    pass
            #Переключаемся на страницу приказа и ищем дату окончания
            time.sleep(3)
            try:
                order = browser.find_element(By.CLASS_NAME, 'date__content').get_attribute("textContent")
                orderfed = browser.find_element(By.XPATH, "//span[@class='caseNumber']").text
                browser.close()
                window_after = browser.window_handles[0]
                browser.switch_to.window(window_after)
                bank_buster_list.insert(4,str(order))
            except NoSuchElementException:
                print('ERROR: Order date not found on client in fedresurs: ' + str(bank_buster_list))
                pass
            #Открываем страницу федресурса по ИНН и ждем загрузки клиента
            browser.get('https://kad.arbitr.ru/')
            time.sleep(3)
            if bank_buster_list[4]:
                print('bruh')
                textarea = browser.find_element(By.XPATH, '//input[@id="*"][3]')
                textarea.send_keys(str(bank_buster_list[4]), Keys.ENTER)
                time.sleep(3)
                orderarb = browser.find_element(By.XPATH, "//a[@class='num_case']").text
                time.sleep(10)
            if orderarb in orderfed:
                browser.find_element(By.XPATH, '//a[contains(@href,"Card")]').click()
                time.sleep(5)
                browser.close()
                window_after = browser.window_handles[0]
                browser.switch_to.window(window_after)
                fullname = browser.find_element(By.XPATH, "//h2[@class='b-case-result']//a[@target='_blank']").text
                subname = "Завершить реализацию имущества гражданина"
                if subname in fullname:
                    bankdate = browser.find_element(By.XPATH, "//span[@class='b-reg-date']").text
                    bank_buster_list.append(str(bankdate))
                else:
                    print('ERROR: Order not found on client in arbitr: ' + str(bank_buster_list))
                    pass
            else:
                print('ERROR: Order not found on client in arbitr: ' + str(bank_buster_list))
                pass
            #Записываем дату приказа в файл и закрываем страницу
            df = pd.DataFrame(bank_buster_list).transpose()
            df.to_csv('input/bankparsedinfo.csv', index = False, mode = 'a', sep='*', header= False)
            window_after = browser.window_handles[0]
            browser.switch_to.window(window_after)
            time.sleep(3)
        except NoSuchElementException:
            print('ERROR: Order not found on client: ' + str(bank_buster_list))
            pass
            #browser.close()
    browser.close()
    browser.quit()
    print('INFO: Done | File generated at input/bankparsedinfo.csv')