from  appium.webdriver.common.appiumby import AppiumBy

class PermissionLocators:
    
    # PERMISSION PAGE - ADD PERMISSION

    LEAVE_NAV_BAR = (AppiumBy.ANDROID_UIAUTOMATOR,
                     'new UiSelector().text("Leaves")'
    )

    PERMISSION_NAV_PAGE = (AppiumBy.ANDROID_UIAUTOMATOR,
                           'new UiSelector().text("Permissions")'
    )

    APPLY_BTN = (AppiumBy.ANDROID_UIAUTOMATOR,
                 'new UiSelector().text("+ Apply")'
    )

    DATE_PICKER = (AppiumBy.ANDROID_UIAUTOMATOR,
                   'new UiSelector().className("com.horcrux.svg.SvgView").instance(1)'
    )

    SELECT_PERMISSION_DATE = (AppiumBy.ACCESSIBILITY_ID,
                              '07 May 2026'
    )

    CLICK_OK_BTN = (AppiumBy.ID,
                    'android:id/button1'
    )

    STARTING_FROM = (AppiumBy.ANDROID_UIAUTOMATOR,
                     'new UiSelector().text("e.g. Chennai Office")'
    )

    DESTINATION = (AppiumBy.ANDROID_UIAUTOMATOR,
                   'new UiSelector().text("e.g. Client Site")'
    )

    START_TIME_PICKER = (AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("com.horcrux.svg.CircleView").instance(0)'
    )

    SELECT_HOUR = (AppiumBy.ACCESSIBILITY_ID,'4')
    SELECT_MINS = (AppiumBy.ACCESSIBILITY_ID,'30')

    END_TIME_PICKER = (AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("com.horcrux.svg.CircleView").instance(1)'
    )

    SELECT_END_HOUR = (AppiumBy.ACCESSIBILITY_ID,'6')
    SELECT_END_MINS = (AppiumBy.ACCESSIBILITY_ID,'0')

    MARK_ATTENDANCE = (AppiumBy.ANDROID_UIAUTOMATOR,
                       'new UiSelector().text("Yes")'
    )

    COMMENT = (AppiumBy.ANDROID_UIAUTOMATOR,
               'new UiSelector().text("Brief reason...")'
    )

    SUBMIT_BTN = (AppiumBy.ANDROID_UIAUTOMATOR,
                  'new UiSelector().text("Submit Application")'
    )

    PERMISSION_PAGE = (AppiumBy.ACCESSIBILITY_ID,
                       'Permissions'
    )

