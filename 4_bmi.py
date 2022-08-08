# Feladatleírás
# A feladat egy 'bmi' nevű függvény elkészítése, ami paraméterül megkapja egy ember magasságát (m) és a tömegét (kg) és ezekből kiszámolja a testtömeg indexét.

# A testtömeg index kiszámítható a tomeg/(magassag*magassag) képlettel

# Feladat megoldása:

def bmi(magassag, tomeg):
    return 1








# TESZTEK -------------------------------------------------------------------------------------------------------------------------------------------------
# A vonal alatt ne szerkeszd a kódot
# Az itt lévő kód teszteli a fenti megoldás helyességét

from pytest import approx

def test1():
    assert bmi(1.8,95) == approx(29.3, .1)
def test2():
    assert bmi(1.7, 110) == approx(38, .1)
def test3():
    assert bmi(1.85,75) == approx(21.9, .1)
def test4():
    assert bmi(2,75) == approx(18.7, .1)