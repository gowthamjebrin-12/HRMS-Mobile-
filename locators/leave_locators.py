from  appium.webdriver.common.appiumby import AppiumBy

class LeaveLocators:

    LEAVE_PAGE_NAV = (AppiumBy.ANDROID_UIAUTOMATOR, 
                      'new UiSelector().text("Leaves")')
    
    APPLY_LEAVE_BTN = (AppiumBy.ANDROID_UIAUTOMATOR,
                       'new UiSelector().text("+ Apply")')
    
    LEAVE_DROPDOWN = (AppiumBy.ANDROID_UIAUTOMATOR,
                      'new UiSelector().className("com.horcrux.svg.SvgView").instance(1)')
    
    OPTION = (AppiumBy.ANDROID_UIAUTOMATOR,
              'new UiSelector().text("")')
    
    DATE_FIELD =  (AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("com.horcrux.svg.RectView").instance({})')

    START_DATE = (AppiumBy.ACCESSIBILITY_ID,
                   '07 May 2026')
    
    END_DATE = (AppiumBy.ACCESSIBILITY_ID,
                 '08 May 2026')
    
    OK_BTN = (AppiumBy.ID,
              'android:id/button1')
    
    REASON_INPUT = (AppiumBy.CLASS_NAME,
                    'android.widget.EditText')
    
    SUBMIT_BTN = (AppiumBy.ANDROID_UIAUTOMATOR,
                  'new UiSelector().text("Submit Application")')
    
    def Option(text):
        return (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{text}")')
    
    