from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def enter_text(self, locator, text):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    def get_text(self, locator):
        return WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(locator)
        ).text
    
    def is_visible(self, locator):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(locator)
            ).is_displayed()
            return True
        except:
            return False
    
    def scroll_down(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                'new UiScrollable(new UiSelector().scrollable(true)).scrollForward()'
    )
        
    def scroll_up(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                'new UiScrollable(new UiSelector().scrollable(true)).scrollBackward()'
    )
        
    def click_dynamic(self, locator, value):
        by, path = locator
        dynamic_locator = (by, path.format(value))
        self.click(dynamic_locator)

    
    def click_by_index(self, locator, index):

        elements = WebDriverWait(self.driver, 20).until(
            lambda d: d.find_elements(*locator)
        )

        elements[index].click()

    def is_displayed(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
            )
            return True
        except:
            return False

    def get_attribute(self, locator, attribute):
        element = self.driver.find_element(*locator)
        return element.get_attribute(attribute)
    
    def clear_text(self, locator):
        element = self.driver.find_element(*locator)
        element.clear()

    def is_enabled(self, locator):
        element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(locator)
        )
        return element.is_enabled()