import clase

def test_hola_mundo():
    assert clase.saludo("Ricardo") == "hola mundo"
    assert clase.saludo(5) == "hola mundo"  
    assert clase.saludo("mundo") == "hola mundo"

def test_suma():
    assert clase.suma(9,2) == 11
    assert clase.suma(9,3) == 11
    assert clase.suma() == 11
    assert clase.suma("a") == 11

def test_raiz_cuadrada():
    #assert clase.raiz_cuadrada(-1) == 2 #bota error de dominio
    #assert clase.raiz_cuadrada(4) == 2
    assert clase.raiz_cuadrada("a") == 2 #bota error de número real, no str