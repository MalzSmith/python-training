# Feladatleírás
# A feladat egy 'osszeg' nevű függvény elkészítése, ami paraméterül kap kettő számot és ezeket összeadja. A visszatérési érték a két szám összege legyen.


# Feladat megoldása:

def osszeg(a, b):
    eredmeny = a + b
    return eredmeny

# TESZTEK -------------------------------------------------------------------------------------------------------------------------------------------------
# A vonal alatt ne szerkeszd a kódot
# Az itt lévő kód teszteli a fenti megoldás helyességét

def test1():
    assert osszeg(1,1) == 2
def test2():
    assert osszeg(1,10) == 11
def test3():
    assert osszeg(1,-9) == -8
def test4():
    assert osszeg(0,-12) == -12