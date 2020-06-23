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


def pass_partout(n: int, m: int, s_p_p: list, portes: list)-> int:
    """fonction qui retourne 0 si toutes les portes ne peuvent pas être ouverte
    sinon le nombre de clé minimum nécessaire
    ----
    :pre:
        - n est un int et 1 <= u <= 10 ** 3
        - m est un int et 1 <= m <= 10 ** 5
        - s_p_p est une list de n tuples \
            d'entier et 1 <= x_i, y_i <= 10 ** 9
        - portes est une list de m tuples \
            d'entier et 1 <= s_i <= 10 ** 9\
                et -1 == a_i ou 1 == a_i
    :post:
        - return_value est un int et 0 <= return_value <= 2
    """

    # Assertion pre
    assert isinstance(n, int), \
        "n must be a int, not {}".format(type(n))
    assert 1 <= n <= 10 ** 3, \
        "n must be in [1, 10 ** 3], not {}".format(n)
    assert isinstance(m, int), \
        "m must be a int, not {}".format(type(m))
    assert 1 <= m <= 10 ** 5, \
        "m must be in [1, 10 ** 5], not {}".format(m)
    assert isinstance(s_p_p, list), \
        "s_p_p must be a list, not {}".format(type(m))
    for i, j in enumerate(s_p_p):
        assert isinstance(j, tuple), \
            "element {} of s_p_p must be a tuple, not {}".format(i, type(j))
        assert len(j) == 2, \
            "element {} of s_p_p must have a lengh of 2, not {}".format(i, len(j))
        for k, l in enumerate(j):
            assert isinstance(l, int), \
                "element {} of element {} of s_p_p must be a int, not {}".format(k, i, type(l))
            assert 1 <= l <= 10 ** 9, \
                "element {} of element {} of s_p_p must be in [1, 10 ** 9], not {}".format(k, i, l)
    for i, j in enumerate(portes):
        assert isinstance(j, tuple), \
            "element {} of portes must be a tuple, not {}".format(i, type(j))
        assert len(j) == 2, \
            "element {} of portes must have a lengh of 2, not {}".format(i, len(j))
        for k, l in enumerate(j):
            assert isinstance(l, int), \
                "element {} of element {} of portes must be a int, not {}".format(k, i, type(l))
        assert -1 <= j[0] <= 1, \
            "element 0 of element {} of portes must be in [-1, 1], not {}".format(i, j[0])
        assert 1 <= j[1] <= 10 ** 9, \
            "element 1 of element {} of portes must be in [1, 10 ** 9], not {}".format(i, j[1]) 

    return_value = 0
    open_door = 0
    # le programme s'occupe des anciennes portes
    best_pp_o, best_pp_n = [s_p_p[0]] * 2

    for i in s_p_p[1:]:
        x_i, y_i = i
        if x_i > best_pp_o[0]:
            best_pp_o = i
        if y_i > best_pp_n[1]:
            best_pp_n = i

    for porte in portes:
        porte: tuple
        age, level_door = porte
        # si la porte est d'avant 1990 et si la porte est ouvrable
        if (age == -1 and best_pp_o[0] >= level_door) \
            or (age == 1 and best_pp_n[0] >= level_door):
            open_door += 1

    if open_door == m:
        if best_pp_n == best_pp_o:
            return_value = 1
        else:
            return_value = 2

    assert isinstance(return_value, int), \
        "return_value must be a int, not {}".format(type(return_value))

    return return_value


if __name__ == "__main__":
    demande = input("quelle algo ")
    if demande == "1":

        N_M = input()
        while not(re.findall(r"^\d+ \d+$", N_M)) \
            and 1 <= int(N_M.split(" ")[0]) <= 273 \
                and 1 <= int(N_M.split(" ")[1]) <= 273:
            N_M = input()
        N, M = N_M.split(" ")
        N = int(N)
        M = int(M)

        S_n = []
        for i in range(N):
            a = input()
            while not re.findall("^[ o]{" + str(M) + "}$", a):
                a = input(str(i))
            S_n.append(a)
    else:
        N = input()
        while not re.findall(r"^\d+$", N) and 1 <= int(N) <= 10 ** 3:
            N = input()
        N = int(N)
        passes_partout = []
        for i in range(N):
            passe_partout = input()
            while not(re.findall(r"^\d+ \d+$", passe_partout)) \
                and 1 <= int(passe_partout.split(" ")[0]) <= 10 ** 6 \
                    and 1 <= int(passe_partout.split(" ")[0]) <= 10 ** 6:
                passe_partout = input()
            passes_partout.append(passe_partout.split(" "))
        del passe_partout

        M = input()
        while not(re.findall(r"^\d+$", M)) and 1 <= int(M) <= 10 ** 6:
            M = input()
        M = int(M)

        Portes = []
        for i in range(M):
            porte = input()
            while not(re.findall(r"^1 \d+$|^-1 \d+$", porte)) and (-1 == porte.split(" ")[0] or 1 == porte.split(" ")[0]) \
                and 1 <= porte.split(" ")[1] <= 10 ** 6:
                porte = input()
            Portes.append(porte.split(" "))
        print(pass_partout(N, M, passes_partout, Portes))
