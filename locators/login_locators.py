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

    INVALID_USER_MAIL = (AppiumBy.ANDROID_UIAUTOMATOR,
                         'new UiSelector().text("Please enter a valid email address")'
    )

    EMPTY_USER_MAIL = (AppiumBy.ANDROID_UIAUTOMATOR,
                       'new UiSelector().text("Please enter your work email")'
    )

    INVALID_PASSWORD = (AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Invalid email or password")'
    )
    
    EMPTY_PASSWORD = (AppiumBy.ANDROID_UIAUTOMATOR,
                      'new UiSelector().text("Please enter your password")'
    )
    
    LOGIN_BACK = (AppiumBy.ANDROID_UIAUTOMATOR,
                  'new UiSelector().text("← Back")'
    )

    WELCOME_PAGE = (AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("Welcome to HRMS")'
    )

    LOGIN_PAGE = (AppiumBy.ANDROID_UIAUTOMATOR,
                  'new UiSelector().text("Welcome back")'
    )