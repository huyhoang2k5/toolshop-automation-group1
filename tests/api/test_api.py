
import pytest


@pytest.mark.api
def test_api_01_status_returns_toolshop(api):
    """Verify Toolshop API status and JSON response."""

    # Send GET request
    response = api.get("/status")

    # Verify HTTP status
    assert response.status == 200, response.text()

    # Verify JSON response
    data = response.json()

    assert isinstance(data, dict)
    assert data["app_name"] == "Toolshop"


@pytest.mark.api
def test_api_02_products_returns_valid_json(api):
    """Verify product list API response structure."""

    response = api.get("/products")

    assert response.status == 200, response.text()

    data = response.json()

    assert isinstance(data, dict)
    assert "data" in data
    assert isinstance(data["data"], list)
    assert len(data["data"]) > 0

    product = data["data"][0]

    assert "id" in product
    assert "name" in product
    assert "price" in product



@pytest.mark.api
def test_api_03_users_me_without_token_returns_401(api):
    """Verify protected endpoint rejects unauthenticated requests."""

    response = api.get("/users/me")

    assert response.status == 401, response.text()




@pytest.mark.api
def test_api_04_users_me_with_token_returns_profile(
    api, auth_headers, test_user
):
    """Verify authenticated user can access their profile."""

    response = api.get(
        "/users/me",
        headers=auth_headers
    )

    assert response.status == 200, response.text()

    data = response.json()

    assert isinstance(data, dict)
    assert data["email"] == test_user["email"]




@pytest.mark.api
def test_api_05_create_cart_returns_201(api):
    """Verify POST /carts creates a new cart."""

    response = api.post("/carts")

    assert response.status == 201, response.text()

    data = response.json()

    assert isinstance(data, dict)
    assert "id" in data
    assert isinstance(data["id"], str)
    assert data["id"]
