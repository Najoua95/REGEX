import re

#1/Immatriculation 
immat = input('Quelle est votre immatriculation ? : ')
prog = re.compile(r"^[A-Z]{2}([.-]?[0-9]{3})([.-]?[A-Z]{2})$")

while True :
     if prog.search(immat) is not None :
         print('Immatriculation valide !')
         break
     else :
         immat = input ("Saisissez une immatriculation (valide) : ")

#2/IPv4
adresse = input('Quelle est votre adresse IPv4 ? : ')
while True :
    if (re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", adresse)) :
        essai = adresse.split(".")
        counter = 0
        for values in essai :
            value = int(values)
            if value > 255:
                counter +=1
        if counter == 0:
            print("Votre adresse IPv4 est valide !")
            break
    else :
        adresse = input('Adresse IPv4 incorrecte ! (Tapez une IPv4 valide): ')






