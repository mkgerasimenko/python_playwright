import allure
from playwright.sync_api import Page
from models.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    @allure.step("Accept cookies")
    def accept_cookies(self):
        self.page.get_by_role("button", name="Accept all").click()
        return self

    @allure.step("Get first search result")
    def get_first_result(self):
        selector = "h3"
        self.page.wait_for_selector(selector)
        return self.page.locator(selector).first

    @allure.step("Search {1}")
    def search(self, phrase: str):
        search_box = self.page.get_by_label("Search", exact=True)
        search_box.click()
        search_box.fill(phrase)
        search_box.press("Enter")
        return self
