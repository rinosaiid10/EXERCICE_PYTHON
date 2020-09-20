import random

nombre_p = random.randint(1,10)
print(nombre_p)
nombre_u = 0
while nombre_u != nombre_p:
    nombre_txt = input("Entrez votre nombre:")
    nombre_u = int(nombre_txt)

    if nombre_p > nombre_u:
        print("C'est plus")
    elif nombre_p < nombre_u:
        print("C'est moins")
    else:
        print ("Bravo , vous avez trouvé le nombre")