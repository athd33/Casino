#encoding:utf-8


import random
import time


money = 100					#création d'une variable int money (argent du joueur)
user_name = ""				#création d'une variable str pour le nom d'utilisateur

	# FONCTIONS


def get_username():
	global user_name		# je déclare user_name en variable globale pour la prendre en compte hors de la fonction
	time.sleep(1)			# un délai d'une seconde
	user_name = input("Quel est votre nom?")

	try:								#vérifier le type de user_name dans la condition if avec le try/except
		user_name = int(user_name)
		print("Votre nom est un numéro? Soyons sérieux...")
		get_username()
	except:
		print("Parfait {}, nous allons pouvoir commencer".format(user_name))
		user_bet_function()


def user_bet_function():					#fonction pour récupérer la somme misée par le joueur
	global user_bet 
	user_bet = input("Combien souhaitez vous miser?")
	try:
		user_bet = int(user_bet)
	except:
		print("Désolé, ce n'est pas un montant")
		user_bet_function()

	if user_bet <= 0:
		print("Sans argent, impossible de payer.")
		time.sleep(2)
		print("Revenez avec des sous...")
		exit()
	elif user_bet > money:
		time.sleep(1)
		print("Vous n'avez pas les fonds sufisants. Actuellement vous avez {} $".format(money))
		user_bet_function()
	else:
		user_numbers_choice()


def user_numbers_choice():
	global users_choice
	users_choice = -1
	users_choice = input("choisissez un nombre entre 0 et 50 :")
	try:									#vérifier si user_choice est de type int et pas str
		users_choice = int(users_choice)
	except:
		print("J'ai mal compris...")
		user_numbers_choice()
	if users_choice <= -1 and users_choice >= 51:
		print("Attention, entre 50 et 0! Merci")
		user_numbers_choice()
	else:
		random_number_function()

def random_number_function():				#création d'une fonction pour générer un nombre aléatoire avec random
	global random_number 					#variable globale pour la sortir de la fonction
	random_number = random.randrange(50)
	print(random_number)
	result()


def result():	
	global money
	if random_number == users_choice:
		money = money + (user_bet * 3)
		print("Bravo")		
		time.sleep(1)
		print("Vous avez maintenant {} $".format(money))
		play_again()
	elif users_choice % 2 == 0 and random_number % 2 == 0:  # utilisation de modulo pour définir si on ajoute les 50% à la mise
		money = money + (user_bet / 2)
		print('Pas mal, vous empochez la moitié de votre mise. Vous avez désormais {} $'.format(money))
		time.sleep(1)
		print("Vous disposez de {} $".format(money))
		play_again()
	else:
		print("Perdu")
		time.sleep(2)
		play_again()

def play_again():
	global current_game
	again = input("Rejouer??")
	if again == "oui":
		time.sleep(1)
		user_bet_function()
	else:
		print("Ok, au revoir")
		current_game = False
		


		#PROGRAMME PRINCIPAL

get_username()					#Lancement du programme principal