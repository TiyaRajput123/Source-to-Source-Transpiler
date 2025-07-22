def generate_js_code(parsed_lines):
    js_code = []
    indent_stack = []

    for stmt in parsed_lines:
        type_, content, indent = stmt

        while indent_stack and indent < indent_stack[-1]:
            js_code.append(' ' * indent_stack.pop() + '}')

        if type_ == 'print':
            js_code.append(' ' * indent + f'console.log({content});')
        elif type_ == 'input':
            js_code.append(' ' * indent + f'const {content} = await input("Enter {content}: ");')
        elif type_ == 'assign':
            var, expr = content
            js_code.append(' ' * indent + f'let {var} = {expr};')
        elif type_ == 'raw':
            js_code.append(' ' * indent + f'// {content}')  # placeholder

        if type_ in ['if', 'while', 'for']:
            indent_stack.append(indent)
            js_code.append(' ' * indent + '{')

    while indent_stack:
        js_code.append(' ' * indent_stack.pop() + '}')

    return '\n'.join(js_code)