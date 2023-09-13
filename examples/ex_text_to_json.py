from ntt.utils.text_to_json import Texte_to_json
import json
import os
from dotenv import load_dotenv
if __name__=="__main__":
    load_dotenv()
    text_file=f"{os.environ.get('PATH_IN')}org_ttj.txt"
    output_file=f"{os.environ.get('PATH_OUT')}res_ttj.json"
    # Charger les données JSON depuis le fichier
    with open(text_file, 'r') as file:
        data = file.read()

    json_data=Texte_to_json(data)

    # Écrire les données formatées dans un fichier texte
    with open(output_file, 'w') as file:
        json.dump(json_data, file)