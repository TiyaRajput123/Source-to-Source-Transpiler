import re

def parse_python_code(code):
    lines = code.split('\n')
    parsed_lines = []

    for line in lines:
        stripped = line.strip()
        indent = len(line) - len(stripped)

        if stripped.startswith('print('):
            parsed_lines.append(('print', stripped[6:-1], indent))
        elif 'input(' in stripped:
            var, expr = stripped.split('=')
            parsed_lines.append(('input', var.strip(), indent))
        elif '=' in stripped:
            var, expr = stripped.split('=')
            parsed_lines.append(('assign', (var.strip(), expr.strip()), indent))
        else:
            parsed_lines.append(('raw', stripped, indent))

    return parsed_lines