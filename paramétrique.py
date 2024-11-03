def addition(a, b):
    return a + b

import pytest

@pytest.mark.parametrize("a, b, resultat", [
    (1, 2, 3),        # test si 1 + 2 = 3
    (10, 5, 15),      # test si 10 + 5 = 15
    (-1, 1, 0),       # test si -1 + 1 = 0
    (0, 0, 0),        # test si 0 + 0 = 0
])
def test_addition(a, b, resultat):
    assert addition(a, b) == resultat