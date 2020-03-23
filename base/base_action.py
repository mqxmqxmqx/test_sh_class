from selenium.webdriver.support.wait import WebDriverWait

# 将动作进行封装(重复利用的东西)(根据page特征去找,点,操作)
class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def click(self, loc):
        self.find_element(loc).click()

    # 给谁输入  输入什么
    def input_text(self, loc, text):
        self.find_element(loc).send_keys(text)

    def find_element(self, loc):
        by = loc[0]
        value = loc[1]
        return WebDriverWait(self.driver, 5, 1).until(lambda x: x.find_element(by, value))

    def find_elements(self, loc):
        by = loc[0]
        value = loc[1]
        return WebDriverWait(self.driver, 5, 1).until(lambda x: x.find_elements(by, value))
