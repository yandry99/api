from api.app import create_app, db
from api.models import Vehiculo,vehiculo_schema, vehiculos_schema
from api.models import Inspeccion,inspeccion_schema,inspecciones_schema
from api.models import Fallos,fallo_schema,fallos_schema
from api.models import CodigoFallos,codigofallos_schema,codigofallo_schema

from flask import request,redirect,jsonify


app = create_app()

# Home endpoint
@app.get('/')
def home():
    return 'Welcome to the API'

@app.post("/inspeccion/add")
def create_inspeccion():
    id_vehiculo = request.json["id_vehiculo"]
    VCC = request.json["VCC"]
    Temp_R = request.json["Temp_R"]
    Rpm = request.json["Rpm"]
    Vel = request.json["Vel"]
    Tem_A = request.json["Tem_A"]
    fecha = request.json["fecha"]
    try:
        add_inspeccion = Inspeccion(id_vehiculo=id_vehiculo, fecha=fecha, VCC=VCC, Temp_R=Temp_R, Tem_A=Tem_A,Vel=Vel,Rpm=Rpm)
        db.session.add(add_inspeccion)
        db.session.commit()
        created_vehiculo = Inspeccion.query.filter_by(id_vehiculo=id_vehiculo).order_by(Inspeccion.id.desc())
    except Exception as e:
        print(f"Error {e}")

    all_vehiculos = inspecciones_schema.dump(created_vehiculo)
    return jsonify(all_vehiculos[0]['id'])

@app.post("/fallos/add")
def create_fallos():
    id_inspeccion = request.json["id_inspeccion"]
    fallos = request.json["fallos"]
    try:
        add_fallos = Fallos(id_inspeccion=id_inspeccion, fallos=fallos)
        db.session.add(add_fallos)
        db.session.commit()
        created_fallos = Fallos.query.filter_by(id_inspeccion=id_inspeccion).order_by(Fallos.id.desc())
    except Exception as e:
        print(f"Error {e}")

    all_fallos = fallos_schema.dump(created_fallos)
    return jsonify(all_fallos[0]['id'])

@app.get("/inspeccion/<int:id>")
def get_inspeccion(id):
    inspeccion = Inspeccion.query.filter_by(id_vehiculo=id).order_by(Inspeccion.fecha.desc())
    all_vehiculos = inspecciones_schema.dump(inspeccion)
    return jsonify(all_vehiculos)

@app.get("/vehiculos")
def get_vehiculos():
    vehiculos = Vehiculo.query.all()
    all_vehiculos = vehiculos_schema.dump(vehiculos)
    return jsonify(all_vehiculos)

@app.get("/fallos/<id>")
def get_fallos(id):
    user = Fallos.query.filter_by(id_inspeccion=id)
    all_vehiculos = fallos_schema.dump(user)
    return jsonify(all_vehiculos[0]['fallos'])

@app.get("/descripcionfallos/<id>")
def get_descripcionfallos(id):
    descripcionfallos = CodigoFallos.query.filter_by(CodigoDTC=id)
    all_fallos = codigofallos_schema.dump(descripcionfallos)
    return jsonify(all_fallos[0]['Descripcion'])
