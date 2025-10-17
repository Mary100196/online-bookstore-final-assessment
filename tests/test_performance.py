import timeit
import cProfile
import pstats
from io import StringIO
from models import Book, CartItem


# ---------- Using timeit ----------
def test_cartitem_performance():
    """Check that total price calculation runs efficiently."""
    setup_code = """
from models import Book, CartItem
book = Book('Speed Book', 'Performance', 20, 'speed.jpg')
cart_item = CartItem(book, quantity=1000)
"""
    test_code = "cart_item.get_total_price()"

    # Run the timing test 1000 times
    execution_time = timeit.timeit(test_code, setup=setup_code, number=1000)
    print(f"\n[timeit] Execution time for get_total_price(): {execution_time:.6f}s")
    assert execution_time < 0.1  # should execute quickly


# ---------- Using cProfile ----------
def test_app_profile():
    """Generate a performance profile for CartItem calculations."""
    pr = cProfile.Profile()
    book = Book("Deep Dive", "Performance", 25, "deep.jpg")
    cart_item = CartItem(book, quantity=10000)

    pr.enable()
    for _ in range(500):
        cart_item.get_total_price()
    pr.disable()

    # Capture profiling stats
    s = StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats("cumulative")
    ps.print_stats(10)
    print("\n[cProfile] Top 10 cumulative time functions:")
    print(s.getvalue())

    # Basic performance assertion
    total_time = sum([x[3] for x in ps.stats.values()])
    assert total_time < 1.0  # the function should be lightweight
