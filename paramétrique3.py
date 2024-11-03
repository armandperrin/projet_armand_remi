def addition(a, b):
    """
    Additionne deux nombres.

    Args:
        a (int): Le premier nombre.
        b (int): Le deuxième nombre.

    Returns:
        int: La somme de `a` et `b`.
    """
    return a + b


import pytest

@pytest.mark.parametrize(
    "a, b, resultat",
    [
        (1, 2, 3),  # test si 1 + 2 = 3
        (10, 5, 15),  # test si 10 + 5 = 15
        (-1, 1, 0),  # test si -1 + 1 = 0
        (0, 0, 0),  # test si 0 + 0 = 0
    ],
)
def test_addition(a, b, resultat):
    """
    Teste la fonction `addition`.

    Vérifie si l'addition de `a` et `b` retourne le `resultat` attendu.

    Args:
        a (int): Le premier nombre pour le test.
        b (int): Le deuxième nombre pour le test.
        resultat (int): Le résultat attendu.
    """
    assert addition(a, b) == resultat
