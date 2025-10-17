import pytest
from models import Book, CartItem


# ---------- Test Book Class ----------
def test_book_creation():
    """Check that Book object initializes correctly."""
    book = Book(title="Python Basics", category="Programming", price=30.0, image="python.jpg")
    assert book.title == "Python Basics"
    assert book.category == "Programming"
    assert book.price == 30.0
    assert book.image == "python.jpg"


def test_book_price_type():
    """Ensure book price is stored as a number."""
    book = Book("Data Science 101", "AI", 45.5, "ds.jpg")
    assert isinstance(book.price, (int, float))


# ---------- Test CartItem Class ----------
def test_cartitem_total_price():
    """Verify total price = book price * quantity."""
    book = Book("Flask Mastery", "Web", 25, "flask.jpg")
    cart_item = CartItem(book, quantity=3)
    assert cart_item.get_total_price() == 75


def test_cartitem_default_quantity():
    """Check default quantity is set to 1."""
    book = Book("ML Starter", "AI", 40, "ml.jpg")
    cart_item = CartItem(book)
    assert cart_item.quantity == 1


def test_cartitem_handles_zero_quantity():
    """Edge case: total should be zero if quantity is zero."""
    book = Book("Null Price", "Testing", 20, "n.jpg")
    cart_item = CartItem(book, quantity=0)
    assert cart_item.get_total_price() == 0
