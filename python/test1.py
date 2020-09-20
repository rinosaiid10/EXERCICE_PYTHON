

class Humain:

    def __init__(self,nom,age):
        print("creation d'un humain")
        self.nom = "Jojo"
        self.age = 10

    def _getage (self):
        return  self._age

    def _getage (self,nouvel_age):
        if nouvel_age >0:
            self._age = 0
        else:
            self._age =nouvel_age

    age =property(_getage)

print("Lancement du programme")
h1= Humain("Jojo",24)
int(h1.age)
h1.age = 0
