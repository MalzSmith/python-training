# Feladatleírás
# A feladat egy 'Jarmu' nevű osztály elkészítése. Ennek az osztálynak legyen egy sebesség és egy rendszám tulajdonsága, amiket konstruktorban megkap.
# Ezen kívül feladat egy 'Ember' nevű osztály létrehozása. az ember konstruktorban kapjon egy járműlistát, amit tároljon, illetve legyen egy 'rendszamok' nevű függvénye, ami visszaadja a hozzá tartozó járművek rendszámának listáját


# Feladat megoldása:

class Jarmu():
    def __init__(self, sebesseg : int, rendszam : str) -> None:
        self.sebesseg = sebesseg
        self.rendszam = rendszam

class Ember():
    def __init__(self, birtokolt_jarmuvek) -> None:
        self.birtokolt_jarmuvek = birtokolt_jarmuvek
    def rendszamok(self):
        rendszamok = []
        for jarmu in self.birtokolt_jarmuvek:
            rendszamok.append(jarmu.rendszam)
        return rendszamok








# TESZTEK -------------------------------------------------------------------------------------------------------------------------------------------------
# A vonal alatt ne szerkeszd a kódot
# Az itt lévő kód teszteli a fenti megoldás helyességét

def test():
    try:
        a = Jarmu(100, 'ABC123')
        b = Jarmu(100, 'AAA111')
        c = Jarmu(100, 'BBB222')
        d = Jarmu(100, 'CCC333')
        jarmuvek = [a,b,c,d]
        a = Ember(jarmuvek)
        rendszamok = a.rendszamok()
        assert len(rendszamok) == len(jarmuvek)
        for j in jarmuvek:
            assert j.rendszam in rendszamok
    except:
        assert False

