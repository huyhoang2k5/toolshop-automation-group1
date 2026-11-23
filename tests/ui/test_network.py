
import re

import pytest
from playwright.sync_api import expect


@pytest.mark.ui
def test_network_01_empty_products_shows_no_results(page, base_url):
    """Verify UI handles an empty product list."""

    empty_response = {
        "current_page": 1,
        "data": [],
        "from": None,
        "last_page": 1,
        "per_page": 9,
        "to": None,
        "total": 0,
    }

    intercepted = []

    def mock_products(route):
        intercepted.append(route.request.url)
        route.fulfill(
            status=200,
            content_type="application/json",
            json=empty_response,
        )

    # Mock product-list requests before navigating
    page.route(re.compile(r"/products(\?.*)?$"), mock_products)

    # Open Toolshop homepage
    page.goto(base_url)

    # Verify mocked response is reflected in the UI
    expect(
        page.get_by_text("There are no products found.")
    ).to_be_visible()

    expect(page.get_by_test_id("product-name")).to_have_count(0)

    # Ensure the API request was actually intercepted
    assert len(intercepted) > 0




@pytest.mark.ui
def test_network_02_product_api_error_keeps_page_usable(page, base_url):
    """Verify homepage remains usable when product API fails."""

    intercepted = []

    def mock_server_error(route):
        intercepted.append(route.request.url)
        route.fulfill(
            status=500,
            content_type="application/json",
            json={"message": "Internal Server Error"},
        )

    # Mock API failure before navigation
    page.route(re.compile(r"/products(\?.*)?$"), mock_server_error)

    # Open homepage
    page.goto(base_url)

    # Verify no products are displayed
    expect(page.get_by_test_id("product-name")).to_have_count(0)

    # Verify search input remains usable
    search_input = page.get_by_test_id("search-query")

    expect(search_input).to_be_visible()
    expect(search_input).to_be_editable()

    search_input.fill("hammer")
    expect(search_input).to_have_value("hammer")

    # Verify request was intercepted
    assert len(intercepted) > 0
