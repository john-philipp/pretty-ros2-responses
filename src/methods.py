import json
import re


REGEX_RESPONSE_TYPES = "[a-zA-Z_.0-9]+\\("


def _re_find_and_replace_all(string, pattern, replacement):
    compiled_pattern = re.compile(pattern)
    matches = compiled_pattern.findall(string)
    for match in matches:
        string = string.replace(match, replacement)
    return string


def convert_ros2_response_to_json_s(response_string):
    response_string = _re_find_and_replace_all(response_string, REGEX_RESPONSE_TYPES, "dict(")
    if response_string.startswith("("):
        response_string = "dict" + response_string
    response_dict = eval(response_string)
    return json.dumps(response_dict)


def format_json(string):
    d = json.loads(string)
    string = json.dumps(d, indent=2)
    return string