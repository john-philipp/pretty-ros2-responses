import sys

from rich.console import Console
from rich.json import JSON

from src.methods import convert_ros2_response_to_json_s, format_json

if __name__ == "__main__":

    console = Console()
    format_remainder = False
    lines = sys.stdin.readlines()
    for line in lines:
        line = line.strip()
        if not format_remainder:
            print(line, file=sys.stderr)

        if line == "response:":
            format_remainder = True
            continue

        if format_remainder:
            json_s = convert_ros2_response_to_json_s(line)
            console.print(JSON(format_json(json_s)))
            break

