from  appium.webdriver.common.appiumby import AppiumBy

class LeaveLocators:

    LEAVE_PAGE_NAV = (AppiumBy.ANDROID_UIAUTOMATOR, 
                      'new UiSelector().text("Leaves")')
    
    APPLY_LEAVE_BTN = (AppiumBy.ANDROID_UIAUTOMATOR,
                       'new UiSelector().text("+ Apply")')
    
    LEAVE_DROPDOWN = (AppiumBy.ANDROID_UIAUTOMATOR,
                      'new UiSelector().className("com.horcrux.svg.SvgView").instance(1)')
    
    EARNED_LEAVE = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("*").instance(1)')

    CASUAL_LEAVE = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Tap to pick date").instance(1)')
        
    DATE_FIELD =  (AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("com.horcrux.svg.RectView").instance({})')

    START_DATE = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("7")')
    
    END_DATE = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("8")')
    
    OK_BTN = (AppiumBy.ID,'android:id/button1')
    
    REASON_INPUT = (AppiumBy.CLASS_NAME,
                    'android.widget.EditText')
    
    SUBMIT_BTN = (AppiumBy.ANDROID_UIAUTOMATOR,
                  'new UiSelector().text("Submit Application")')
    
    LEAVE_PAGE = (AppiumBy.ANDROID_UIAUTOMATOR,
                  'new UiSelector().text("Leave history").instance(0)'
    )
    

    
    