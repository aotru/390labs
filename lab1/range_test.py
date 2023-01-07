"""Tests for range.py module."""

from range import Range


def test_basic():
    """Run basic test cases on Range."""
    range1 = Range(1, 1)
    assert not range1
    print(len(range1))
    range2 = Range(1, 5)
    assert len(range2) == 4
    print(len(range2))
    range3 = Range(1, 5, 3)
    assert len(range3) == 2
    print(len(range3))
    assert 1 in range3
    assert 4 in range3
    assert 3 not in range3
    assert 7 not in range3
    items = []
    for i in Range(-3, 11, 3):
        items.append(i)
    assert items == [-3, 0, 3, 6, 9]
    print(str(items))


def test_additional():
    """Run additional test cases on Range."""
    range1 = Range(7, 22)
    assert len(range1) == 15
    print(len(range1))
    range1 = Range(7, 22, 2)
    assert len(range1) == 8
    print(len(range1))
    range1 = Range(7, 22, 3)
    assert len(range1) == 5
    print(len(range1))
    range1 = Range(7, 22, 4)
    assert len(range1) == 4
    print(len(range1))
    items = []
    for i in range1:
        items.append(i)
    print(str(items))


if __name__ == "__main__":
    test_basic()
    test_additional()
