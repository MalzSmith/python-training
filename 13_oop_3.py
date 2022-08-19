# A feladat 3 osztály elkészítése:

# Ember: Az embernek van neve és azonosító száma. Ezeket konstruktorban kapja meg (ilyen sorrendben).
# Diak: A Diak az Ember osztályból származik, van még neki egy beiratkozási éve
# Tanár: A Tanár az Ember-ből származik. Tartoznak hozzá diákok, ezt egy listában tárolja. Van neki még egy 'legregebbi' nevű függvénye, ami visszaadja a legkorábban kezdett diákjának a nevét. (Feltéve, hogy a legkorábbi évben csak egy diákja kezdett)


class Ember():
    def __init__(self, nev, azonosito) -> None:
        self.nev = nev
        self.azonosito = azonosito

class Diak(Ember):
    def __init__(self, nev, azonosito, beiratkozas) -> None:
        super().__init__(nev, azonosito)
        self.beiratkozas = beiratkozas

class Tanar(Ember):
    def __init__(self, nev, azonosito, diakok) -> None:
        super().__init__(nev, azonosito)
        self.diakok = diakok
    def legregebbi(self):
        res = self.diakok[0]
        m = self.diakok[0].beiratkozas
        for d in self.diakok:
            if d.beiratkozas < m:
                res = d
                m = d.beiratkozas
        return res.nev


# TESZTEK -------------------------------------------------------------------------------------------------------------------------------------------------
# A vonal alatt ne szerkeszd a kódot
# Az itt lévő kód teszteli a fenti megoldás helyességét

from pytest import approx

def test():
    try:
        a = Diak("Peti", 123, 2005)
        b = Diak("BBB", 111, 2004)
        c = Diak("CCC", 222, 2007)
        d = Diak("DDD", 331, 2001)

        diakok = [a,b,c,d]
        t = Tanar("Pista bacsi", 530, diakok)

        assert t.legregebbi() == "DDD"
    except:
        assert False

