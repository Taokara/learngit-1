# from selenium import webdriver
#
# op_google=webdriver.Chrome()
#
#
#
#
#
# op_google.get("https://www.baidu.com")
# op_google.find_element_by_css_selector('.s_ipt').send_keys("刘德华")
#
# op_google.find_element_by_id('su').click()
                                             #通过id找到按钮并输入点击
#
# li_class=op_google.find_elements_by_class_name('bg')
#                #这里用了elements，找到的就算列表，用element只会找到第一个
# print(li_class)
# for i in li_class:
#     if i.get_attribute('value')=="百度一下":
#         i.click()
#                             # 通过class粗筛，再通过属性找到按钮并输入点击
#

# li1=op_google.find_elements_by_css_selector('div>p')
# #div下一级中的p标签
# li2=op_google.find_elements_by_css_selector('div+p')
# #紧连在div下的一个p标签
# li3=op_google.find_elements_by_css_selector('div[hight*="50"]+p')
# #[]内是该标签属性，*表示包含





# op_google.get("http://localhost:63342/learngit-1/test7.html?_ijt=ikj0eutvlnbl54lvp7vhcpq8m5")
# a=op_google.find_element_by_css_selector('div>p')
# print(a.text)
# li=op_google.find_elements_by_css_selector('div>p')
# for i in li:
#     print(i.text)



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep
# from selenium.webdriver.support.select import Select
#
# op_google = webdriver.Chrome()
# op_google.get("http://192.168.1.41/ecshop/admin/privilege.php?act=login")
#
# username = (By.NAME,"username")
# password = (By.NAME,"password")
# submit = (By.CSS_SELECTOR,"input[value=进入管理中心]")
# try:
#     op_google.find_element(*username).send_keys("admin")
#     op_google.find_element(*password).send_keys("admin123456")
#     op_google.find_element(*submit).click()
#     op_google.switch_to.frame("header-frame")
#     op_google.find_element(By.CSS_SELECTOR,"#submenu-div > ul > li:nth-child(7) > a").click()
#     op_google.switch_to.parent_frame()
#     op_google.switch_to.frame("main-frame")
#     op_google.find_element(By.CSS_SELECTOR, "#all_menu_list > option:nth-child(6)").click()
#     op_google.find_element(By.CSS_SELECTOR, "#btnAdd").click()
#     select1 = op_google.find_element(By.ID, "menus_navlist")
#     select2 = Select(select1)  # 这一步是把定位传入下拉框
#     select2.select_by_visible_text("商品品牌")
#     for i in range(len(select2.options)-1):
#         op_google.find_element(By.CSS_SELECTOR, "#btnMoveUp").click()
# except Exception:
#     raise
# finally:
#     sleep(3)
#     op_google.quit()


# 装饰器



#
# def addfunc(func):
#     def infunc(*args, **kwargs):
#         func_result = func(*args, **kwargs)
#         infunc_result= func_result*func_result
#         return infunc_result
#     return infunc
#
# @addfunc
# def func(a,b):
#     c = a + b
#     return c
#
# print(func(3, 5))

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select



op_google = webdriver.Chrome()
op_google.get("http://192.168.1.41/ecshop/admin/privilege.php?act=login")



username = (By.NAME,"username")
password = (By.NAME,"password")
submit = (By.CSS_SELECTOR,"input[value=进入管理中心]")
try:
    op_google.find_element(*username).send_keys("admin")
    op_google.find_element(*password).send_keys("admin123456")
    op_google.find_element(*submit).click()
    op_google.switch_to.frame("menu-frame")
    op_google.find_element(By.CSS_SELECTOR,".collapse.lis.ico_1").click()
    op_google.find_element(By.LINK_TEXT,"商品列表").click()
    op_google.switch_to.parent_frame()
    op_google.switch_to.frame("main-frame")
    def goods(a):
        i = str(a+3)
        loc1 = "//*[@id='listDiv']/table[1]/tbody/tr[" + i + "]/td[2]/span"
        test = op_google.find_element_by_xpath(loc1).text
               # loc1是字符串，带入变量就自动含有“ ”了，不用说在拼接的时候加上
        return test
    paper = int(op_google.find_element(By.ID, "pageSize").get_attribute("value"))
    for a in range(paper):
        if goods(a) == "毛貂毛边卫衣套装":
            op_google.find_element(By.CSS_SELECTOR,
"#listDiv > table:nth-child(1) > tbody > tr:nth-child(4) > "
"td:nth-child(1) > input[type=checkbox]").click()
            break

except Exception:
    raise
finally:
    op_google.save_screenshot("../1.png")
    sleep(2)
    op_google.quit()
