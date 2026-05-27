import os
from dotenv import load_dotenv
from appium import webdriver
from appium.options.android import UiAutomator2Options

load_dotenv()

def before_scenario(context, scenario):
    
    options = UiAutomator2Options()

    options.platform_name = os.getenv("PLATFORM_NAME")
    options.device_name = os.getenv("DEVICE_NAME")
    options.automation_name = os.getenv("AUTOMATION_NAME")

    options.app_package = os.getenv("APP_PACKAGE")
    options.app_activity = os.getenv("APP_ACTIVITY")

    options.no_reset = True

    context.driver = webdriver.Remote(
        "http://127.0.0.1:4723",
         options=options
    )

    context.username = os.getenv("EMP_USERNAME")
    context.password = os.getenv("EMP_PASSWORD")

def after_scenario(context, scenario):

    if hasattr(context, 'driver'):
        context.driver.quit()
