from pages.sidebar_nav.sidebar_nav import SidebarNav

def test_sidebar_navigation(driver):
    
    sidebar_nav_page = SidebarNav(driver)
    sidebar_nav_page.sidebar_navigation()

    print("Sidebar navigation successful")