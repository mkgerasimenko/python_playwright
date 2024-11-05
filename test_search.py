import allure
from playwright.sync_api import Page
from models.search_page import SearchPage


@allure.title("Test Google Search")
@allure.description("This test attempts to search different words in the first result")
@allure.tag("Search")
@allure.severity(allure.severity_level.MINOR)
def test_successful_search(page: Page, base_url):
    searched_criteria = "Playwright"
    google_page = SearchPage(page)
    google_page.navigate(base_url).accept_cookies().search(searched_criteria)

    assert (
        searched_criteria in google_page.get_first_result().inner_text()
    ), "The first result does not contain {0}".format(searched_criteria)
