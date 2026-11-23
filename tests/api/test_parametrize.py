import json
from pathlib import Path
import pytest


@pytest.mark.api
@pytest.mark.parametrize(
    "endpoint",
    [
        "/users/me",
        "/users/999999",
    ],
)
def test_parametrize_01_unauthorized_requests(api, endpoint):
    """Verify protected endpoints reject unauthenticated requests."""

    response = api.get(endpoint)

    assert response.status == 401, (
        f"{endpoint}: expected 401, got "
        f"{response.status}. Body: {response.text()}"
    )




# Load test cases from JSON file
DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "api_cases.json"

with DATA_FILE.open(encoding="utf-8") as file:
    API_CASES = json.load(file)


@pytest.mark.api
@pytest.mark.parametrize(
    "case",
    API_CASES,
    ids=[case["name"] for case in API_CASES],
)
def test_parametrize_02_api_cases_from_json(api, case):
    """Verify API status codes using JSON test data."""

    response = api.get(case["endpoint"])

    assert response.status == case["expected_status"], (
        f"{case['name']}: expected {case['expected_status']}, "
        f"got {response.status}. Body: {response.text()}"
    )
