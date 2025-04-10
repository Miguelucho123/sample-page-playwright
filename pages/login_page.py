from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator('input[name="UserName"]')
        self.password_input = page.locator('input[name="Password"]')
        self.login_logout_button = page.locator('#login')
        self.message = page.locator('#loginstatus')

    def navigate(self):
        self.page.goto("http://uitestingplayground.com/sampleapp")

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_logout_button.click()

    def logout(self):
        self.login_logout_button.click()

    def get_message(self) -> str:
        return self.message.text_content().strip()
