#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2025-10-15 20:06:49
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0
# basedpyright: strict

# %%
from pydantic import BaseModel
from typing import Any


class ItemModel(BaseModel):
    name: str
    quantity: int


items: list[str] = ["apple", "banana", "cherry", "date"]
books: Any = ["yama", "kuma", "ninja", "hero"]
my_items: list[ItemModel] = [
    ItemModel(name="item1", quantity=10),
    ItemModel(name="item2", quantity=20),
]

for item in items:
    print(f"Item: {item}, Type: {type(item)}")

print("All items processed.")

# %%
