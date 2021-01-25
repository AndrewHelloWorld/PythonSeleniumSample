#!/usr/bin/python3
"""
@File    : home_page.py
@Time    : 2019/11/29 21:38
@Author  : 柠檬班-小简
@Email   : lemonban_simple@qq.com
@Company: 湖南省零檬信息技术有限公司
"""

from Common.basepage import BasePage
from PageLocators.home_page_loc import HomePageLoc as loc


class HomePage(BasePage):

    # 检测 退出元素 是否存在。
    def check_loginbutton_exist(self):
        return self.check_element_visible(loc.login_name,"首页_检测退出元素是否存在")

    # 点击login button，进入login page。
    def click_login_button(self):
        self.click_element(loc.login_button,"首页_点击login按钮")
        self.click_element(loc.login_Popup_button, "login pop up 转换用户名密码登录")
        # self.click_element(loc.login_Popup_name, "首页_点击login按钮")