from pages.base_page import BasePage
from locators.sidebar_nav_locators import SidebarNavLocators

class SidebarNav(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def sidebar_navigation(self):

        self.click(SidebarNavLocators.ICON)
        self.click(SidebarNavLocators.PROFILE_SIDEBAR)

        self.click(SidebarNavLocators.ICON)
        self.click(SidebarNavLocators.OVERALL_POLICIES_SIDEBAR)
        self.go_back()

        self.click(SidebarNavLocators.ICON)
        self.click(SidebarNavLocators.LEAVE_SIDEBAR)
        self.click(SidebarNavLocators.HOME_PAGE)

        self.click(SidebarNavLocators.ICON)
        self.click(SidebarNavLocators.ATTENDANCE_SIDEBAR)
        self.click(SidebarNavLocators.HOME_PAGE)


        self.click(SidebarNavLocators.ICON)
        self.click(SidebarNavLocators.CALENDAR_SIDEBAR)
        self.go_back()

        self.click(SidebarNavLocators.ICON)
        self.click(SidebarNavLocators.RESET_PASSWORD_SIDEBAR)
        self.click(SidebarNavLocators.CLOSE_BTN)



