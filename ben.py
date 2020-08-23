import json
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()

# 记得写完整的url 包括http和https
#driver.get('https://ehall.jlu.edu.cn/Fx_redirected%25253Dtrue%252526scope%25253Dprofile%25252Bprofile_edit%25252Bapp%25252Btask%25252Bprocess%25252Bsubmit%25252Bprocess_edit%25252Bsys_triple%25252Btriple%25252Bsys_profile%25252Btriple%25252Bsys_triple_edit%25252Bsys_app%25252Bstats%25252Bsys_stats%252526response_type%25253Dcode%252526redirect_uri%25253Dhttps%2525253A%2525252F%2525252Fehall.jlu.edu.cn%2525252Fjlu_portal%2525252Fwall%2525252Fendpoint%2525253FretUrl%2525253Dhttps%252525253A%252525252F%252525252Fehall.jlu.edu.cn%252525252Fjlu_portal%252525252Flogin%252526client_id%25253D679e3d8a-a8b9-424e-859a-7e25ac760a74%26state%3D396f15%26client_id%3DbwDBpMCWbid5RFcljQRP#/')
driver.get('https://ehall.jlu.edu.cn/jlu_portal/login')
def login(user,passw):
    driver.find_element_by_id('username').clear()
    driver.find_element_by_id('username').send_keys(user)
    driver.find_element_by_id('password').clear()
    driver.find_element_by_id('password').send_keys(passw)
    driver.find_element_by_id('login-submit').click()
    time.sleep(3)
login("zhangchuang2117","zc21172406")