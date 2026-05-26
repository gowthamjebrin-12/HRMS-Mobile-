import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")

    APPIUM_URL = os.getenv("APPIUM_URL")

    PLATFORM_NAME = os.getenv("PLATFORM_NAME")
    DEVICE_NAME = os.getenv("DEVICE_NAME")
    AUTOMATION_NAME = os.getenv("AUTOMATION_NAME")

    APP_PACKAGE = os.getenv("APP_PACKAGE")
    APP_ACTIVITY = os.getenv("APP_ACTIVITY")

    CURRENT_PASSWORD = os.getenv("CURRENT_PASSWORD")
    NEW_PASSWORD = os.getenv("NEW_PASSWORD")