#NO ELIMINAR LA SIGUIENTE IMPORTACIÓN, sirve para probar tu código en consola
#from pruebas import pruebas_codigo_estudiante

#NOTA: PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
#LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO

#En este espacio podrás programar las funciones que deseas usar en la función solución (NO ES OBLIGATORIO CREAR OTRAS FUNCIONES)
"""Inicio espacio para programar funciones propias"""



#PUEDES PROGRAMAR CUANTAS FUNCIONES DESEES 

mensaje_a_traducir="hole mundo"
"""Fin espacio para programar funciones propias"""

def traductor_a_morse(mensaje_a_traducir):
    #PROGRAMA ACÁ TU SOLUCIÓN
    
    mensaje_a_traducir=mensaje_a_traducir.upper()
    print(mensaje_a_traducir)
    abecedario={"A":".-",
    "B":"-...",
    "C":"-.-.",
    "D":"-..",
    "E":".",
    "F":"..-.",
    "G":"--.",
    "H":"....",
    "I":"..",
    "J":".---",
    "K":"-.-",
    "L":".-..",
    "M":"--",
    "N":"-.",
    "O":"---",
    "P":".--.",
    "Q":"--.-",
    "R":".-.",
    "S":"...",
    "T":"-",
    "U":"..-",
    "V":"...-",
    "W":".--",
    "X":"-..-",
    "Y":"-.--",
    "Z":"--..",
    " ":"/"}
    
    mensaje_traducido=""
    
    for i in mensaje_a_traducir:
          mensaje_traducido+=abecedario[i]+" "        
     
    
    return mensaje_traducido.strip()

"""
Esta línea de código que sigue, permite probar si su ejercicio es correcto
"""
#NO ELIMINAR LA SIGUIENTE LÍNEA DE CÓDIGO
# pruebas_codigo_estudiante(traductor_a_morse)
traductor_a_morse(mensaje_a_traducir)