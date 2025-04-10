import pytest
from pages.login_page import LoginPage
from utils.logger import logger
#author: Miguel Gutierrez
@pytest.mark.parametrize("username,password,expected", [
    ("TestUser", "pwd", "Welcome, TestUser"),           # Login successful
    ("TestUser", "wrongpwd", "Invalid username/password"), # password incorrect
    ("", "", "Invalid username/password"),              # empty username and password
    ("TestUser", "", "Invalid username/password"),      # only username
    ("", "pwd", "Invalid username/password")            # only password
])
def test_login_scenarios(page, username, password, expected):
    login_page = LoginPage(page)

    logger.info("the user open the testing background page")
    login_page.navigate()

    logger.info(f" the user login with '{username}' and '{password}'")
    login_page.login(username, password)

    actual_message = login_page.get_message()
    logger.info(f"Login status: '{actual_message}'")

    try:
        assert actual_message == expected, f"Expected: '{expected}' but was: '{actual_message}'"
        logger.info("Assertion passed")
    except AssertionError as e:
        screenshot_path = f"screenshots/fail_{username or 'empty'}_{password or 'empty'}.png"
        page.screenshot(path=screenshot_path)
        logger.error(f"Assertion failed, screenshots attached: {screenshot_path}")
        raise e


    if expected.startswith("Welcome"):
        logger.info("Logout After Successful Login")
        login_page.logout()
        logout_message = login_page.get_message()
        try:
            assert logout_message == "User logged out."
            logger.info("Logout Successful")
        except AssertionError as e:
            screenshot_path = f"screenshots/logout_fail_{username or 'empty'}.png"
            page.screenshot(path=screenshot_path)
            logger.error(f"Assertion failed, screenshots attached: {screenshot_path}")
            raise e
