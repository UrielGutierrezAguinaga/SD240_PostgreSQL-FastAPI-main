import orm.modelos as modelos
from sqlalchemy.orm import Session


#Esta funcion es llamada por api.py
#para atender GET '/usuarios/{id}'
#select * from app.usuarios 
def usuario_por_id(sesion:Session,id_usuario:int):
    print("select * from app.usuarios where id =",id_usuario)
    return sesion.query(modelos.Usuario).filter(modelos.Usuario.id==id_usuario).first()

def compras_por_id(sesion:Session,id_usuario:int):
    print("select * from app.compras where id =",id_usuario)
    return sesion.query(modelos.Compras).filter(modelos.Compras.id==id_usuario).first()

def fotos_por_id(sesion:Session,id_usuario:int):
    print("select * from app.fotos where id =",id_usuario)
    return sesion.query(modelos.Fotos).filter(modelos.Fotos.id==id_usuario).first()

