# 页面基类，主要封装每个页面都可能会使用到的方法
class BasePage:
    def __init__(self,driver):  # 重写构造方法，初始化浏览器对象
        self.driver = driver

    # 封装元素定位方法
    def find_element(self,*ele):
        return self.driver.find_element(*ele)

    # 封装定位一组元素的方法
    def find_elements(self,*ele):
        return self.driver.find_elements(*ele)

    #封装表单切换方法
    def switch_frame(self,*ele):
        self.driver.switch_to.frame(self.find_element(*ele))

    def switch_back(self):
        self.driver.switch_to.default_content()
    # 封装获取页面标题的方法
    def get_title(self):
        return self.driver.title

    # 封装获取页面url的方法
    def get_url(self):
        return self.driver.current_url

    # 封装截图方法
    def get_image(self,igname):
        self.driver.get_screenshot_as_file(igname)
