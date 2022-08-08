# Feladatleírás
# A feladat egy 'paros' nevű függvény elkészítése, ami paraméterül kap egy számot és True/False értéket ad vissza attól függően, hogy a megadott szám páros-e.


# Feladat megoldása:

def paros(a):
    eredmeny = a % 2 == 0
    return eredmeny







# TESZTEK -------------------------------------------------------------------------------------------------------------------------------------------------
# A vonal alatt ne szerkeszd a kódot
# Az itt lévő kód teszteli a fenti megoldás helyességét

def test1():
    assert not paros(1)
def test2():
    assert paros(0)
def test3():
    assert paros(2)
def test4():
    assert not paros(-1)
def test5():
    assert paros(-2)