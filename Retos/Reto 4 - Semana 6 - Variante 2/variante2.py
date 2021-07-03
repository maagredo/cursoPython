#NO ELIMINAR LA SIGUIENTE IMPORTACIÓN, sirve para probar tu código en consola
#from pruebas import pruebas_codigo_estudiante
"""NOTAS: 
    -PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
    -LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO
"""


"""Inicio espacio para programar funciones propias"""
#En este espacio podrás programar las funciones que deseas usar en la función solución (ES OPCIONAL


"""Fin espacio para programar funciones propias"""

def actualizar_estado_editor(operaciones_usuario):
    #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.
    
    """
    texto_escrito=[] 
    texto_actual = ""
    rehacer=[]
    contador=0
    cadena_final=""

    for i in operaciones_usuario:
        if i =="DESHACER":
            rehacer.append(texto_actual)
            texto_actual = texto_escrito.pop()
            contador=contador-1
        elif i =="REHACER":
            texto_escrito.append(texto_actual)
            texto_actual=rehacer.pop()
            contador=contador+1
        elif texto_actual=="":
            texto_actual=i        
        else:
            texto_escrito.append(texto_actual)
            texto_actual=i
            contador=contador +1    
        
    for i in range(contador):
        cadena_final+=texto_escrito[i]
    """
    """
    contador2=contador
    cadena=[]
    while contador>0:        
        cadena.append(texto_escrito.pop())        
        contador=contador-1
    while contador2>0:
        cadena_final+=cadena.pop()
        contador2=contador2-1
    """
    
    texto_escrito = []
    rehacer = []
    texto_actual = ""
    cadena = ""

    for i in operaciones_usuario:
        if i != 'DESHACER' and i != 'REHACER':
            texto_escrito.append(texto_actual)
            texto_actual = i
            rehacer.clear()

        if i == 'DESHACER':
            rehacer.append(texto_actual)
            texto_actual = texto_escrito.pop()

        if i == 'REHACER':
            texto_escrito.append(texto_actual)
            texto_actual = rehacer.pop()
    for i in range(len(texto_escrito)):
        cadena += texto_escrito[i]
    
    cadena_final = cadena + texto_actual
            
    print(cadena_final)

"""
NO PEDIR DATOS CON LA FUNCIÓN input(), NO COLOCAR CÓDIGO FUERA DE LAS FUNCIONES QUE USTED CREE
Esta línea de código que sigue, permite probar si su ejercicio es correcto
Por favor NO ELIMINARLA, NO MODIFICARLA
"""
"""
operaciones_usuario = ["Definamos qué es una función de Python: ",
"Una función es ","un arreglo unidimensional de datos",
"DESHACER", "DESHACER", "REHACER",
"un grupo de instrucciones"]


actualizar_estado_editor(operaciones_usuario)"""