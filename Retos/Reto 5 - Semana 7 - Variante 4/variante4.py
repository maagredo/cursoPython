#NO ELIMINAR LAS SIGUIENTES IMPORTACIONES, sirven para probar tu código en consola, y el funcionamiento del módulo csv respectivamente
from pruebas import pruebas_codigo_estudiante
import csv
"""NOTAS: 
    -PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
    -LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO
"""


"""Inicio espacio para programar funciones propias"""
#En este espacio podrás programar las funciones que deseas usar en la función solución (ES OPCIONAL)



"""Fin espacio para programar funciones propias"""

def solucion():
    #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.
    csvsalida = open("analisis_archivo.csv", 'w', newline='')    
    salida = csv.writer(csvsalida, delimiter='\t')
    header=['Fecha','Mean-Min-Max','Concepto']
    salida.writerow(header)

    with open("archivos\FB_2.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        
        lowest_mean=0
        for row in reader:
            if lowest_mean==0:
                prom=(float(row['High'])+float(row['Low']))/2     
                lowest_mean=prom
                highest_mean=prom
                date_lowest_mean=row['Date']
                date_highest_mean=row['Date']
            else:
                prom=(float(row['High'])+float(row['Low']))/2     
            if prom < 239:
                cadena="MUY BAJO"
            elif prom >= 239 and prom < 265:
                cadena="BAJO"
            elif prom >= 265 and prom < 291:
                cadena="MEDIO"
            elif prom >= 291 and prom < 317:
                cadena="ALTO"
            else:
                cadena="MUY ALTO"

            data=[row['Date'],prom,cadena]
            salida.writerow(data)
            if lowest_mean>prom:            
                date_lowest_mean=row['Date']
                lowest_mean=prom
            if highest_mean<prom:
                highest_mean=prom
                date_highest_mean=row['Date']

    csvfile.close()

    return date_lowest_mean, lowest_mean, date_highest_mean, highest_mean

"""
NO COLOCAR CÓDIGO FUERA DE LAS FUNCIONES QUE USTED CREE
Esta línea de código que sigue permite saber si su solución al ejercicio es correcto
Por favor NO ELIMINARLA, NO MODIFICARLA
"""
pruebas_codigo_estudiante(solucion)