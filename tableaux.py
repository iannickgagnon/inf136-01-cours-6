
def tab_init_zeros(n_lignes, n_col):
    """
    Initialise un tableau avec des dimensions données.

    Aarguments:
        n_lignes (int): Nombre de lignes.
        n_col (int): Nombre de colonnes.

    Retourne:
        (list): Le tableau initialisé.
    """

    # Initialiser le tableau
    tab = []

    # Construire le tableau
    for i in range(n_lignes):

        # Initialiser la ligne courante
        ligne = []

        # Construire la ligne courante
        for j in range(n_col):
            ligne.append(0)

        # Ajoute la ligne courante
        tab.append(ligne)

    return tab
