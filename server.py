from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# Rota principal (opcional)
@app.route("/")
def home():
    return "Servidor rodando!"

# Rota que realmente processa
@app.route("/process", methods=["POST"])
def process():
    data = request.json.get("value", 0)

    # Simulação de processamento pesado
    time.sleep(0.2)  # 200 ms

    result = data * data  # operação qualquer

    return jsonify({
        "input": data,
        "output": result
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)


