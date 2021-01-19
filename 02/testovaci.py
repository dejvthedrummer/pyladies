from turtle import speed, bgcolor, forward, left, color, circle, exitonclick

'''
#n-angle per user
anglecount= int(input("Number of angles: "))

angle = 360/int(anglecount)

for _ in range(anglecount):
	forward(50)
	left(angle)


#circle
for _ in range(360):
	forward(1)
	left(1)


#spiral squerish

length = 10
speed(0)


for _ in range(10):
	left(90)
	forward(length)
	left(90)
	forward(length)
	length = length + 10

exitonclick()



#smallest number
nejmensi = None
print(nejmensi)

for _ in range (5):
	aktualni = input("Zvol si cislo: ")
	
	if nejmensi == None: 
		nejmensi = aktualni 	
	if aktualni < nejmensi:
		nejmensi = aktualni
	
print("Nejmensi cilso je " + nejmensi)


#zamena retezce

slovo = input('Slovo: ')
pozice = int(input('Které písmeno zaměnit (od nuly)? '))
novy_znak = input('Nové písmeno: ')

before = slovo[:pozice]
after = slovo[pozice+1:]

print(before + novy_znak + after)


#inicialy

jmeno = input("Jake je vase jmeno? ")
prijmeni = input("Jake je vase prijmeni? ")

print("Vase inicialy jsou " + (jmeno[0]+prijmeni[0]).upper())

Cas stehovanim 
#sablony

sablona = 'Ahoj {jmeno}! Tvoje číslo je {cislo}.'
print(sablona.format(cislo=7, jmeno='Hynku'))
print(sablona.format(cislo=42, jmeno='Viléme'))
print(sablona.format(cislo=3, jmeno='Jarmilo'))


#pohlavi

prijmeni = input("jake je Vase prijmeni? ")

if prijmeni[-1] == "a" or prijmeni[-1] == "á":
	print("Vy musite byt zena!")
else:
	print("Zdravim pane")


import os
os.system('clear')

lyrics = input("Insert the song lyrics\n")
char = input("What character are you searching?\n")
count = 0
leng = int(len(lyrics))


for _ in range(leng):
	if lyrics[_] == char:
		count = count + 1
print("There are" ,count, "chars in total in the lyrics.")

#counter

import os
os.system('clear')


for counter in range(5):
	print("Řádek", counter)



#mocnina

import os
os.system('clear')

for counter in range(5):
	print(counter,"na druhou je", counter**2)



#matice

import os
os.system('clear')

for radek in range(5):
	for pozice in range(5):
		if pozice == 4:
			print("X", end = "\n")
		else:
			print("X", end = " ")

#nasobeni v matici

import os
os.system('clear')

for radek in range(5):
		
	for pozice in range(5):
		 
		if pozice == 4:
			print(char, end = "\n")
		else:
			print(char, end = " ")

		char = char + radek	
		


#pisnicka bez specialnich znaku

import os
os.system('clear')

l1 = "!#$%&\'()*+,-./:;<=>?@[\]^_{|}~."
l2 = '"'

specchars = l1 + l2

print(specchars)

lyrics = input("Add the text")
counter = 0

for _ in range(len(lyrics)):
	char = lyrics[_]
	if not char in (specchars):
		counter = counter + 1
		
print("There are", counter ,"non special characters.")


import os, random
from obrazek import obrazek
os.system('clear')

#sibenice
words = ["pes", "zahrada", "hovno" ]

gamecontinue = True
wrongtrymax = 9


print("Ja uz mam vybrano, tak hadej pismeno.")

while gamecontinue == True :
	
	word = words[random.randint(0,2)].lower()
	wordlen = len(word)
	guessword = "_" * wordlen 
	wrongtrycount = 0 
	guesschar = ""
	currentgame = True
	
	while currentgame == True :
		
		os.system('clear')
		print(obrazek(wrongtrycount))
		print(f"Hadane slovo: {guessword}")
			
		while True:	
			guesschar = input("Zadej pismeno:").lower()
		
			if len(guesschar) > 1:
				print("Nevalidni vstup")
			else:
				break
		
		if guesschar in word:
			for _ in range(wordlen):
				if word[_] == guesschar:
					guessword = guessword[:_] + guesschar + guessword[_+1:]
		else:
			#print("Pismeno",guesschar,"ve slove neni")	
			wrongtrycount = wrongtrycount + 1
			
			#print("Spatnych pokusu",wrongtrycount)	
				
		print(guessword)
		
		if guessword == word:
			os.system('clear')
			print("Skvele, uhodl jsi. Hledane slovo bylo",guessword)
			break
		elif wrongtrycount == wrongtrymax:
			print("Mrzi me to, mel jsi",wrongtrymax,"spatnych poskusu")
			break
			
	gamecontinue = input("Chces pokracovat A/N? ").lower()
	if gamecontinue == "a":
		print("Nova hra")
		gamecontinue = True
		continue
	else:
		gamecontinue = False
		break	

#obsah funkce

def obsah(a,b):
	return a*b
	
print(obsah(2,2))


#rekurze

def pruzkum(hloubka):
    print(f'Rozhlížím se v hloubce {hloubka} m')

    if hloubka >= 30:
        print('Už toho bylo dost!')
    else:
        print(f'Zanořuju se (z {hloubka} m)')

        pruzkum(hloubka + 10)

        print(f'Vynořuju se (na {hloubka} m)')

pruzkum(0)

#faktorial

import os, random
os.system('clear')

def factorial(x):
    if x == 0:
        return 1
    elif x > 0:
        return x * factorial(x - 1)

print(factorial(5))
print(1 * 2 * 3 * 4 * 5)


#funkce pohlavi

def pohlavi(gender):
	if gender[-1] == "a":
		print("Vy musite byt zena!")
	else:
		print("Tak vy budete muz")
		
prijmeni = input("Jake je vase jmeno?")

pohlavi(prijmeni)

#domky jednim tahem

from turtle import forward, left, right, exitonclick
import os
os.system('clear')


def domky(housesize, housecount):
	house = 0
	while house <= housecount:
		
		left(90)
		forward(100*housesize)
		right(90)
		forward(100*housesize)
		right(135)
		forward(141*housesize)
		left(135)
		forward(100*housesize)
		left(135)
		forward(141*housesize)
		right(90)
		forward(70*housesize)
		right(90)
		forward(70*housesize)
		right(45)
		forward(100*housesize)
		left(90)
		
		#move to next house
		forward(100)
		
		house += 1
		housesize += housesize*2

domky(1,1)

exitonclick()	

#try catch

def nacti_cislo():
    while True:
        odpoved = input('Zadej číslo: ')
        try:
            return int(odpoved)  # máme výsledek, funkce končí
        except ValueError:
            print('To nebylo číslo!')
            
nacti_cislo()


'''

def obsah_ctverce(strana):
    if strana > 0:
        return strana ** 2
    else:
        raise ValueError(f'Strana musí být kladná, číslo {strana} kladné není!')
        
obsah_ctverce(-2)
