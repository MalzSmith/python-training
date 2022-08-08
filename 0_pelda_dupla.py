# Feladatleírás
# A feladat egy 'dupla' nevű függvény elkészítése, ami visszaadja a paraméterül kapott szám kétszeresét


# Feladat megoldása:

def dupla(a):
    return a * 2



# TESZTEK -------------------------------------------------------------------------------------------------------------------------------------------------
# A vonal alatt ne szerkeszd a kódot
# Az itt lévő kód teszteli a fenti megoldás helyességét

def test1():
    assert dupla(1) == 2
def test2():
    assert dupla(10) == 20
def test3():
    assert dupla(-2) == -4
def test4():
    assert dupla(0) == 0