from storefront import Cart, Item, subtotal_cents


def test_subtotal_sums_line_items():
    cart = Cart([Item(sku="widget", unit_cents=1999, qty=3)])
    assert subtotal_cents(cart) == 5997


def test_empty_cart_is_free():
    assert subtotal_cents(Cart()) == 0
