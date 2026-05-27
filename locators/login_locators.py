from  appium.webdriver.common.appiumby import AppiumBy

class LoginLocators:

    USERNAME = (AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().text("e.g. john.doe@company.com")'
    )

    CONTINUE_BTN = (AppiumBy.ACCESSIBILITY_ID,
                    'Continue'
    )

    PASSWORD = (AppiumBy.XPATH,
                '//android.widget.EditText[@text="••••••••"]'
    )

    SIGN_IN_BTN = (AppiumBy.XPATH,
                   '//android.view.ViewGroup[@content-desc="Sign in"]'
    )

    HOME_PAGE = (AppiumBy.ANDROID_UIAUTOMATOR,
                 'new UiSelector().text("Home")'
    )