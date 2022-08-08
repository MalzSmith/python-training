# Feladatleírás
# A feladat egy 'oszthato' nevű függvény elkészítése, ami paraméterül kap kettő számot és True/False értéket ad vissza attól függően, hogy a második szám osztója-e az első számnak


# Feladat megoldása:

def oszthato(a, b):
    return False






# TESZTEK -------------------------------------------------------------------------------------------------------------------------------------------------
# A vonal alatt ne szerkeszd a kódot
# Az itt lévő kód teszteli a fenti megoldás helyességét

def test1():
    assert not oszthato(10, 3)
def test2():
    assert oszthato(0, 10)
def test3():
    assert oszthato(2, 1)
def test4():
    assert not oszthato(50, 11)
def test5():
    assert oszthato(104329, 17)
