
import pytest
from playwright.sync_api import expect

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.contact_page import ContactPage


@pytest.mark.smoke
def test_smoke_search_pliers(page):
    """Goal: Search for pliers.
    Precondition: Home page is accessible.
    Expected: All displayed products contain 'pliers'.
    """
    home = HomePage(page).open()
    home.search("pliers")

    expect(home.search_completed).to_be_attached()
    expect(home.product_names.first).to_be_visible()

    names = home.product_names.all_inner_texts()
    assert names, "Search should return at least one product"
    assert all("pliers" in name.lower() for name in names)


@pytest.mark.smoke
def test_smoke_add_three_claw_hammers(page):
    """Goal: Add three Claw Hammers to the cart.
    Precondition: Cart is empty and home page is accessible.
    Expected: Cart badge displays quantity 3.
    """
    home = HomePage(page).open()
    product = home.open_product("Claw Hammer")
    product.add_to_cart(quantity=3)

    cart_badge = page.get_by_test_id("cart-quantity")
    expect(cart_badge).to_have_text("3")


@pytest.mark.smoke
def test_smoke_invalid_login(page):
    """Goal: Log in using a nonexistent account.
    Precondition: Login page is accessible.
    Expected: Error is displayed and login page remains open.
    """
    login = LoginPage(page).open()
    login.login("nonexistent-sprint1@example.com", "WrongPassword123!")

    expect(login.error).to_contain_text("Invalid email or password")
    expect(page).to_have_url(
        "https://practicesoftwaretesting.com/auth/login"
    )


@pytest.mark.smoke
def test_smoke_empty_contact_form(page):
    """Goal: Submit an empty contact form.
    Precondition: Contact page is accessible.
    Expected: Subject and message validation errors are displayed.
    """
    contact = ContactPage(page).open()
    contact.submit()

    expect(contact.errors).to_contain_text(
        ["First name is required", "Last name is required",
         "Email is required", "Subject is required",
         "Message is required"]
    )
