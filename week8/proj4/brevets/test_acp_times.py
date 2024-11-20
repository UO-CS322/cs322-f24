"""
Pytests for functionality of acp_times.py

Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders

"""

import arrow
import pytest

import acp_times

start_time = arrow.get("2024-01-01T00:00:00+00:00")
brevet_length = 1000  # make it the max long brevet so that we can test functionality for each threshold


def test_none():
    """Test the open/close time threshold for 0 distance."""
    # Test open time
    expected_open_time = start_time.isoformat()
    assert (
        acp_times.open_time(0, brevet_length, start_time.isoformat())
        == expected_open_time
    )
    # Test close time
    expected_close_time = start_time.shift(hours=1).isoformat()
    assert (
        acp_times.close_time(0, brevet_length, start_time.isoformat())
        == expected_close_time
    )


def test_200():
    """Test the open/close time threshold for 200 distance."""
    # Test open time
    expected_open_time = start_time.shift(hours=5, minutes=53).isoformat()
    assert (
        acp_times.open_time(200, brevet_length, start_time.isoformat())
        == expected_open_time
    )
    # Test close time
    expected_close_time = start_time.shift(hours=13, minutes=20).isoformat()
    assert (
        acp_times.close_time(200, brevet_length, start_time.isoformat())
        == expected_close_time
    )


def test_400():
    """Test the open/close time threshold for 400 distance."""
    # Test open time
    expected_open_time = start_time.shift(hours=12, minutes=8).isoformat()
    assert (
        acp_times.open_time(400, brevet_length, start_time.isoformat())
        == expected_open_time
    )
    # Test close time
    expected_close_time = start_time.shift(days=1, hours=2, minutes=40).isoformat()
    assert (
        acp_times.close_time(400, brevet_length, start_time.isoformat())
        == expected_close_time
    )


def test_600():
    """Test the open/close time threshold for 600 distance."""
    # Test open time
    # Test open time
    expected_open_time = start_time.shift(hours=18, minutes=48).isoformat()
    assert (
        acp_times.open_time(600, brevet_length, start_time.isoformat())
        == expected_open_time
    )
    # Test close time
    expected_close_time = start_time.shift(days=1, hours=16).isoformat()
    assert (
        acp_times.close_time(600, brevet_length, start_time.isoformat())
        == expected_close_time
    )


def test_1000():
    """Test the open/close time threshold for 1000 distance."""
    # Test open time
    expected_open_time = start_time.shift(days=1, hours=9, minutes=5).isoformat()
    assert (
        acp_times.open_time(1000, brevet_length, start_time.isoformat())
        == expected_open_time
    )
    # Test close time
    expected_close_time = start_time.shift(days=3, hours=3).isoformat()
    assert (
        acp_times.close_time(1000, brevet_length, start_time.isoformat())
        == expected_close_time
    )


def main():
    result = pytest.main()
    if result == 0:
        print(f"Yas! All tests pass. Bless up tbh")
    else:
        print(f"Darn. Some tests failed.")


if __name__ == "__main__":
    main()
