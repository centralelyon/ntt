import numpy as np

def texte_to_json(texte):
    """
    Convert a text file to a JSON object.
    
    Args:
        texte: The text file to convert.
    
    Returns:
        The JSON object.
    """
    data = texte.split('\n')
    texte_out = recursive_liste_json(data)
    return texte_out

def recursive_liste_json(liste, degre=0):
    """
    Recursively convert a list of strings to a JSON object.
    
    Args:
        liste: The list of strings to convert.
        degre: The current degree of recursion.
    
    Returns:
        The JSON object.
    """
    if len(liste) == 1:
        retour = liste[0].split('\t')[-1]
        try:
            retour = int(retour)
        except ValueError:
            try:
                retour = float(retour)
                if np.isnan(retour):
                    retour = None
            except ValueError:
                if retour == 'True':
                    retour = True
                elif retour == 'False':
                    retour = False
        return retour
    elif len(liste) > 1:
        res = [[], []]
        for indexe in range(len(liste)):
            t = liste[indexe].split('\t')
            if len(t) < degre + 2:
                res[0].append(indexe)
                res[1].append(t[-1])
        if not res[1]:
            return None
        
        if res[1][0] == '0':
            donne = []
            for i in range(len(res[0]) - 1):
                donne.append(recursive_liste_json(liste[res[0][i] + 1:res[0][i + 1]], degre=degre + 1))
            donne.append(recursive_liste_json(liste[res[0][-1] + 1:], degre=degre + 1))
        else:
            donne = {}
            for i in range(len(res[0]) - 1):
                donne[res[1][i]] = recursive_liste_json(liste[res[0][i] + 1:res[0][i + 1]], degre=degre + 1)
            
            donne[res[1][-1]] = recursive_liste_json(liste[res[0][-1] + 1:], degre=degre + 1)
        return donne

# Backwards compatibility aliases
Texte_to_json = texte_to_json
Recursive_liste_json = recursive_liste_json