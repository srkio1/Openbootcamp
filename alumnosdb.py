import sqlite3

def main():
    buscarAlumno("Carlos","Ruiz")
    
def main2():
    crearusuario(1,"Carlos","Ruiz")
    crearusuario(2,"Nombre2","Apellido2")
    crearusuario(3,"Nombre3","Apellido3")
    crearusuario(4,"Nombre4","Apellido4")
    crearusuario(5,"Nombre5","Apellido5")
    crearusuario(6,"Nombre6","Apellido6")
    crearusuario(7,"Nombre7","Apellido7")
    crearusuario(8,"Nombre8","Apellido8")
        

def crearusuario(id, nombre, apellido):
    conn = sqlite3.connect("miaplicacion.db")
    cursor= conn.cursor()
    query='''Insert into Alumnos(id,nombre,apellido) VALUES(?,?, ?)'''
    
    rows = cursor.execute(query,(id,nombre,apellido))
    conn.commit()
    cursor.close()
    conn.close()

def buscarAlumno(nombre, apellido):
    conn = sqlite3.connect("miaplicacion.db")
    cursor= conn.cursor()
    query=f"SELECT * FROM Alumnos WHERE nombre='{nombre}' AND apellido='{apellido}'"
    
    rows = cursor.execute(query)    
    data = rows.fetchone()
    print(data)
    cursor.close()
    conn.close()
    
    if data== None:
        return False
    return True

        
if __name__ == '__main__':
    main()

