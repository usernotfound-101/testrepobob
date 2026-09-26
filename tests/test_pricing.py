from storefront import Cart, Item, apply_discount


def test_discount_applied():
    cart = Cart([Item(sku="widget", unit_cents=1999, qty=3)])
    assert apply_discount(cart, percent=17) == 4978


def test_discount_zero_percent_is_noop():
    cart = Cart([Item(sku="widget", unit_cents=1999, qty=3)])
    assert apply_discount(cart, percent=0) == 5997


def test_full_discount_is_free():
    cart = Cart([Item(sku="widget", unit_cents=1999, qty=3)])
    assert apply_discount(cart, percent=100) == 0
