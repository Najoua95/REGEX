import re


immat = input('Quelle est votre immatriculation ? : ')
prog = re.compile(r"^[A-Z]{2}([.-]?[0-9]{3})([.-]?[A-Z]{2})$")

while True :
     if prog.search(immat) is not None :
         print('Immatriculation valide !')
         break
     else :
         immat = input ("Saisissez une immatriculation (valide) : ")

     
################
adresse = input('Quelle est votre adresse IPv4 ? : ')
prog = re.compile(r"^(\d{1,3}\.){3}\d{1,3}$") ### ou prog = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")

while True :
    if prog.search(adresse) is not None :
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
            adresse = input("Adresse IPv4 est hors range! (Tapez une IPv4 valide): ")
    else : 
        adresse = input("Format de l'adresse IPv4 incorrecte ! (Tapez une IPv4 valide): ")




