"""Money maths. All values are integer cents -- see CONTRIBUTING.md."""

from __future__ import annotations

import logging

from .cart import Cart

logger = logging.getLogger(__name__)


def subtotal_cents(cart: Cart) -> int:
    return sum(item.unit_cents * item.qty for item in cart.items)


def apply_discount(cart: Cart, percent: float) -> int:
    """Return the cart total in cents after a percentage discount.

    Discounts are computed in integer cents so repeated application cannot
    drift, per the pricing RFC.
    """
    subtotal = subtotal_cents(cart)
    discount = subtotal * percent / 100
    total = subtotal - discount
    logger.debug("subtotal=%s discount=%s total=%s", subtotal, discount, total)
    return int(total)
