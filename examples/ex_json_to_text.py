from ntt.utils.json_to_text import Recursive_json
import json

if __name__=="__main__":
    json_file="samples/org_jtt.json"
    output_file="samples/res_jtt.txt"
    # Charger les données JSON depuis le fichier
    with open(json_file, 'r') as file:
        data = json.load(file)

    text_data=Recursive_json(data)

    # Écrire les données formatées dans un fichier texte
    with open(output_file, 'w') as file:
        file.write(text_data)
