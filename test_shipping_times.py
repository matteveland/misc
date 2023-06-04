import pytest
from shipping_times import shipping_times


def test_shipping_times():
    assert shipping_times("2023-06-16", "7") == 2
    assert shipping_times("2023-06-06", "15") == 13
    assert shipping_times("2023-07-03", "7") == 4
    assert shipping_times("2023-07-03", "15") == 5
    assert shipping_times("2023-07-04", "8") == 12
    assert shipping_times("2023-08-24", "15") == 13
    assert shipping_times("2023-08-25", "8") == 14
    assert shipping_times("2023-07-25", "16") == 13
    assert shipping_times("2023-07-25", "7") == 14
    assert shipping_times("2023-10-27", "7") == 14
    assert shipping_times("2023-10-27", "15") == 13
    assert shipping_times("2023-06-23", "15") == 13
    assert shipping_times("2024-05-24", "15") == 3
    assert shipping_times("2024-05-24", "7") == 2
