from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(
    "mongodb+srv://adminmongo:Admin123456@logistica.apu736t.mongodb.net/logistica?retryWrites=true&w=majority&appName=logistica"
)

db = client["logistica"]


def obtener_coleccion_vehiculos():
    colecciones = db.list_collection_names()

    if "vehiculos" in colecciones:
        return db["vehiculos"]

    if "vehículos" in colecciones:
        return db["vehículos"]

    return db["vehiculos"]


@app.route("/")
def index():
    total_rutas = db["rutas"].count_documents({})
    total_clientes = db["clientes"].count_documents({})
    total_conductores = db["conductores"].count_documents({})
    total_vehiculos = obtener_coleccion_vehiculos().count_documents({})

    return render_template(
        "index.html",
        rutas=total_rutas,
        clientes=total_clientes,
        conductores=total_conductores,
        vehiculos=total_vehiculos
    )


@app.route("/rutas")
def rutas():
    lista_rutas = list(db["rutas"].find())
    return render_template("rutas.html", rutas=lista_rutas)


@app.route("/vehiculos")
def vehiculos():
    lista_vehiculos = list(obtener_coleccion_vehiculos().find())
    return render_template("vehiculos.html", vehiculos=lista_vehiculos)


@app.route("/agregar_vehiculo", methods=["GET", "POST"])
def agregar_vehiculo():
    if request.method == "POST":
        nuevo_vehiculo = {
            "vehiculo_id": request.form["vehiculo_id"],
            "placa": request.form["placa"],
            "marca": request.form["marca"],
            "modelo": request.form["modelo"],
            "tipo": request.form["tipo"],
            "capacidad_kg": int(request.form["capacidad_kg"]),
            "estado": request.form["estado"]
        }

        obtener_coleccion_vehiculos().insert_one(nuevo_vehiculo)

        return redirect(url_for("vehiculos"))

    return render_template("agregar_vehiculo.html")


@app.route("/clientes")
def clientes():
    lista_clientes = list(db["clientes"].find())
    return render_template("clientes.html", clientes=lista_clientes)


@app.route("/conductores")
def conductores():
    lista_conductores = list(db["conductores"].find())
    return render_template("conductores.html", conductores=lista_conductores)


if __name__ == "__main__":
    app.run(debug=True)