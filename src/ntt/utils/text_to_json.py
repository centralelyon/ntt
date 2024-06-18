"""TODO : temporal module provides ...
"""

import numpy as np


def text_to_json(text):
    """_summary_

    Args:
        text (_type_): _description_

    Returns:
        _type_: _description_
    """
    data = text.split("\n")
    text = recursive_liste_json(data)
    return text


def recursive_liste_json(liste, degre=0):
    """_summary_

    Args:
        liste (_type_): _description_
        degre (int, optional): _description_. Defaults to 0.

    Returns:
        _type_: _description_
    """
    if len(liste) == 1:
        retour = liste[0].split("\t")[-1]
        try:
            retour = int(retour)
        except ValueError:
            try:
                retour = float(retour)
                if np.isnan(retour):
                    retour = None
            except ValueError:
                if retour == "True":
                    retour = True
                elif retour == "False":
                    retour = False
        return retour
    elif len(liste) > 1:

        res = [[], []]
        for indexe in range(len(liste)):
            t = liste[indexe].split("\t")
            if len(t) < degre + 2:
                res[0].append(indexe)
                res[1].append(t[-1])
        if res[1][0] == "0":
            donne = []

            for i in range(len(res[0]) - 1):
                donne.append(
                    recursive_liste_json(
                        liste[res[0][i] + 1:res[0][i + 1]], degre=degre + 1
                    )
                )
            donne.append(recursive_liste_json(liste[res[0][-1] + 1:], degre=degre + 1))
        else:
            donne = {}
            for i in range(len(res[0]) - 1):
                donne[res[1][i]] = recursive_liste_json(
                    liste[res[0][i] + 1:res[0][i + 1]], degre=degre + 1
                )

            donne[res[1][-1]] = recursive_liste_json(
                liste[res[0][-1] + 1:], degre=degre + 1
            )
        return donne
