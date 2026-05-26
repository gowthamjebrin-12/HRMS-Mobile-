from  appium.webdriver.common.appiumby import AppiumBy

class LogoutLocators:

    SIDE_BAR = (AppiumBy.ANDROID_UIAUTOMATOR,
                 'new UiSelector().className("com.horcrux.svg.SvgView").instance(0)'
    )

    # OPEN_MENU = (AppiumBy.CLASS_NAME,
    #              'com.horcrux.svg.SvgView'
    # )


    LOGOUT_BTN = (AppiumBy.ANDROID_UIAUTOMATOR,
                  'new UiSelector().text("LOGOUT")'
    )
    

    CONFIRM_LOGOUT = (AppiumBy.ACCESSIBILITY_ID,
                      'Logout'
    )