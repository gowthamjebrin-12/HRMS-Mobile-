from appium.webdriver.common.appiumby import AppiumBy

class SidebarNavLocators:

    ICON = (AppiumBy.CLASS_NAME,
                    'com.horcrux.svg.SvgView'
    )

    PROFILE_SIDEBAR = (AppiumBy.ANDROID_UIAUTOMATOR,
                       'new UiSelector().description("Profile")'
    )

    OVERALL_POLICIES_SIDEBAR =(AppiumBy.ACCESSIBILITY_ID,
                               'Overall Policies'
    )

    # BACK_BTN = (AppiumBy.CLASS_NAME,
    #             'com.horcrux.svg.PathView'
    # )

    LEAVE_SIDEBAR = (AppiumBy.ACCESSIBILITY_ID,
                     'Leave'
    )

    HOME_PAGE = (AppiumBy.ANDROID_UIAUTOMATOR,
                 'new UiSelector().text("Home")'
    )

    ATTENDANCE_SIDEBAR = (AppiumBy.ACCESSIBILITY_ID,
                          'Attendance'
    )

    CALENDAR_SIDEBAR = (AppiumBy.ACCESSIBILITY_ID,
                        'Calendar'
    )

    # BACK_BTN = (AppiumBy.XPATH,
                        #  '//android.widget.Button[@content-desc="Go back"]/com.horcrux.svg.SvgView'
    # )

    RESET_PASSWORD_SIDEBAR = (AppiumBy.ACCESSIBILITY_ID,
                              'Reset Password'
    )

    CLOSE_BTN = (AppiumBy.CLASS_NAME,
                 'com.horcrux.svg.GroupView'
    )
