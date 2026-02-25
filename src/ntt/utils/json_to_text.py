def recursive_json(data, degre=0, texte_out=""):
    """
    Recursively convert a JSON object to a text file.
    
    Args:
        data: The JSON object to convert.
        degre: The current degree of recursion.
        texte_out: The text to append to.
    
    Returns:
        The text representation of the JSON object.
    """
    type_valide = (str, float, int, bool)
    if isinstance(data, type_valide) or data is None:
        texte = str(data)
        texte_part = '\t' * degre + texte + '\n'
        return texte_part
        
    elif isinstance(data, dict):
        texte_part = ''
        for key, value in data.items():
            texte_part += '\t' * degre + str(key) + '\n' + recursive_json(value, degre=degre + 1)
        return texte_part
        
    elif isinstance(data, list):
        texte_part = ''
        for i, value in enumerate(data):
            texte_part += '\t' * degre + str(i) + '\n' + recursive_json(value, degre=degre + 1)
        return texte_part

# Backwards compatibility alias
Recursive_json = recursive_json