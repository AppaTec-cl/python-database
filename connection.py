from pymysql import *

class DataBase:
    def __init__(self):
        self.conector = connect(
            host='sql10.freesqldatabase.com',
            user='sql10704330',
            password='RdCRy6aVhV',
            db='sql10704330')
        self.cursor = self.conector.cursor()
        print("Conectado!!")


class DAO(DataBase):
    def __init__(self):
        super().__init__()

    def verUsuario(self, id):
        sql = "SELECT usuario.id_usuario, usuario.rut, usuario.nombre, usuario.apellido_p, usuario.apellido_m, usuario.email, usuario.password, usuario.rol FROM usuario WHERE usuario.id_usuario = '"+str(id)+"'"
        try:
            self.cursor.execute(sql)
            resultado = self.cursor.fetchone()
            if resultado != None:
                print("    Id               : ",resultado[0])
                print("    Rut              : ",resultado[1])
                print("    Nombre           : ",resultado[2])
                print("    Apellido Paterno : ",resultado[3])
                print("    Apellido Materno : ",resultado[4])
                print("    Email            : ",resultado[5])
                print("    Password         : ",resultado[6])
                print("    Rol              : ",resultado[7])
                print("")
            else:
                print("Usuario no existente en los registros")
        except Exception as e:
            print("Error: ",str(e.args))

    def verUsuarios(self):
        sql = "SELECT usuario.id_usuario, usuario.rut, usuario.nombre, usuario.apellido_p, usuario.apellido_m, usuario.email, usuario.password, usuario.rol FROM usuario"
        try:
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()
            if len (resultado) == 0:
                print("No hay Usuarios")
            else:
                for obj in resultado:
                    print("    Id               : ",obj[0])
                    print("    Rut              : ",obj[1])
                    print("    Nombre           : ",obj[2])
                    print("    Apellido Paterno : ",obj[3])
                    print("    Apellido Materno : ",obj[4])
                    print("    Email            : ",obj[5])
                    print("    Password         : ",obj[6])
                    print("    Rol              : ",obj[7])
                    print("")
        except Exception as e:
            print("Error: ",str(e.args))

    def verHistorial(self):
        sql = "SELECT historial_contrato.id_historial_contrato, historial_contrato.id_contrato, historial_contrato.estado_anterior, historial_contrato.estado_nuevo, historial_contrato.fecha_cambio FROM historial_contrato"
        try:
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()
            if len (resultado) == 0:
                print("No hay Registros en el Historial")
            else:
                for obj in resultado:
                    print("    Id               : ",obj[0])
                    print("    Id del Contrato  : ",obj[1])
                    print("    Estado Anterior  : ",obj[2])
                    print("    Estado Nuevo     : ",obj[3])
                    print("    Apellido Materno : ",obj[4])
                    print("    Fecha de Cambio  : ",obj[5])
                    print("")
        except Exception as e:
            print("Error: ",str(e.args))
    
    def verContrato(self):
        sql = "SELECT contrato.id_contrato, contrato.id_usuario_trabajador, contrato.fecha_inicio, contrato.fecha_expiracion, contrato.tipo_contrato, contrato.contenido_contrato, contrato.estado, contrato.comentario FROM contrato"
        try:
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()
            if len (resultado) == 0:
                print("No hay Registros de Contratos")
            else:
                for obj in resultado:
                    print("    Id                      : ",obj[0])
                    print("    Id del Usuario          : ",obj[1])
                    print("    Fecha Inicio            : ",obj[2])
                    print("    Fecha Expiracion        : ",obj[3])
                    print("    Tipo de Contrato        : ",obj[4])
                    print("    Contenido del Contrato  : ",obj[5])
                    print("    Estado del Contrato     : ",obj[6])
                    print("    Comentario del Contrato : ",obj[7])
                    print("")
        except Exception as e:
            print("Error: ",str(e.args))

    def agregarUsuario(self, id, rut, nombre, apellido_p, apellido_m, email, password, rol):
        sql = "INSERT INTO usuario (id_usuario, rut, nombre, apellido_p, apellido_m, email, password, rol) VALUES ('"+str(id)+"','"+rut+"','"+nombre+"','"+apellido_p+"','"+apellido_m+"','"+email+"','"+password+"','"+rol+"')"
        msg = "Usuario agregado"
        try:
            self.cursor.execute(sql)
            self.conector.commit()
        except Exception as e:
            msg = "Error: ",str(e.args)
        
        return msg


a1 = DAO()


