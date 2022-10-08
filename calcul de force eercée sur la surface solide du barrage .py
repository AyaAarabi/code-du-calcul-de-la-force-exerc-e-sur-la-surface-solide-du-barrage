P=float(input("entrez la valeur de la pression: "))
L=float(input("entrez la valeur de la largeur: " ))
l= float(input("entrez la valeur de longeur "))
try:
    S=L*l
    F=S*P
    print("la valeur de la force exercée sur la surface du barrage est:",F)
except:
    print("la valeur que vous avez donnée de pression ou/et de S est incorrect")