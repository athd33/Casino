#encoding:utf-8


import random
import time


money = 100					#création d'une variable int money (argent du joueur)
user_name = ""				#création d'une variable str pour le nom d'utilisateur

	# FONCTIONS

def myprint(message):		#création de la fonction myprint() avec un time.sleep(1)
	time.sleep(1)
	print(message)

def get_username():
	user_name = input("Quel est votre nom?")

	try:								#vérifier le type de user_name dans la condition if avec le try/except
		user_name = int(user_name)
		myprint("Votre nom est un numéro? Soyons sérieux...")
		get_username()
	except:
		myprint(f"Parfait {user_name}, nous allons pouvoir commencer")
		user_bet_function()
	return user_name


def user_bet_function():	#fonction pour récupérer la somme misée par le joueur
	global user_bet
	user_bet = input(f"Combien souhaitez vous miser? Attention, vous disposez de {money} $ ")
	try:
		user_bet = int(user_bet)
	except:
		print("Désolé, ce n'est pas un montant")
		user_bet_function()

	if user_bet <= 0:
		myprint("Sans argent, impossible de payer.")
		myprint("Revenez avec des sous...")
		exit()
	elif user_bet > money:
		myprint(f"Vous n'avez pas les fonds sufisants. Actuellement vous avez {money} $")
		user_bet_function()
	else:
		user_numbers_choice()
		return user_bet


def user_numbers_choice():
	global users_choice
	users_choice = -1
	users_choice = input("choisissez un nombre entre 0 et 50 :")
	try:									#vérifier si user_choice est de type int et pas str
		users_choice = int(users_choice)
	except:
		print("J'ai mal compris...")
		user_numbers_choice()
	if users_choice <= -1 or users_choice >= 51:
		print("Attention, entre 50 et 0! Merci")
		user_numbers_choice()
	else:
		random_number_function()
		result()

def random_number_function():				#création d'une fonction pour générer un nombre aléatoire avec random
	global random_number 					#variable globale pour la sortir de la fonction
	random_number = random.randrange(50)
	result()


def result():	
	global money
	if random_number == users_choice:
		money = money + (user_bet * 3)
		myprint("Rien ne va plus....")
		myprint(f"Bravo!!! C'est le {random_number} qui est sorti! ")
		myprint(f"Vous avez maintenant {money} $")
		play_again()
	elif (users_choice % 2) == 0 and (random_number % 2) == 0:  # utilisation de modulo pour définir si on ajoute les 50% à la mise
		money = money + (user_bet / 2)
		myprint("Rien ne va plus....")
		myprint(f"Pas mal, le {random_number} vous empochez la moitié de votre mise. Vous avez désormais {money} $")
		myprint(f"Vous disposez de {money} $")
		play_again()
	else:
		money = money - user_bet
		myprint("Rien ne va plus....")
		myprint(f"Perdu! c'est le {random_number} qui est sorti! Il vous reste {money} $, on recommence?")
		play_again()

def play_again():
	global current_game
	again = input("Rejouer??")
	if again == "oui":
		user_bet_function()
	else:
		myprint("Ok, au revoir")
		current_game = False
		exit()
		


		#PROGRAMME PRINCIPAL

get_username()					#Lancement du programme principal