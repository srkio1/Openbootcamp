#obtener la hora del sistema?
from datetime import datetime
import time

formato = "%H:%M:%S"
hora=datetime.now().strftime("%H:%M:%S")
salida = "19:00:00"

h1=datetime.strptime(hora, formato)
h2=datetime.strptime(salida, formato)
    

r = h2 - h1
    
    
print(f"Aun faltan {r} para salir del trabajo")
    
        
        
    
    

    








