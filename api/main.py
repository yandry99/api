"""
    API REST con Python 3 y SQLite 3
    By Parzibyte:
    ** https://parzibyte.me/blog **
"""
from flask import Flask, jsonify, request

import controller

app = Flask(__name__)

#obtener vehiculos
@app.route('/vehiculos', methods=["GET"])
def get_vehiculos():
    games = controller.get_vehiculos()
    return jsonify(games)

# obtner datos de inspeccio
@app.route("/inspeccion/<id>", methods=["GET"])
def obtener_inspeccion(id):
    inspeccion = controller.obtener_inspeccion(id)
    return jsonify(inspeccion)

# obtner datos de inspeccio
@app.route("/fallos/<id>", methods=["GET"])
def get_fallos(id):
    fallos = controller.get_fallos(id)
    return jsonify(fallos)

#obtener descripcion de fallos
@app.route("/codigo_fallos/<id>", methods=["GET"])
def get_codigo(id):
    fallos = controller.get_codifoFallos(id)
    return jsonify(fallos)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)