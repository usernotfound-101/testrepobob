from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Item:
    sku: str
    unit_cents: int
    qty: int = 1


@dataclass
class Cart:
    items: list[Item] = field(default_factory=list)

    def add(self, item: Item) -> None:
        self.items.append(item)
