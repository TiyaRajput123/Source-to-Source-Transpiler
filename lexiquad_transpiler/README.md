# LexiQuad – Python to JavaScript Source-to-Source Transpiler

LexiQuad is a lightweight, modular transpiler that converts Python code to equivalent JavaScript. Built using Python’s AST (Abstract Syntax Tree) module and Flask for the web UI, LexiQuad helps developers seamlessly translate backend logic into frontend JavaScript code.

> 🚀 Developed as a team project by B.Tech CSE students — for both learning and real-world utility.

---

## 🧠 Key Features

- ✅ Translates variable assignments, arithmetic, `print()` and `input()`
- 💻 Command-Line Interface (CLI) support for offline use
- 🌐 Flask-based web interface for real-time code conversion
- 🔄 Modular, extensible codebase ready for loops, functions, conditionals
- 📁 Includes test cases to validate output correctness

---

## 💻 Technologies Used

- Python (`ast`, `os`, `sys`)
- Flask & Jinja2
- HTML, CSS
- Git & GitHub

---

## 📂 Folder Structure

lexiquad_transpiler/
├── parser.py # AST parsing of Python code
├── generator.py # JavaScript code generation
├── utils.py # Helper functions
├── main.py # Entry point for CLI
├── requirements.txt # Dependencies
├── test_cases/
│ ├── sample1.py # Example input
│ └── expected1.js # Expected output
└── web_frontend/
├── app.py # Flask backend
└── templates/
└── index.html # Web UI template


---

| Name              | Role                   
| ----------------- | ----------------------- | 
| Taru Kulshrestha  | Team Lead / Integration | 
| Sachin Singh Negi | Parser & CLI            | 
| Tiya Rajput       | Web UI Developer        |
| Sakshi Negi       | JavaScript Generator    |


