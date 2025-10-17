import pytest
from app import app

@pytest.fixture
def client():
    """Create a Flask test client for simulating HTTP requests."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# ---------- Basic Page Tests ----------
def test_homepage(client):
    """Home page should return 200 OK."""
    response = client.get("/")
    assert response.status_code == 200


def test_cart_page(client):
    """Cart page should return 200 OK."""
    response = client.get("/cart")
    assert response.status_code == 200


def test_account_page(client):
    """Account page should return 200 OK or redirect if login required."""
    response = client.get("/account")
    assert response.status_code in (200, 302)


# ---------- POST Request Tests ----------
def test_add_to_cart_post(client):
    """POST to add-to-cart should return success or redirect."""
    response = client.post("/add-to-cart", data={"book_id": 1})
    assert response.status_code in (200, 302)


def test_login_post(client):
    """POST to login should respond correctly."""
    response = client.post("/login", data={"username": "user", "password": "123"})
    assert response.status_code in (200, 302)


def test_register_post(client):
    """POST to register should return success or redirect."""
    response = client.post("/register", data={"username": "new", "password": "123"})
    assert response.status_code in (200, 302)
