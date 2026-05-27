from appium.webdriver.common.appiumby import AppiumBy

class PunchInOutLocators:

    PUNCH_IN_BTN = (AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("Punch In")'
    )

    PUNCH_IN_DONE = (AppiumBy.ANDROID_UIAUTOMATOR,
                   'new UiSelector().text("Clocked In")'
    )


    PUNCH_OUT_BTN = (AppiumBy.ANDROID_UIAUTOMATOR,
                     'new UiSelector().text("Punch Out")'
    )

    PUNCH_OUT_DONE = (AppiumBy.ANDROID_UIAUTOMATOR,
                      'new UiSelector().text("Shift ended")'
    ) 