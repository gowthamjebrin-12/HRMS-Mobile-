from  appium.webdriver.common.appiumby import AppiumBy

class AttendanceLocators:

    ATTENDANCE_NAV_BAR = (AppiumBy.ACCESSIBILITY_ID,
                          'Attendance'
    )

    APPLY_BTN = (AppiumBy.ANDROID_UIAUTOMATOR,
                 'new UiSelector().text("+ Apply")'
    )

    START_DATE = (AppiumBy.ANDROID_UIAUTOMATOR,
                  'new UiSelector().className("com.horcrux.svg.RectView").instance(0)'
    )

    SELECT_START_DATE = (AppiumBy.ACCESSIBILITY_ID,
                         '01 June 2026'
    )
    
    END_DATE = (AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("com.horcrux.svg.RectView").instance(1)'
    )

    SELECT_END_DATE = (AppiumBy.ACCESSIBILITY_ID,
                       '01 June 2026'
    )

    OK_BTN = (AppiumBy.ID,
                'android:id/button1'
    )

    START_TIME = (AppiumBy.ANDROID_UIAUTOMATOR,
                   'new UiSelector().className("com.horcrux.svg.CircleView").instance(0)'
    )

    CHECK_IN_TIME = (AppiumBy.ACCESSIBILITY_ID,
                     '9'
    )
    
    CHECK_IN_MINS = (AppiumBy.ACCESSIBILITY_ID,
                     '30'
    )

    END_TIME = (AppiumBy.ANDROID_UIAUTOMATOR,
                 'new UiSelector().className("com.horcrux.svg.CircleView").instance(1)'
    )

    CHECK_OUT_TIME = (AppiumBy.ACCESSIBILITY_ID,
                      '18'  
    )

    CHECK_OUT_MINS = (AppiumBy.ACCESSIBILITY_ID,
                      '0'
    )

    DESCRIPTION_FIELD = (AppiumBy.ANDROID_UIAUTOMATOR,
                         'new UiSelector().text("Describe the task or activity...")'
    )

    SUBMIT_BTN = (AppiumBy.ACCESSIBILITY_ID,
                 'Apply'
    )

    ATTENDANCE_PAGE = (AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().text("Attendance").instance(0)'
    )

    ATTENDANCE_HISTORY_PAGE = (AppiumBy.ANDROID_UIAUTOMATOR,
                               'new UiSelector().text("Attendance History")'
    )    
    
    REQUEST_PENDING = (AppiumBy.ANDROID_UIAUTOMATOR,
                       'new UiSelector().text("PENDING").instance(0)'
    )

    END_DATE_EARLIER_THAN_START_DATE = (AppiumBy.ACCESSIBILITY_ID,
                         '02 June 2026'
    )

    INVALID_DATE = (AppiumBy.ACCESSIBILITY_ID,
                    'Invalid Date Range'
    )

    INVALID_TIME = (AppiumBy.ACCESSIBILITY_ID,
                    'Invalid Time Range'
    )
    
    END_TIME__EARLIER_THAN_START_TIME = (AppiumBy.ANDROID_UIAUTOMATOR,
                   'new UiSelector().className("com.horcrux.svg.CircleView").instance(0)'
    )

    ALERT_MESSAGE = (AppiumBy.ID,
                     'com.hrmsmobile:id/alertTitle')
    
    CHECK_IN_EARLY_TIME = (AppiumBy.ACCESSIBILITY_ID,
                     '18'
    )

    CHECK_IN_EARLY_MINS = (AppiumBy.ACCESSIBILITY_ID,
                     '0'
    )

    CHECK_OUT_EARLY_TIME = (AppiumBy.ACCESSIBILITY_ID,
                      '9'  
    )

    CHECK_OUT_EARLY_MINS = (AppiumBy.ACCESSIBILITY_ID,
                      '0'
    )

