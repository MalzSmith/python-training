# Feladatleírás
# A feladat egy 'masodfoku' nevű függvény elkészítése, ami paraméterül megkapja egy másodfokú egyenlet együtthatóit és visszatérési értéke pedig a másodfokú egyenlet megoldásai közül a nagyobbik
# Pl. ha másodfokú egyenletem az x^2 - 15x + 50 = 0 , akkor a = 1, b = -15, c = 0 , és a függvény visszatérési értéke az 10

# Gyököt vonni a math.sqrt() függvénnyel lehet

# Feladat megoldása:

from math import sqrt

def masodfoku(a, b, c):
    pass







# TESZTEK -------------------------------------------------------------------------------------------------------------------------------------------------
# A vonal alatt ne szerkeszd a kódot
# Az itt lévő kód teszteli a fenti megoldás helyességét

from pytest import approx

def test1():
    assert masodfoku(1, -15, 50) == approx(10)
def test2():
    assert masodfoku(2, -4, -30) == approx(5)
def test3():
    assert masodfoku(1, 3, 0) == approx(0)
def test4():
    assert masodfoku(1, 12, -45) == approx(3)