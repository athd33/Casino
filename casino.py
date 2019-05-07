#encoding:utf-8


import time
import random

########### VARIABLE ###########

money = 100

########## FONCTIONS ############

def myprint(mess): #fonction print avec un time.sleep()
	time.sleep(1)
	print(mess)

def start_game():
	player_name = input("Quel est votre nom? : ")
	try:
		player_name = int(player_name)
		myprint("Attention , votre nom est en lettres.")
		start_game()
	except:
		player_name = player_name.lower()
		return player_name

def get_number():
	number = random.randrange(50)
	return number


def get_bet():
	player_name = start_game()
	bet = input(f"Parfait {player_name}, combiez misez vous? Attention, vous disposez de {money} $ ")
	bet = int(bet)
	return bet

def get_user_number():
	user_number = input("Choisissez un nombre entre 0 et 50 : ")
	user_number = int(user_number)
	print("Rien ne va plus...")
	return user_number

############## PROGRAMME #####################

print("Bonjour")

number  = get_number()
bet = get_bet()
user_number  = get_user_number()

if user_number == number:
	print("Bravo!")
	money = money * 3
	myprint(f"Vous avez maintenant {money} $ ")

elif (user_number % 2) == 0 and (number % 2) == 0:
	money = money + (money / 2)
	myprint(f"Pas mal, vous avez maintenant {money} $")

else:
	myprint("Arf, perdu..")
	print("Perdu")

