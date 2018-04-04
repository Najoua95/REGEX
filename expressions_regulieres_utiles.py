#entier positif sans limite de taille
nb = input("Votre nombre positif (sans limite) : ")
prog = re.compile(r"^\d+$")

while True :
    if prog.search(nb) is not None :
        print('nombre validé')
        break
    else :
        nb = input ("Saisissez un nombre positif : ")


#entier positif avec une taille limite de 10 chiffres
nb = input('Votre nombre positif entre 1 et 10 chiffres: ')
prog = re.compile(r"^\d{1,10}$")

while True :
    if prog.search(nb) is not None :
        print('nombre validé')
        break
    else :
        nb = input ("Saisissez un nombre positif entre 1 et 10 chiffres : ")


#entier positif avec taille fixe à 5
nb = input('Votre nombre positif de 5 chiffres : ')
prog = re.compile(r"^\d{5}$")

while True :
    if prog.search(nb) is not None :
        print('nombre validé')
        break
    else :
        nb = input ("Saisissez un nombre positif de 5 chiffres : ")

########################################################################
#entier relatif sans limite
nb = input("Votre nombre relatif (sans limite) : ")
prog = re.compile(r"^-\d+$")

while True :
    if prog.search(nb) is not None :
        print('nombre validé')
        break
    else :
        nb = input ("Saisissez un nombre relatif : ")


#entier relatif limité entre 1 et 10 chiffres
nb = input('Votre nombre relatif entre 1 et 10 chiffres: ')
prog = re.compile(r"^-\d{1,10}$")

while True :
    if prog.search(nb) is not None :
        print('nombre validé')
        break
    else :
        nb = input ("Saisissez un nombre relatif entre 1 et 10 chiffres : ")


#entier relatif limité à 5 chiffres
nb = input('Votre nombre relatif de 5 chiffres : ')
prog = re.compile(r"^-\d{5}$")

while True :
    if prog.search(nb) is not None :
        print('nombre validé')
        break
    else :
        nb = input ("Saisissez un nombre relatif de 5 chiffres : ")

#####################################################################################
#entier positif ou relatif sans limite
nb = input("Votre nombre positif ou relatif (sans limite) : ")
prog = re.compile(r"^-?\d+$")

while True :
    if prog.search(nb) is not None :
        print('nombre validé')
        break
    else :
        nb = input ("Saisissez un nombre relatif : ")

#entier positif ou relatif limité entre 1 et 10 chiffres
nb = input('Votre nombre positif ou relatif entre 1 et 10 chiffres: ')
prog = re.compile(r"^-?\d{1,10}$")

while True :
    if prog.search(nb) is not None :
        print('nombre validé')
        break
    else :
        nb = input ("Saisissez un nombre positif ou relatif entre 1 et 10 chiffres : ")

#entier positif ou relatif taille de 5 fixe
nb = input('Votre nombre positif ou relatif de 5 chiffres : ')
prog = re.compile(r"^-?\d{5}$")

while True :
    if prog.search(nb) is not None :
        print('nombre validé')
        break
    else :
        nb = input ("Saisissez un nombre poisitif ou relatif de 5 chiffres : ")

###############################################################################################
#un nombre : positif ou négatif avec ou sans des chiffres après la virgule.
nb = input('Votre nombre positif ou négatif avec ou sans virgule : ')
prog = re.compile(r"^-?\d+\,?\d?$")

while True :
    if prog.search(nb) is not None :
        print('nombre validé')
        break
    else :
        nb = input ("Saisissez un nombre poisitif ou relatif avec ou sans virgule : ")

#positif ou négatif avec 2 chiffres après la virgule.
nb = input('Votre nombre positif ou négatif avec 2 chiffres après la virgule : ')
prog = re.compile(r"^-?\d+\,\d{2}$")

while True :
    if prog.search(nb) is not None :
        print('nombre validé')
        break
    else :
        nb = input ("Saisissez un nombre poisitif ou relatif avec 2 chiffres après la virgule : ")

#nombre version américiane avec '.'
nb = input('Votre nombre (version us) : ')
prog = re.compile(r"^-?\d+[,|.]\d{2}$")

while True :
    if prog.search(nb) is not None :
        print('nombre validé')
        break
    else :
        nb = input ("Saisissez un nombre (version us) : ")

#un nombre qui peut ou non comporter le signe %
nb = input('Votre nombre : ')
prog = re.compile(r"^\d+\%?$")

while True :
    if prog.search(nb) is not None :
        print('nombre validé')
        break
    else :
        nb = input ("Saisissez un nombre(avec ou sans %) : ")

#un nombre : positif ou négatif avec ou sans des chiffres après la virgule et qui comporte ou non le signe %.
nb = input('Votre nombre : ')
prog = re.compile(r"^-?\d+[,|.]?\d{2}\%?$")

while True :
    if prog.search(nb) is not None :
        print('nombre validé')
        break
    else :
        nb = input ("Saisissez un nombre (avec ou sans chiffres après la virgule et avec ou sans %) : ")


############################################### RECAPITULATIF #############################################

#cas 1 : entier positif sans limite = ^\d+$
#cas 2 : entier positif limite de 10 chiffres = ^\d{1,10}$
#cas 3 : entier positif à 5 chiffres = ^\d{5}$
#cas 4 : entier relatif sans limite = ^-\d+$
#cas 5 : entier relatif limite de 10 chiffres = ^-\d{1,10}$
#cas 6 : entier relatif à 5 chiffres = ^-\d{5}$
#cas 7 : entier positif ou relatif sans limite = ^-?\d+$
#cas 8 : entier positif ou relatif sans limite = ^-?\d+$
#cas 9 : entier positif ou relatif limite de 10 chiffres = ^-?\d{1,10}$
#cas 10 : entier positif ou relatif limite de 10 chiffres = ^-?\d{1,10}$
#cas 11 : entier positif ou relatif à 5 chiffres = ^-?\d{5}$
#cas 12 : nombre positif ou négatif avec ou sans chiffres après la virgule = ^-?\d+\,?\d?$
#cas 13 : nombre positif ou négatif avec 2 chiffres après la virgules = ^-?\d+\,\d{2}$
#cas 14 : nombre version américaine = ^-?\d+[,|.]\d{2}$
#cas 15 : qui peut ou non comporter le signe % = ^\d+\%?$
#cas 16 : nombre positif ou négatif avec 2 chiffres après la virgules, avec ou sans % = ^-?\d+[,|.]?\d{2}\%?$

nb = input('Votre nombre : ')
#ici, autre méthode, on utilise un while avec un re.match
while re.match(r"^-?\d+[,|.]?\d{2}\%?$", nb) is None : #modifier votre regex en fonction du cas recherché
    nb = input('Entrez un nombre valide : ')
print("votre nombre est valide : {}".format(nb))
