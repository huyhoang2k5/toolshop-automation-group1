
import re
import pytest
from playwright.sync_api import expect
from pages.cart_page import CartPage
from pages.product_page import ProductPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.contact_page import ContactPage

@pytest.mark.ui
@pytest.mark.regression
def test_ui_07_product_detail_displays_information(page, base_url):
    """Verify product detail page displays essential information."""

    page.goto(base_url)

    # Open the first product from the homepage
    first_product = page.get_by_test_id("product-name").first
    expect(first_product).to_be_visible()

    product_name = first_product.inner_text().strip()
    first_product.click()

    # Verify product details
    product = ProductPage(page)

    expect(product.name).to_be_visible()
    expect(product.name).to_have_text(product_name)

    expect(product.unit_price).to_be_visible()
    expect(product.quantity).to_be_visible()
    expect(product.add_to_cart_button).to_be_visible()

    # Verify quantity can be edited
    expect(product.quantity).to_be_editable()




@pytest.mark.ui
@pytest.mark.regression
def test_ui_08_product_quantity_can_be_changed(page, base_url):
    """Verify product quantity can be changed."""

    page.goto(base_url)

    # Open the first product
    first_product = page.get_by_test_id("product-name").first
    expect(first_product).to_be_visible()
    first_product.click()

    product = ProductPage(page)

    # Verify quantity input is available
    expect(product.quantity).to_be_visible()
    expect(product.quantity).to_be_editable()

    # Change quantity
    product.quantity.fill("3")

    # Verify updated value
    expect(product.quantity).to_have_value("3")





@pytest.mark.ui
@pytest.mark.regression
def test_ui_09_cart_total_matches_line_prices(page, base_url):
    """Verify cart total equals the sum of line prices."""

    page.goto(base_url)

    # Open first product
    first_product = page.get_by_test_id("product-name").first
    expect(first_product).to_be_visible()
    first_product.click()

    product = ProductPage(page)

    # Add one product to cart
    expect(product.add_to_cart_button).to_be_visible()
    

    
    product.add_to_cart()

    # Wait until the cart is updated before navigating
    cart_quantity = page.get_by_test_id("cart-quantity")
    expect(cart_quantity).to_have_text("1", timeout=10000)

    # Open cart
    cart = CartPage(page)
    cart.open()




    # Wait for cart data to appear
    expect(cart.product_titles.first).to_be_visible()
    expect(cart.total).to_be_visible()

    # Compare displayed total with sum of line prices
    line_totals = cart.line_totals()
    actual_total = cart.total_value()

    assert len(line_totals) > 0
    assert round(sum(line_totals), 2) == round(actual_total, 2), (
        f"Expected {sum(line_totals):.2f}, "
        f"got {actual_total:.2f}"
    )




@pytest.mark.ui
@pytest.mark.regression
def test_ui_10_sort_products_by_price_ascending(page, base_url):
    """Verify products are sorted by price from low to high."""

    home = HomePage(page)
    home.open()

    # Wait for initial products to appear
    expect(home.product_names.first).to_be_visible()

    # Sort by price ascending
    home.sort_by("price,asc")

    # Wait for the sorting request to complete
    expect(home.sort_select).to_have_value("price,asc")
    expect(home.sorting_completed).to_be_visible()

    # Read displayed prices
    prices = home.prices()

    # Verify sorting
    assert len(prices) >= 2, "Not enough products to verify sorting"

    assert prices == sorted(prices), (
        f"Products are not sorted by ascending price: {prices}"
    )





@pytest.mark.ui
@pytest.mark.regression
def test_ui_11_login_successfully(page, test_user):
    """Verify a registered user can log in successfully."""

    # Open login page
    login = LoginPage(page).open()

    # Verify login form
    expect(login.email).to_be_visible()
    expect(login.password).to_be_visible()
    expect(login.submit_button).to_be_visible()

    # Login using the test account created by API
    login.login(
        test_user["email"],
        test_user["password"]
    )

    # Verify successful navigation to account page
    expect(page).to_have_url(
        re.compile(r"/account$")
    )

    # Verify login form is no longer displayed
    expect(login.submit_button).not_to_be_visible()





@pytest.mark.ui
@pytest.mark.regression
def test_ui_12_contact_invalid_email(page):
    """Verify contact form rejects an invalid email."""

    contact = ContactPage(page).open()

    # Enter an invalid email address
    contact.first_name.fill("Test")
    contact.last_name.fill("User")
    contact.email.fill("invalid-email")

    # Submit the form
    contact.submit()

    # Verify email validation error
    email_error = page.get_by_test_id("email-error")
    expect(email_error).to_be_visible()
    expect(email_error).to_contain_text("Email")

    # Verify the user remains on the contact page
    expect(page).to_have_url(re.compile(r"/contact$"))
