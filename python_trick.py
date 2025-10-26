# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.18.1
# ---

# %%
# #!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2023-08-18 00:03:42
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


# self typing

from typing import Any, Self


class Stack:
    def __init__(self) -> None:
        self.items: list[Any] = []

    def push(self, item: Any) -> Self:
        self.items.append(item)
        return self

    def pop(self) -> Any:
        if self.__bool__():
            return self.items.pop()
        else:
            raise ValueError("Stack is empty")

    def __bool__(self) -> bool:
        return len(self.items) > 0

