import json
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
def login(user,passw,driver):
    #


    driver.find_element_by_id('username').clear()
    driver.find_element_by_id('username').send_keys(user)
    driver.find_element_by_id('password').clear()
    driver.find_element_by_id('password').send_keys(passw)
    driver.find_element_by_id('login-submit').click()
    time.sleep(3)

def send_information(zy,ss,driver):

    driver.find_element_by_id('V1_CTRL40').clear()
    driver.find_element_by_id('V1_CTRL40').send_keys(zy)
    #driver.find_element_by_id('V1_CTRL41').clear()
    opt = driver.find_element_by_id('V1_CTRL41')
    Select(opt).select_by_value('9')
    opt = driver.find_element_by_id('V1_CTRL42')
    Select(opt).select_by_value('1')
    opt = driver.find_element_by_id('V1_CTRL7')
    Select(opt).select_by_value('12')

    driver.find_element_by_id('V1_CTRL8').clear()
    driver.find_element_by_id('V1_CTRL8').send_keys(ss)

def seventeen_point():
    driver = init_driver()
    init_job(driver)
    driver.find_element_by_id('V1_CTRL23').click()  # 17点
    do_job(driver)
def eleven_point():
    driver = init_driver()
    init_job(driver)
    driver.find_element_by_id('V1_CTRL19').click()  # 11点
    do_job(driver)
def seven_point():
    driver = init_driver()
    zy, ss = init_job(driver)
    send_information(zy, ss,driver)
    driver.find_element_by_id('V1_CTRL28').click()  # 7点
    do_job(driver)
def twentyone_point():

    driver=init_driver()
    init_job(driver)
    do_job(driver)
def init_driver():
    chrome_opts = webdriver.ChromeOptions()
    chrome_opts.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_opts)
    driver.get('https://ehall.jlu.edu.cn/infoplus/form/YJSMRDK/start')

    return driver
def init_job(driver):

    f = open('information.txt', encoding='utf-8')
    content = f.read()  # 使用loads（）方法需要先读文件
    user_dic = json.loads(content)
    username = user_dic['username']
    password = user_dic['password']
    print(user_dic)
    login(username, password,driver)
    zz = user_dic['major']
    ss = user_dic['dornum']

    return zz,ss
def do_job(driver):
    driver.find_element_by_id('V1_CTRL44').click()  # V1_CTRL44  博士
    time.sleep(3)
    driver.find_element_by_xpath("//a[contains(@id, 'infoplus_action')]").click()
    time.sleep(2)
    driver.find_element_by_xpath("//button[contains(@class, 'default')]").click()
    time.sleep(2)
    driver.quit()
if __name__ == '__main__':
    seven_point()
    # time.sleep(3)
    # driver.find_element_by_xpath("//a[contains(@id, 'infoplus_action')]").click()
    # #driver.find_element_by_xpath('//button[@class="dialog_button default fr"]').click()  # send space
    # #driver.find_element_by_class_name('dialog_button default fr').click()
    # time.sleep(2)
    # driver.find_element_by_xpath("//button[contains(@class, 'default')]").click()