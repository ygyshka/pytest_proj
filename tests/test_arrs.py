from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], -1, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]


def test_normalized_start():
    assert arrs.my_slice([1, 2, 3], 0, 2) == [1, 2]
    assert arrs.my_slice([1, 2, 3, 4, 5], -2, 3) == []
    assert arrs.my_slice([], 0, 3) == []
    assert arrs.my_slice([1, 2, 3, 4], -5, 3) == [1, 2, 3]
