#Creer un classe banque  et permettre à utilisateur d'ajouter   ou retirer un montant
# à des cleints.
#permettre à utilisateur  d'ajouter des clients et aussi des montants à ces cleints
#dite au programme de demande à utilisateur de continuer ou arrete puis afficher la liste des clients de la banque


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
        print("{0} : {1}$ en banque".format(self.nom,self.balance))
clients={}
continuer ="o"
while continuer == "o":
    nom = input("Saisissez le nom du client: ")
    montant = input("saisissez son solde de depart :")

    clients[nom]= Banque()
    clients[nom].nom = nom
    clients[nom].balance = montant

    continuer = input("voulez vous ajouter un autre client ? o/n ")
    print("")
print("")
print("Voici la liste des cliente de votre Banque")
for client in clients.values():
    print("{0} : {1} en banque".format(client.nom, client.balance))