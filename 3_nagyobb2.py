# Feladatleírás
# A feladat egy 'legnagyobb' nevű függvény elkészítése, ami paraméterül kap három számot és visszaadja a nagyobbat.


# Feladat megoldása:


def legnagyobb(a, b, c):
    pass







# TESZTEK -------------------------------------------------------------------------------------------------------------------------------------------------
# A vonal alatt ne szerkeszd a kódot
# Az itt lévő kód teszteli a fenti megoldás helyességét



def test1():
    assert legnagyobb(1, 1, 10) == 10
def test2():
    assert legnagyobb(1, -10, -5) == 1
def test3():
    assert legnagyobb(0, 0, 0) == 0
def test4():
    assert legnagyobb(10, 0, 3) == 10
def test5():
    assert legnagyobb(-10, -9, -10) == -9

