import argparse
import json
import re
import os
import ast


REGEX_RESPONSE_TYPES = "[a-zA-Z_.0-9]+\\("
ENV_VAR_INCLUDE_TYPES = "PR_I"
DEFAULT_INCLUDE_TYPES = False
try:
    # We can specify defaults via env var.
    DEFAULT_INCLUDE_TYPES = ast.literal_eval(os.environ[ENV_VAR_INCLUDE_TYPES])
except (KeyError, ValueError):
    pass


def handle_input_args(*args):
    parser = argparse.ArgumentParser(prog='pretty-ros2-responses', description='Prettify ROS2 responses.')
    parser.add_argument(
        '-i', '--include-types',
        action="store_true",
        default=DEFAULT_INCLUDE_TYPES,
        help="Include types as '_type' in JSON.")
    return parser.parse_args(args=args)


def convert_ros2_response_to_json_s(response_string, include_types):
    compiled_pattern = re.compile(REGEX_RESPONSE_TYPES)
    matches = compiled_pattern.findall(response_string)
    for match in matches:
        if include_types:
            # Allows to include type in response. Doing this on
            # the inside means we avoid nesting the structure
            # further, and we get to skip the matching nested
            # braces part.
            response_string = response_string.replace(match, f"dict(_type='{match[:-1]}', ")
        else:
            response_string = response_string.replace(match, "dict(")
    if response_string.startswith("("):
        response_string = "dict" + response_string
    response_dict = eval(response_string)
    return json.dumps(response_dict)


def format_json(string):
    d = json.loads(string)
    string = json.dumps(d, indent=2)
    return string
