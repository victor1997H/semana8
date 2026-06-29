from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Semana 8 - Lista de Tareas</title>
        <style>
            body { font-family: 'Segoe UI', sans-serif; background: #f0f4f8; color: #333; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
            .container { background: white; padding: 40px; border-radius: 12px; box-shadow: 0 8px 24px rgba(0,0,0,0.05); text-align: center; max-width: 450px; width: 100%; }
            h1 { color: #1a365d; margin-bottom: 10px; }
            p { color: #4a5568; font-size: 14px; margin-bottom: 30px; }
            .badge { background: #e6fffa; color: #234e52; padding: 6px 12px; border-radius: 20px; font-size: 12px; font-weight: bold; }
            ul { list-style: none; padding: 0; margin: 20px 0; text-align: left; }
            li { padding: 12px 16px; background: #f7fafc; margin-bottom: 8px; border-radius: 8px; border-left: 4px solid #3182ce; font-size: 14px; }
            li.done { border-left-color: #38a169; background: #f0fff4; }
        </style>
    </head>
    <body>
        <div class="container">
            <span class="badge">🟢 DESPLIEGUE EN PUERTO 1004</span>
            <h1>📋 Semana 8: Lista de Tareas</h1>
            <p>Proyecto Python + Flask corriendo de forma limpia en Swarm.</p>
            <ul>
                <li class="done">✓ Repositorio "semana8" creado limpio</li>
                <li class="done">✓ Publicado en GitHub Packages</li>
                <li class="done">✓ GitHub Actions corriendo en verde</li>
                <li>⏳ ¡Despliegue completado con éxito!</li>
            </ul>
        </div>
    </body>
    </html>
    ''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)