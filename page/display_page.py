from selenium.webdriver.common.by import By
from base.base_action import BaseAction

# 怎么做的(页面的内容修改,找特征)
class DisplayPage(BaseAction):
    # 显示按钮
    display_button = By.XPATH, "//*[contains(@text,'显示')]"
    # 放大镜
    search_button = By.ID, "com.android.settings:id/search"
    # 输入文本框
    search_edit_text = By.ID, "android:id/search_src_text"
    # 返回按钮
    back_button = By.CLASS_NAME, "android.widget.ImageButton"

    # 创建对象的时候传进来
    def __init__(self, driver):
        BaseAction.__init__(self, driver)
        # self.driver = driver
        # 点击显示(init 里面可以去写已经确定的这个模块所有的前置功能)
        self.click_display()
    # 方法具体实现
    def click_display(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()
        # self.driver.find_element(self.display_button).click()
        # self.find_element(self.display_button).click()
        self.click(self.display_button)

    def click_search(self):
        # self.driver.find_element_by_id("com.android.settings:id/search").click()
        # self.find_element(self.search_button).click()
        self.click(self.search_button)

    def input_search_text(self, text):
        # self.driver.find_element_by_id("android:id/search_src_text").send_keys(text)
        # self.find_element(self.search_edit_text).send_keys(text)
        self.input_text(self.search_edit_text, text)

    def click_text_view(self):
        # self.find_element(self.search_edit_text).click()
        self.click(self.search_edit_text)

    def click_back(self):
        # self.driver.find_element_by_class_name("android.widget.ImageButton").click()
        # self.find_element(self.back_button).click()
        self.click(self.back_button)
