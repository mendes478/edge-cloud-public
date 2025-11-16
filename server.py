from flask import Flask, request, jsonify
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "Servidor rodando!"


    # Simulação de processamento pesado (ex.: IA, análise, etc.)
    time.sleep(0.2)  # 200 ms

    result = data * data  # operação qualquer

    return jsonify({
        "input": data,
        "output": result
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

