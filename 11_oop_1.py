# Feladatleírás
# A feladat egy 'Ember' nevű osztály elkészítése. Ennek az osztálynak legyen neve, magassága (méterben) és tömege (kg-ban). Ezeket konstruktorban kapja meg (ilyen sorrendben).
# Legyen egy 'bmi' nevű függvénye, ami visszaadja az ember testtömegindexét.


# Feladat megoldása:








# TESZTEK -------------------------------------------------------------------------------------------------------------------------------------------------
# A vonal alatt ne szerkeszd a kódot
# Az itt lévő kód teszteli a fenti megoldás helyességét

from pytest import approx

def test():
    try:
        a = Ember("Peti", 1.8, 95)
        assert a.bmi() == approx(29.3, .1)
        assert Ember("", 1.7, 110).bmi() == approx(38, .1)
        assert Ember("", 1.85,75).bmi() == approx(21.9, .1)
        assert Ember("", 2,75).bmi() == approx(18.7, .1)
    except:
        assert False

