from utils import arrs
import pytest


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get(["0", 1, 2, 3], 0, "test") == "0"
    assert arrs.get([1, 2, 3], -1, "test") == "test"



def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 4, 5], 0, -1) == [1, 2, 3, 4]
    assert arrs.my_slice([1, 2, 3, 2, 1], 1, 2) == [2]
    assert arrs.my_slice([]) == []
    assert arrs.my_slice([1, 2, 3, 2, 1]) == [1, 2, 3, 2, 1]


@pytest.fixture
def out_coll():
    """Так как фикстуру полноценно применить в данном задании невозможно
(судя по ответам в комментариях к сдаче домашки на my.sky.pro), то я
применил частичную фикстуру в виде списка, подставляемую в переменную array.
В связи с этим, у меня появилось покрытие 93% вместо 100% для обычных
тестов (нельзя проверить пустой список)."""
    return [1, 2, 3, 4]

def test_get(out_coll):
    assert arrs.get(out_coll, 1, "test") == 2
    assert arrs.get(out_coll, 3, "test") == 4
    assert arrs.get(out_coll, 6, "test") == "test"

def test_slice(out_coll):
    assert arrs.my_slice(out_coll, 1, 3) == [2, 3]
    assert arrs.my_slice(out_coll, 0, 1) == [1]
    assert arrs.my_slice(out_coll) == [1, 2, 3, 4]

