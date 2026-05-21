from appium.webdriver.common.appiumby import AppiumBy

class PunchInOutLocators:

    PUNCH_IN_BTN = (AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("Punch In")'
    )

    PUNCH_OUT_BTN = (AppiumBy.ANDROID_UIAUTOMATOR,
                     'new UiSelector().text("Punch Out")'
    )

    