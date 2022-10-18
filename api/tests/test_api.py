def test_create_isnpeccion(client):
    path = "inspeccion/add"
    matricula = "1"
    VCC = "365"
    Temp_R = "45"
    Rpm = "587"
    Vel = "45"
    Tem_A = "28"
    fecha = "12-10-2021"
    response = client.post(path,
                           json={
                               "id_vehiculo": matricula,
                               "VCC": VCC,
                               "Temp_R": Temp_R,
                               "Rpm": Rpm,
                               "Vel": Vel,
                               "Tem_A": Tem_A,
                               "fecha": fecha,
                           },
                           )
    assert response.status_code == 200

def test_create_fallos(client):
    path = "fallos/add"
    id_inspeccion = "1"
    fallos = "365"

    response = client.post(path,
                           json={
                               "id_inspeccion": id_inspeccion,
                               "fallos": fallos,
                           },
                           )
    assert response.status_code == 200

def test_obtener_historial(client):
    path = "fallos/2"
    response = client.get('http://127.0.0.1:8080/'+path)
    assert response.status_code == 200

def test_obtener_inspeccion(client):
    path = "inspeccion/2"
    response = client.get('http://127.0.0.1:5000/'+path)
    assert response.status_code == 200


def test_obtener_vehiculo(client):
    path = "vehiculos"
    response = client.get('http://127.0.0.1:5000/'+path)
    assert response.status_code == 200
