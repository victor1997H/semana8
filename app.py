from flask import Flask, request, render_template_string, redirect

app = Flask(__name__)

# Lista en memoria
tasks = []

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Lista de Tareas</title>
    <style>
        body {
            font-family: Arial;
            background: #f4f6f8;
            display: flex;
            justify-content: center;
            padding-top: 50px;
        }
        .container {
            background: white;
            padding: 20px;
            border-radius: 10px;
            width: 400px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 { text-align: center; }
        form { display: flex; gap: 10px; }
        input {
            flex: 1;
            padding: 8px;
        }
        button {
            padding: 8px;
            background: #007bff;
            color: white;
            border: none;
            cursor: pointer;
        }
        ul { list-style: none; padding: 0; }
        li {
            background: #eee;
            margin-top: 10px;
            padding: 8px;
            display: flex;
            justify-content: space-between;
        }
        a {
            color: red;
            text-decoration: none;
        }
    </style>
</head>
<body>
<div class="container">
    <h1>📋 Lista de Tareas</h1>

    <form method="POST">
        <input name="task" placeholder="Nueva tarea..." required>
        <button type="submit">Agregar</button>
    </form>

    <ul>
        {% for t in tasks %}
        <li>
            {{ t }}
            <a href="/delete/{{ loop.index0 }}">X</a>
        </li>
        {% endfor %}
    </ul>
</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        task = request.form.get("task")
        tasks.append(task)
        return redirect("/")
    return render_template_string(HTML, tasks=tasks)

@app.route("/delete/<int:index>")
def delete(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)