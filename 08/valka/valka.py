from os import system
import random

system('clear')

# define a deck
def deck():

	obrazove = list("JQKA")
	obrazovehodnota = list(range(2,11))
	zakladni = list(range(2,11))
	
	#print(obrazovehodnota)
	
	barva = list('♥♠♦♣')
	value = zakladni + obrazove
	
	deck = []
		
	for b in barva:
		for v in value:
			#rewrite 
			points = 10
			deck.append((v,b,points)) 	
	
	return deck

# assess the cards played	
def asses(player_one_card,player_two_card):
	
	'''
	if player_one_card[0] in "JQK":	
		player_one_point = 10
	if player_two_card[0] in "JQK":	
		player_two_point = 10
	'''	
	

def run():
	gemeover = False
	
	#prepare the decks
	deck_a = deck()
	random.shuffle(deck_a)

	deck_b = deck()
	random.shuffle(deck_b)
	
	while gemeover == False: 

		system('clear')
		
		
		player1point = 0
		player2point = 0
		card1 = 'N/A'
		card2 = 'N/A'
		winner = 'N/A'
		
		state = """
		-------- HRA VALKA --------
		
		BODY HRAC 1: %s
		BODY HRAC 2: %s
		
		KARTA HRAC 1: %s
		KARTA HRAC 2: %s
		
		VYHRAL HRAC: %s
		
		""" % (player1point, player2point, card1, card2, winner)
		
		print(state)
				
		goon = input("Pokracovat y/n? ")
		print(goon)
		
		if 'n' == goon:
			gameover = True
		else:
			gameover = False
			
		print(gemeover)	
	print("Dekuji za hru, budu se tesit priste!")
run()	
