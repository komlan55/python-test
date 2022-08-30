import pytest

from modules.trackers import TemperatureTracker

number_list = [22, 7, 22, 13, 2, 31, 18]


def test_insert():
    tracker = TemperatureTracker()
    tracker.insert(number_list)
    assert number_list == tracker.item_list


def test_insert_non_integer():
    tracker = TemperatureTracker()
    non_integer = "anuvu"
    with pytest.raises(Exception) as exc:
        tracker.insert(number_list + [non_integer])
    assert f"Integer only! : '{non_integer}' is not an integer" in str(exc.value)


def test_get_max():
    tracker = TemperatureTracker()
    tracker.insert(number_list)
    assert 31 == tracker.get_max()


def test_get_min():
    tracker = TemperatureTracker()
    tracker.insert(number_list)
    assert 2 == tracker.get_min()


def test_get_mean():
    tracker = TemperatureTracker()
    tracker.insert(number_list)
    assert 16.43 == tracker.get_mean()
