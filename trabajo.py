#obtener la hora del sistema?
from datetime import datetime
import time

formato = "%H:%M:%S"



    
    


for i in range(3600):
    hora=datetime.now().strftime("%H:%M:%S")
    salida = "20:00:00"
    h1=datetime.strptime(hora, formato)
    h2=datetime.strptime(salida, formato)
    

    r = h2 - h1
    if h1<h2:
        print(f"Aun falta {r} horas para salir del trabajo")
    else:
        print(f"Ya es hora de salir del trabajo{r}")
    time.sleep(1)
        
        
    
    

    








