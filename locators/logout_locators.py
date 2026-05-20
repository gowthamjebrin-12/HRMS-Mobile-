from  appium.webdriver.common.appiumby import AppiumBy

class LogoutLocators:

    SIDE_BAR = (AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("com.horcrux.svg.SvgView").instance(0)'
    )

    LOGOUT_BTN = (AppiumBy.ACCESSIBILITY_ID,
                  'LOGOUT'
    )

    CONFIRM_LOGOUT = (AppiumBy.ACCESSIBILITY_ID,
                      'Logout'
    )