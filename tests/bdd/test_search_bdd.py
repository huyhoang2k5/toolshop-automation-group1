import pytest
from playwright.sync_api import expect
from pytest_bdd import scenarios, given, when, then, parsers

from pages.home_page import HomePage


pytestmark = [pytest.mark.bdd, pytest.mark.ui]

scenarios("search.feature")


@pytest.fixture
def home(page):
    return HomePage(page)


@given("I am on the Toolshop home page")
def open_home(home):
    home.open()


@when(parsers.parse('I search for "{keyword}"'))
def search_product(home, keyword):
    home.search(keyword)


@then(parsers.parse('all displayed product names should contain "{keyword}"'))
def verify_search_results(home, keyword):
    expect(home.search_completed).to_be_attached()
    expect(home.product_names.first).to_be_visible()

    names = home.product_names.all_inner_texts()
    assert names, "Search should return at least one product"
    assert all(keyword.lower() in name.lower() for name in names)
