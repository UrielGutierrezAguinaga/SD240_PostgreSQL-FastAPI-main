from orm.config import BaseClass
#esta clase hereda o es la clase base de los modelos 
#los modelos o clases modelo son las clases que mapean a las tablas 
#importar de AQLAlquemy los tipos de datos que usan las tabblas
from sqlalchemy  import Column, String, Integer, DateTime, ForeignKey, Float
#para calcular la hora actual
import datetime 

class Usuario(BaseClass):
    __tablename__="usuarios"
    id=Column(Integer,primary_key=True)
    nombre=Column(String(100))
    edad=Column(Integer)
    domicilio= Column(String(200))
    email= Column("email",String(100))
    password= Column(String(40))
    fecha_registro=Column(DateTime(timezone= True),default=datetime.datetime.now)

    
class Compras(BaseClass):
    __tablename__="compras"
    id=Column(Integer,primary_key=True)
    id_usuario=Column(Integer,ForeignKey(Usuario.id))
    producto=Column(String(100))
    precio=Column(Float(100))
    
   
class Fotos(BaseClass):
    __tablename__="fotos"
    id=Column(Integer,primary_key=True)
    id_usuario=Column(Integer,ForeignKey(Usuario.id))
    titulo=Column(String(100))
    descripcion= Column(String(100))
    ruta= Column(String(50))
   
        
    