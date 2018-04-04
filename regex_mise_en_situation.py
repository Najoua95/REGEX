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

###################
#Ecrire un script qui vérifie que la chaîne saisie par un User est bien celle d’un email, sinon lui demander de resaisir à nouveau (jusqu'à obtenir un email valide) ?
def correct_mail():
    email = input("Insérez une adresse mail valide : ")
    prog = re.compile(r"^[a-zA-Z0-9-._]+@{1}[a-zA-Z0-9]+\.[a-z]{2,4}")
    while True : 
        if prog.search(email) is not None :
            print('E-mail valide !')
            return email
        else :
            email = input ("Insérez une adresse mail valide: ")
 correct_mail()

###################
#Ecrire 1script qui vérifie que la chaîne saisie par un User est bien celle d’un email, sinon lui demander de resaisir à nouveau (jusqu'à obtenir un email valide) ?
def correct_mail():
    email = input("Insérez une adresse mail valide : ")
    prog = re.compile(r"^[a-zA-Z0-9-._]+@{1}[a-zA-Z0-9]+\.[a-z]{2,4}$")
    mdp = re.compile(r"^[a-zA-Z0-9]{4,}$")
    
    while True : 
        if prog.search(email) is not None :
            print('E-mail valide !')
            mot_de_passe = input("Votre mot de passe ? ")
            if mdp.search(mot_de_passe) is not None : 
                print('mot de passe valide')
            return email
        else :
            email = input ("Insérez une adresse mail valide: ")
correct_mail()

##################

