from  appium.webdriver.common.appiumby import AppiumBy

class ResetPasswordLocators:

    MENU_SIDEBAR = (AppiumBy.CLASS_NAME,
                    'com.horcrux.svg.SvgView'
    )

    RESET_PASS_SIDEBAR = (AppiumBy.ACCESSIBILITY_ID,
                          'Reset Password'
    )

    CURRENT_PASSWORD = (AppiumBy.ACCESSIBILITY_ID,
                          'Enter current password')
    
    NEW_PASSWORD = (AppiumBy.ACCESSIBILITY_ID,
                      'Enter new password'
    )

    CONFIRM_PASSWORD = (AppiumBy.ACCESSIBILITY_ID,
                          'Re-enter new password'
    )

    UPDATE_BTN = (AppiumBy.ACCESSIBILITY_ID,
                  'Update Password'
    )

    CONFIRMATION_MSG = (AppiumBy.ID,
                        'android:id/button1'
    )