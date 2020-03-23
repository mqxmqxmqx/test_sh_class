import os, sys
sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.display_page import DisplayPage

# 做什么  (流程修改)
class TestDisplay:
    def setup(self):
        # 连接手机
        self.driver = init_driver()
        # 创建page对象  把driver传给page对象
        self.display_page = DisplayPage(self.driver)

    def test_display_input(self):
        # 点击显示
        # self.display_page.click_display()
        # 点击放大镜
        self.display_page.click_search()
        # 输入文字(传什么由脚本决定)
        self.display_page.input_search_text("1")
        # 点击返回
        self.display_page.click_back()

    # self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()
    # self.driver.find_element_by_id("com.android.settings:id/search").click()
    # self.driver.find_element_by_id("android:id/search_src_text").send_keys("hello")
    # self.driver.find_element_by_class_name("android.widget.ImageButton").click()

    def teardown(self):
        self.driver.quit()
