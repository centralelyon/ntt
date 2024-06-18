# pylint: disable=C0114

import json
import os

from dotenv import load_dotenv
from ntt.utils.json_to_text import recursive_json

if __name__ == "__main__":
    load_dotenv()
    json_file = os.path.join(os.environ.get("PATH_IN"), "org_jtt.json")
    output_file = os.path.join(os.environ.get("PATH_IN"), "res_jtt.txt")
    # upload json data from file
    with open(json_file, "r") as file:
        data = json.load(file)

    text_data = recursive_json(data)

    # write formatted data in text file
    with open(output_file, "w") as file:
        file.write(text_data)
