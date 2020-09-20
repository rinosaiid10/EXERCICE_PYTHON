"""
-Récupérer ce que saisit l'utilisateur.
-Tester si c'est un nombre.
-Si oui,continuer,afficher la table de mutliplication et demander à l'utilisateur
s'il souhaite quitter le programe ou non.
-si utilisagteur saisit autre qu'un nobre (si non),arreter la boucle et  demander à l'utilisateur de saisir un nombre
"""
oquitter=""
while oquitter !="o":
    oinput = input("Svp,entrez un nombre : ")

    obool= oinput.isdigit()
    if obool== True: # on peut aussi ecrire if obool:
        oinput=int(oinput) #on peut supprimer la ligne precedente et ecrire if  oinput.isdigit()
        for i in range(11):
            print(str(i)+ "*" +str(oinput) +"="+str(i* oinput))

        oquitter= input("voulez vous quitter le programme o/n ")
    elif obool==False: #et aussi remplacer par elif not oinput.isdigit()
        print("Erreur vous n'avez pas entre de nombre !")

