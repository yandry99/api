from api.app import db,ma

#============================ Modelo Vehiculos ================================#
class Vehiculo(db.Model):
    id_vehiculo= db.Column(db.Integer, primary_key =True)
    matricula=db.Column(db.String(100),nullable=False )

    def __repr__(self):
        return "<matricula %r>" % self.matricula

class VehiculoSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id_vehiculo", "matricula")

vehiculo_schema = Vehiculo()
vehiculos_schema = VehiculoSchema(many=True)
#============================Modelo Inspeccion ================================#
class Inspeccion(db.Model):
    id= db.Column(db.Integer, primary_key =True)
    id_vehiculo= db.Column(db.Integer,nullable=False)
    VCC=db.Column(db.String(100),nullable=False )
    Temp_R=db.Column(db.String(100),nullable=False )
    Tem_A=db.Column(db.String(100),nullable=False )
    Rpm=db.Column(db.String(100),nullable=False )
    Vel=db.Column(db.String(100),nullable=False )
    fecha=db.Column(db.String(100),nullable=False )

    def __repr__(self):
        return "<Matricula %r>" % self.id_vehiculo

class InspeccionSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id","id_vehiculo", "VCC", "Temp_R", "Tem_A", "Rpm", "Vel", "fecha")

inspeccion_schema = Inspeccion()
inspecciones_schema = InspeccionSchema(many=True)
#============================ Modelo Fallos ================================#
class Fallos(db.Model):
    id= db.Column(db.Integer, primary_key =True)
    id_inspeccion= db.Column(db.Integer,nullable=False)
    fallos=db.Column(db.String(100),nullable=False )

    def __repr__(self):
        return "<id %r>" % self.fallos

class FallosSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id","id_inspeccion", "fallos")

fallo_schema = Fallos()
fallos_schema = FallosSchema(many=True)
#============================ Modelo Codigofallos ================================#
class CodigoFallos(db.Model):
    id= db.Column(db.Integer, primary_key =True)
    CodigoDTC= db.Column(db.String(100), nullable=False)
    Descripcion= db.Column(db.String(100),nullable=False)

    def __repr__(self):
        return "<id %r>" % self.Descripcion

class CodigoFallosSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id","CodigoDTC","Descripcion")

codigofallo_schema = CodigoFallos()
codigofallos_schema = CodigoFallosSchema(many=True)