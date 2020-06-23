import re

def pins_bound(n: int, m: int, s_n: list)-> int:
    """fonction qui retourne 1 si l'ensemble des pin's respecte la propriété de conception du laboratoire Okabé
    ----
    :pre:
        - n est un int et 1 <= n <= 273
        - m est un int et 1 <= n <= 273
        - s_n est une liste de n str
    :post:
        - return_value est un int 0 <= return value <= 1
    """

    # Assertion pre
    assert isinstance(n, int), "n must be a int, not {}".format(type(n))
    assert 1 <= n <= 273, "n must be in [1, 273], not {}".format(n)
    assert isinstance(m, int), "m must be a int, not {}".format(type(m))
    assert 1 <= m <= 273, "m must be in [1, 273], not {}".format(m)
    assert isinstance(s_n, list), "s_n must be a list, not {}".format(type(s_n))
    assert len(s_n) == n, "s_n must have {} elements instead of {} elements".format(n, len(s_n))
    for i, j in enumerate(s_n):
        assert isinstance(j, str), "element {} of s_n must be a str, not {}".format(i, type(j))
        assert len(j) == len(s_n[0]), \
            "lengh of element {} is not the same of the first element, {} instead of {}".format(i, len(j, len(s_n[0])))

    return_value = 0
    s_n = [
        "o  o",
        "o o ",
        "oo  "
    ]

    # Assertion post
    assert isinstance(return_value, int), "return_value must be a int, not {}".format(type(return_value))

    return return_value

def pass_partout(n: int, m: int, s_p_p: list, s_p: list)-> int:

    # Assertion pre
    assert isinstance(n, int), "n must be a int, not {}".format(type(n))
    assert 1 <= n <= 10 ** 3, "n must be in [1, 10 ** 3], not {}".format(n)
    assert isinstance(m, int), "m must be a int, not {}".format(type(m))
    assert 1 <= m <= 10 ** 5, "m must be in [1, 10 ** 5], not {}".format(m)
    return_value = 0
    return return_value