from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Mini IA: responde un texto aleatorio (simulación simple)
responses = [
    "Hola, soy una IA básica lista para ayudarte.",
    "Procesando tu solicitud...",
    "Estoy funcionando correctamente dentro del contenedor."
]

@app.route("/")
def home():
    return "RECUPERACION"

@app.route("/ia", methods=["POST"])
def ia():
    data = request.json
    pregunta = data.get("pregunta", "")
    return jsonify({
        "pregunta": pregunta,
        "respuesta": random.choice(responses)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
