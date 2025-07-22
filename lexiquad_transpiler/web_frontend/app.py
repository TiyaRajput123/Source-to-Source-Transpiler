from flask import Flask, render_template, request
from parser import parse_python_code
from generator import generate_js_code

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    js_code = ""
    python_code = ""

    if request.method == "POST":
        python_code = request.form["python_code"]
        parsed = parse_python_code(python_code)
        js_code = generate_js_code(parsed)

    return render_template("index.html", python_code=python_code, js_code=js_code)

if __name__ == "__main__":
    app.run(debug=True)