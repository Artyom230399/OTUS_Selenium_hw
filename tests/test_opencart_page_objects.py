from page_objects.HomePage import HomePage


def test_search_DesktopButton(browser):
    HomePage.search_button_desktops(browser)
