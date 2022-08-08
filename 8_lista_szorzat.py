# Feladatleírás
# A feladat egy 'lista_szorzat' nevű függvény elkészítése, ami paraméterül kap egy számokat tartalmazó listát és visszatérési értéke pedig a listában lévő számok összege


# Feladat megoldása:

def lista_szorzat(lista):
    pass







# TESZTEK -------------------------------------------------------------------------------------------------------------------------------------------------
# A vonal alatt ne szerkeszd a kódot
# Az itt lévő kód teszteli a fenti megoldás helyességét

def test1():
    assert lista_szorzat([1,2,3,4]) == 24
def test2():
    assert lista_szorzat([1]) == 1
def test3():
    assert lista_szorzat([1,-2,-3,-4]) == -24
def test4():
    assert lista_szorzat([100, -100]) == -10000
def test5():
    assert lista_szorzat([0,0,0,0,0]) == 0