# -*- coding: utf-8 -*-

from __future__ import annotations
import typing as t
import abc

__all__ = [
    "AbstractDLQ",
    "AbstractDLQItem",
    "VT",
]

# Value type
VT = t.TypeVar("VT")


class AbstractDLQ(abc.ABC):

    @abc.abstractmethod
    def __init__(self, initializer: t.Optional[t.Iterable[VT]] = None) -> None:
        """:param initializer: Fill the DLQ with initializer items, if given"""

    @abc.abstractmethod
    def first(self) -> t.Optional[AbstractDLQItem]:
        """:return: The first item, if the DLQ is non-empty (None otherwise)"""

    @abc.abstractmethod
    def last(self) -> t.Optional[AbstractDLQItem]:
        """:return: The last item, if the DLQ is non-empty (None otherwise)"""

    @abc.abstractmethod
    def append(self, value: VT) -> AbstractDLQItem[VT]:
        """:param value: anything that shuold be stored in the end of the DLQ
           :return: The corresponding DLQ item"""

    @abc.abstractmethod
    def appendleft(self, value: VT) -> AbstractDLQItem[VT]:
        """:param value: anything that shuold be stored in the begginning of the DLQ
           :return: The corresponding DLQ item"""

    @abc.abstractmethod
    def pop(self) -> VT:
        """:return: The last DLQ element value, removing from the original DLQ
           :raise: KeyError on emptiness"""

    @abc.abstractmethod
    def popleft(self) -> VT:
        """:return: The first DLQ element value, removing from the original DLQ
           :raise: KeyError on emptiness"""

    @abc.abstractmethod
    def __iter__(self) -> t.Iterable[VT]:
        """:return: An iterable object representing DLQ sequence values"""


class AbstractDLQItem(abc.ABC, t.Generic[VT]):
    @property
    @abc.abstractmethod
    def value(self) -> VT:
        """:return: containing value"""

    @abc.abstractmethod
    def next(self) -> t.Optional[AbstractDLQItem]:
        """:return: next DLQ item, if any, or None otherwise"""

    @abc.abstractmethod
    def previous(self) -> t.Optional[AbstractDLQItem]:
        """:return: previous DLQ item, if any, or None otherwise"""
