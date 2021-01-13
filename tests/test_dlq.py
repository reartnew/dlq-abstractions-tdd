# -*- coding: utf-8 -*-
# pylint: disable=abstract-class-instantiated

import dlq


def _test_123(queue: dlq.AbstractDLQ) -> None:
    assert queue.first() is not None
    assert queue.last() is not None
    assert queue.first().value == 1
    assert queue.last().value == 3
    assert queue.first().next().value == 2
    assert queue.first().next() is queue.last().previous()


def test_init_empty():
    queue = dlq.DLQ()
    assert queue.first() is None
    assert queue.last() is None


def test_init_with_initializer():
    queue = dlq.DLQ([1, 2, 3])
    _test_123(queue)


def test_appends():
    queue = dlq.DLQ()
    queue.append(2)
    queue.append(3)
    queue.appendleft(1)
    _test_123(queue)


def test_pops():
    queue = dlq.DLQ([0, 1, 2, 3, 4])
    assert queue.pop() == 4
    assert queue.popleft() == 0
    _test_123(queue)


def test_iter():
    queue = dlq.DLQ([1, 2, 3])
    assert list(queue) == [1, 2, 3]


def test_equal():
    assert dlq.DLQ([1001, 1002, 1003]) == dlq.DLQ([1001, 1002, 1003])


def test_equal_empty():
    assert dlq.DLQ() == dlq.DLQ()


def test_non_equal_same_length():
    assert dlq.DLQ([1, 2, 3]) != dlq.DLQ([3, 2, 1])


def test_non_equal_different_length():
    assert dlq.DLQ([1, 2, 3]) != dlq.DLQ([1, 2, 3, 4])
