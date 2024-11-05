import allure
from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Navigate to {1}")
    def navigate(self, url):
        self.page.goto(url, timeout=5000)
        return self
