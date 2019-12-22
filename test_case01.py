# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

import allure
import pytest
from appium import webdriver

class TestXueqiu:
    @pytest.fixture(scope="function")
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "mumu"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = True

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

        yield
        sleep(5)
        self.driver.quit()


    @allure.feature('test_xueqiu_module1')
    @allure.story('test_xueqiu_login')
    # test_xueqiu_login
    def test_xueqiu(self,setup):
        """
        对雪球app的登录界面进行测试
        """
        el1 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.ImageView")
        el1.click()
