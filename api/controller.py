import sqlite3
from db import create_connection


def insert_game(data):
    connection = create_connection()

    try:
        cur = connection.cursor()
        #insertar inspeccion
        sqlstr = "INSERT INTO inspeccion ('id_vehiculo', 'VCC', 'Temp_R','RPM','Vel','Tem_A','fecha') ""VALUES (?,?,?,?,?,?,?)"
        cur.execute(sqlstr, data)
        connection.commit()
        return True
    except sqlite3.Error  as err:
        print(f"Error at insert_recuoe function: {err.msg}")
        return False
    finally:
        cur.close()
        connection.close()


def get_fallos(id_inspeccion):

    db = create_connection()

    cursor = db.cursor()

    sqlstr = 'SELECT * FROM fallos where fecha = ?  LIMIT 7'

    cursor.execute(sqlstr,[id_inspeccion])

    return cursor.fetchall()

def get_codifoFallos(row):

    db = create_connection()

    cursor = db.cursor()

    sqlstr = f"""SELECT * FROM codigo_fallos where CodigoDTC like '%{row}%'"""

    cursor.execute(sqlstr)

    return cursor.fetchall()