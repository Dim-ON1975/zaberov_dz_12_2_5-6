from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([1, 2, 3], -1, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 4, 5], -1, -3) == []
    assert arrs.my_slice([1, 2, 3, 4, 5], -5, -5) == []
    assert arrs.my_slice([1, 2, 3, 4, 5], -1, -1) == []
    assert arrs.my_slice([1, 2, 3, 4, 5], -3, -1) == [3, 4]
    assert arrs.my_slice([1, 2, 3, 4, 5], -1) == [5]
    assert arrs.my_slice([1, 2, 3, 4, 5], -5) == [1, 2, 3, 4, 5]
    assert arrs.my_slice([1, 2, 3, 4, 5], -3) == [3, 4, 5]
    # Было пропущено тестирование строк 31 и 34. Добавляем тесты
    assert arrs.my_slice([], 0) == []
    assert arrs.my_slice([1, 2, 3, 4, 5], None, 4) == [1, 2, 3, 4]
