import math

def saludo(name = "mundo"):
    return f"hola {name}"


def suma(a=5,b=6): # se le da estos valores para que no reasigne
    return a + b

# los test permiten saber para qué valores se revienta la función

def raiz_cuadrada(numero):
    try:
        return math.sqrt(numero)
    except ValueError:
        return "error, no se puede calcular raíz cuadrada de", f"{numero}"
    except TypeError:
        return "error, no se puede calcular raíz cuadrada de", f"{numero}"

print(raiz_cuadrada("a"))




