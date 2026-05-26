from  appium.webdriver.common.appiumby import AppiumBy

class ResetPasswordLocators:

    OPEN_MENU = (AppiumBy.ACCESSIBILITY_ID, 'Open menu')

    RESET_NAV = (AppiumBy.ANDROID_UIAUTOMATOR,
                 'new UiSelector().text("Reset Password")')
    
    CURRENT_PASSWORD = (AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Enter current password")')
    
    NEW_PASSWORD = (AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("Enter new password")')
    
    CONFIRM_PASSWORD = (AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Re-enter new password")')
    
    UPDATE_BTN = (AppiumBy.ANDROID_UIAUTOMATOR,
                  'new UiSelector().text("Update Password")')
    
    OK_BTN =  (AppiumBy.ID,'android:id/button1')