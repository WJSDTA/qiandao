import json
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
def login(user,passw):
    driver.find_element_by_id('username').clear()
    driver.find_element_by_id('username').send_keys(user)
    driver.find_element_by_id('password').clear()
    driver.find_element_by_id('password').send_keys(passw)
    driver.find_element_by_id('login-submit').click()
    time.sleep(3)

def send_information(zy,ss):

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
    driver.find_element_by_id('V1_CTRL23').click()  # 17点
def eleven_point():
    driver.find_element_by_id('V1_CTRL19').click()  # 11点
def seven_point(zy,ss):
    send_information(zy, ss)
    driver.find_element_by_id('V1_CTRL28').click()  # 7点
if __name__ == '__main__':
    driver = webdriver.Chrome()

    # 记得写完整的url 包括http和https
    driver.get('https://ehall.jlu.edu.cn/infoplus/form/YJSMRDK/start')
    f = open('information.txt', encoding='utf-8')
    content = f.read()  # 使用loads（）方法需要先读文件
    user_dic = json.loads(content)
    username = user_dic['username']
    password = user_dic['password']
    if driver.find_element_by_id("username"):
        login(username, password)

    zz=user_dic['major']
    ss=user_dic['dornum']
    driver.find_element_by_id('V1_CTRL44').click()  # V1_CTRL44  博士

    #eleven_point()
    time.sleep(5)
    driver.find_element_by_xpath("//a[contains(@id, 'infoplus_action')]").click()
    #driver.find_element_by_xpath('//button[@class="dialog_button default fr"]').click()  # send space
    #driver.find_element_by_class_name('dialog_button default fr').click()
    time.sleep(2)
    driver.find_element_by_xpath("//button[contains(@class, 'default')]").click()
    time.sleep(2)
    driver.quit()