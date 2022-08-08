# Feladatleírás
# A feladat egy 'lista_osszeg' nevű függvény elkészítése, ami paraméterül kap egy számokat tartalmazó listát és visszatérési értéke pedig a listában lévő számok összege


# Feladat megoldása:

def lista_osszeg(lista):
    eredmeny = 0
    for szam in lista:
        eredmeny = eredmeny + szam
    return eredmeny







# TESZTEK -------------------------------------------------------------------------------------------------------------------------------------------------
# A vonal alatt ne szerkeszd a kódot
# Az itt lévő kód teszteli a fenti megoldás helyességét

def test1():
    assert lista_osszeg([1,2,3,4]) == 10
def test2():
    assert lista_osszeg([1]) == 1
def test3():
    assert lista_osszeg([1,2,-3,-4]) == -4
def test4():
    assert lista_osszeg([100, -100]) == 0
def test5():
    assert lista_osszeg([0,0,0,0,0]) == 0