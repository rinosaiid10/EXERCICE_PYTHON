
class Banque:
    def __init__(self):
        self.nom=""
        self.balance =0
    def ajouter_argent (self,montant):
        self.balance +=montant
        print("vous avez ajoute {0} $  au compte en banque de {1}".format(montant,self.nom))

    def retirer_argent(self, montant):
        self.balance -= montant
        print("vous avez retirer {0} $  au compte en banque de {1}".format(montant, self.nom))
    def afficher_balance (self):
        print("{0} à {1}$".format(self.nom,self.balance))

client_01 = Banque()
client_01.nom= "Pierre"

client_02 = Banque()
client_02.nom = "Jacque"

client_03= Banque()
client_03.nom ="Paul"

client_01.ajouter_argent(50)
client_02.ajouter_argent(30)
client_03.ajouter_argent(60)

client_03.retirer_argent(20)
client_03.afficher_balance()