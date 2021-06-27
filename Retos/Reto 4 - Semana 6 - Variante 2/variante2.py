#NO ELIMINAR LA SIGUIENTE IMPORTACIÓN, sirve para probar tu código en consola
#from pruebas import pruebas_codigo_estudiante
"""NOTAS: 
    -PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
    -LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO
"""


"""Inicio espacio para programar funciones propias"""
#En este espacio podrás programar las funciones que deseas usar en la función solución (ES OPCIONAL
class Stack: 
    def __init__(self):
        self.items = []
#Metodo para insertar elementos en la pila
    def push(self,item):
        self.items.append(item)

"""Fin espacio para programar funciones propias"""

def actualizar_estado_editor(operaciones_usuario):
    #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.
    texto_escrito=Stack() 
    texto_actual = ""
    rehacer=Stack()
    contador=0
    cadena_final=""
    for i in operaciones_usuario:
        if i =="DESHACER":
            rehacer.push(texto_actual)
            texto_actual = texto_escrito.items.pop()
            contador=contador-1
        elif i =="REHACER":
            texto_escrito.push(texto_actual)
            texto_actual=rehacer.items.pop()
            contador=contador+1
        elif texto_actual=="":
            texto_actual=i        
        else:
            texto_escrito.push(texto_actual)
            texto_actual=i
            contador=contador +1    
        
    contador2=contador
    cadena=Stack()
    while contador>0:        
        cadena.push(texto_escrito.items.pop())        
        contador=contador-1
    while contador2>0:
        cadena_final+=cadena.items.pop()
        contador2=contador2-1

        
    print(cadena_final+texto_actual)

"""
NO PEDIR DATOS CON LA FUNCIÓN input(), NO COLOCAR CÓDIGO FUERA DE LAS FUNCIONES QUE USTED CREE
Esta línea de código que sigue, permite probar si su ejercicio es correcto
Por favor NO ELIMINARLA, NO MODIFICARLA
"""

operaciones_usuario = ["Definamos qué es una función de Python: ",
"Una función es ","un arreglo unidimensional de datos",
"DESHACER", "DESHACER", "REHACER", "un grupo de instrucciones"]


actualizar_estado_editor(operaciones_usuario)