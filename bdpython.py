import sqlite3
import getpass
"""
conn = sqlite3.connect("miaplicacion.db")

cursor = conn.cursor()

rows = cursor.execute("select * from usuarios")
for row in rows:
    print(row)

cursor.close()
conn.close()"""

def main():
    nombre=input("nombre del usuario: ")
    telefono=getpass.getpass("telefono del usuario: ")
    if verificar_credenciales(nombre,telefono):
        print("login correcto")
    else:
        print("login fallido")


def verificar_credenciales(nombre, telefono):
    conn = sqlite3.connect("miaplicacion.db")
    cursor= conn.cursor()
    query=f"SELECT id FROM usuarios WHERE nombre='{nombre}' AND telefono='{telefono}'"
    
    rows = cursor.execute(query)
    data = rows.fetchone()
    cursor.close()
    conn.close()
    
    if data== None:
        return False
    return True
def crearusuario(id, nombre, telefono):
    conn = sqlite3.connect("miaplicacion.db")
    cursor= conn.cursor()
    query=f"Insert into usuarios(id,nombre,telefono) VALUES(3,'Christian', '123456789')"
    
    rows = cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()
    
if __name__ == '__main__':
    main()