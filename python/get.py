

class Humain:
    def __init__(self,nom,age):
        print("Creation d'un humain")
        self.nom = nom
        self._age = age
    def _getage(self):

            if self._age <= 1:
                return "{} {}".format(self._age,"an")
            else:
                return "{} {}".format(self._age,"ans")
    age = property(_getage)


h1= Humain("Roberto", 1)
print("{0} à {1}".format(h1.nom,h1.age))


