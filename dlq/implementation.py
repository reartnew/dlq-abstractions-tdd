# -*- coding: utf-8 -*-

from . import abstract

__all__ = [
    "DLQ",
    "DLQItem",
]


class DLQ(abstract.AbstractDLQ):
    pass


class DLQItem(abstract.AbstractDLQItem):
    pass
