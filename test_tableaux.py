# Librairies internes
from tableaux import (
    tab_init_zeros,
)


def test_tab_init_zeros():

    # Les dimenions du tableau de test
    nb_lignes = 4
    nb_colonnes = 3

    # Tableau attendu
    tableau_attendu = [[0, 0, 0],
                       [0, 0, 0],
                       [0, 0, 0],
                       [0, 0, 0]]

    # Tableau obtenu
    tableau_obtenu = tab_init_zeros(nb_lignes, nb_colonnes)

    assert tableau_obtenu == tableau_attendu
