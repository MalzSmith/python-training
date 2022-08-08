# Feladatleírás
# A feladat egy 'lista_max' nevű függvény elkészítése, ami paraméterül kap egy számokat tartalmazó listát és visszatérési értéke pedig a listában lévő számok összege
# Ne használd a max függvényt ha lehet


# Feladat megoldása:

def lista_max(lista):
    pass






# TESZTEK -------------------------------------------------------------------------------------------------------------------------------------------------
# A vonal alatt ne szerkeszd a kódot
# Az itt lévő kód teszteli a fenti megoldás helyességét

def test1():
    assert lista_max([1,2,3,4]) == 4
def test2():
    assert lista_max([1]) == 1
def test3():
    assert lista_max([1,2,-3,-4]) == 2
def test4():
    assert lista_max([100, -100]) == 100
def test5():
    assert lista_max([0,0,0,0,0]) == 0
def test6():
    assert lista_max([-1, -2, -3]) == -1