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

#autre méthode, tout en regex :
adresse = input('Entrez votre adresse IPv4 ? : ')
if re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", adresse) :
    print("Okay !")
else : 
    print ("KO !")

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
#Augmenter le script pour taper le mot de passe (mdp, évidemment si l'email est valide où la seule spécifité du mdp est de contenir au moins 4caractères) 
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

####################
#Le mot de passe doit maintenant contenir au moins 6 caractères : au moins une lettre en miniscule ET au moins une lettre en majuscule Et au moins un chiffre Et au moins un charactére spécial (parmi $#@)

def correct_mail():
    email = input("Insérez une adresse mail valide : ")
    prog = re.compile(r"^[a-zA-Z0-9-._]+@{1}[a-zA-Z0-9]+\.[a-z]{2,4}$")
    mdp = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[\$#@]).{6,}$") #on doit utiliser '?=' : positive lookahead
    
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

