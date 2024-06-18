# pylint: disable=C0114

import json
import os

from dotenv import load_dotenv
from ntt.utils.text_to_json import text_to_json

if __name__ == "__main__":
    load_dotenv()
    text_file = os.path.join(os.environ.get("PATH_IN"), "org_ttj.txt")
    output_file = os.path.join(os.environ.get("PATH_OUT"), "res_ttj.json")
    # upload data from json
    with open(text_file, "r") as file:
        data = file.read()

    json_data = text_to_json(data)

    # write formatted data in text file
    with open(output_file, "w") as file:
        json.dump(json_data, file)
