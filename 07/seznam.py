'''

import random

def balicek():
	balicek = []
	listhodnot = list(range(2,11))
	listhodnot += list('JQKA')
	
	#print(listhodnot)
	
	for barva in '♠', '♥', '♦', '♣':
		for hodnota in listhodnot:
			balicek.append(str(hodnota)+barva)
	return balicek
	
balicek = balicek()

random.shuffle(balicek)
karta = random.choice(balicek)

print(karta)


#vicerozmerne seznamy

seznam_seznamu = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(seznam_seznamu[0][0])



#prace se zviratky

def vytvor_seznam_zvirat():
	zvirata = ["pes", "kočka", "králík", "had"]
	return zvirata

zvirata = vytvor_seznam_zvirat()

#zvirata = vytvor_seznam_zvirat()
#zvirata.pop()
#print(zvirata)
#zvirata = vytvor_seznam_zvirat()
#print(zvirata)


def filtruj_kratka_jmena(jmeno):
	items = []
	for item in jmeno:
		if len(item) < 5:
			items.append(item)
		else:
			continue
	return items
	
print(filtruj_kratka_jmena(zvirata))


def filtruj_k(seznam):
	items = []
	for item in seznam:
		if item[0] == 'k':
			items.append(item)
		else:
			continue
	return items

print(filtruj_k(zvirata))


def bez_prvniho(seznam):
	del seznam[0]	
	return seznam
	
print(bez_prvniho(zvirata))

# Had prvni a ostatni zvířata seřadí podle abecedy, ale bude ignorovat první písmeno.

zvirectvo = ["pes", "kočka", "králík", "had", "andulka"]


def serad_od_druheho(pole):
	zvirata = []
	for item in pole:	
		zvirata.append((item[1], item))
	zvirata.sort()

	nova_zvirata = []
	
	for zvire in zvirata:
		nova_zvirata.append((zvire[1]))
		
	
	print(nova_zvirata)

serad_od_druheho(zvirectvo)

#nakresli tabulku 

def nakresli_tabulku():
	linemax = 5
	posmax = 5
	
	
	for l in range(linemax):
		for p in range(posmax+1):
			if p == posmax:
				print('a', end = '\n')
			else:
				print('x', end = '')

nakresli_tabulku()

# hra had

#napis cestu
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
   

def napis_cestu(souradnice):
	linemax = 10
	posmax = 10
	
	for l in range(linemax):
		for p in range(posmax+1):
			if p == posmax:
				if (l, p) in souradnice:
					print("X", end = '\n')
				else:
					print(".", end = '\n')
			else:
				if (l, p) in souradnice:
					print("X", end = " ")
				else:
					print(".", end = " ")


def ask_way(startPosition):
	
	cls()
	
	napis_cestu(startPosition)
	#napis_cestu(startPosition)
	move = list(startPosition)
	
	while True:
	
		direction = input("Tak kam dal? ")
		
		print (startPosition[-1])
		if direction == "s":
			move.append((move[-1][0]-1,move[-1][1]))
		elif direction == "j":
			move.append((move[-1][0]+1,move[-1][1]))
		elif direction == "v":
			move.append((move[-1][0],move[-1][1]+1))
		elif direction == "z":
			move.append((move[-1][0],move[-1][1]-1))
		cls()
		
		napis_cestu(move)

start = [(0,0)]

ask_way(start)



#enumeration

dny = ['Po', 'Út', 'St', 'Čt', 'Pá', 'So', 'Ne']

for index, day in enumerate(dny, 1):
	print(f"Dnes je {index}. {day}")



#zip
veci = ['tráva', 'slunce', 'mrkev', 'list']
barvy = ['zelená', 'žluté', 'oranžová', 'zelený']

print(list(zip(veci, barvy)))

#zip
veci = ['tráva', 'slunce', 'mrkev', 'list', 'myšlenka', 'spravedlnost']
barvy = ['zelená', 'žluté', 'oranžová', 'zelený']
for vec, barva in zip(veci, barvy):
    print(f"{vec} je {barva}")


with open ("../02/testovaci.py", encoding = 'utf-8') as soubor:
    for radek in soubor:
        radek = radek.rstrip()
        print('    ' + radek)


    
for file in range(10):
	open("myfile"+str(file)+".txt", "x")    
	
'''

with open ("../02/testovaci.py", encoding = 'utf-8') as soubor:
	print(int(soubor.read()))		


        
        
