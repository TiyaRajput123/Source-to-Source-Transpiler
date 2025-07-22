from parser import parse_python_code
from generator import generate_js_code
import sys

def transpile_file(input_path, output_path):
    with open(input_path, 'r') as infile:
        python_code = infile.read()

    parsed_lines = parse_python_code(python_code)
    js_code = generate_js_code(parsed_lines)

    with open(output_path, 'w') as outfile:
        outfile.write(js_code)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py input.py output.js")
    else:
        transpile_file(sys.argv[1], sys.argv[2])