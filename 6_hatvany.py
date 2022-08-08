# Feladatleírás
# A feladat egy 'hatvany' nevű függvény elkészítése, ami paraméterül kap kettő számot és visszatérési értéke pedig az első szám a második számra emelve (pl ha a megadott számok 3 és 4, akkor a visszatérési érték 81)


# Feladat megoldása:

def hatvany(a, b):
    pass







# TESZTEK -------------------------------------------------------------------------------------------------------------------------------------------------
# A vonal alatt ne szerkeszd a kódot
# Az itt lévő kód teszteli a fenti megoldás helyességét

def test1():
    assert hatvany(1, 10) == 1
def test2():
    assert hatvany(0, 100) == 0
def test3():
    assert hatvany(2, 16) == 65536
def test4():
    assert hatvany(-1, 3) == -1
def test5():
    assert hatvany(5, 0) == 1