"""TODO : json_to_text module provides ...
"""


def recursive_json(data, degre=0):
    """_summary_

    Args:
        data (_type_): _description_
        degre (int, optional): _description_. Defaults to 0.
        texte_out (str, optional): _description_. Defaults to "".

    Returns:
        _type_: _description_
    """
    type_valide = [str, float, int, bool]
    if type(data) in type_valide or data is None:
        texte = str(data)
        texte_part = "\t" * degre + texte + "\n"
        return texte_part
    elif isinstance(data, dict):
        texte_part = ""
        for i in data:
            texte_part = (
                texte_part
                + "\t" * degre
                + i
                + "\n"
                + recursive_json(data[i], degre=degre + 1)
            )
        return texte_part

    elif isinstance(data, list):
        texte_part = ""
        # TODO : Find a better name for val
        for i, val in enumerate(data):
            texte_part = (
                texte_part
                + "\t" * degre
                + str(i)
                + "\n"
                + recursive_json(val, degre=degre + 1)
            )
        return texte_part
