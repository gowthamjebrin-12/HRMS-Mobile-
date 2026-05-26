from appium import webdriver
from appium.options.android import UiAutomator2Options

from utils.config import Config

class DriverFactory:

    @staticmethod
    def get_driver():

        options = UiAutomator2Options()

        options.platform_name = Config.PLATFORM_NAME
        options.device_name = Config.DEVICE_NAME
        options.automation_name = Config.AUTOMATION_NAME
        options.app_package = Config.APP_PACKAGE
        options.app_activity = Config.APP_ACTIVITY
        options.no_reset = True

        driver = webdriver.Remote(
            Config.APPIUM_URL,
            options=options
        )

        driver.implicitly_wait(10)
        return driver