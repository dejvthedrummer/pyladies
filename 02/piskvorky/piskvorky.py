import os, random
os.system('clear')

rowlenset = 19

def vyhodnot(string):
	
	string = string.lower()
	
	if "xxx" in string:
		return "x"
	elif "ooo" in string:
		return "o"	
	elif "o" not in string and "x" not in string:
		return "-"	
	elif "-" in string:	
		return "!"		
	
'''
Vrátí herní pole s daným symbolem umístěným na danou pozici
`pole` je herní pole, na které se hraje.
`pozice` je číslo políčka. Čísluje se od nuly.
`symbol` může být 'x' nebo 'o', podle toho jestli je tah za křížky
nebo za kolečka.
'''

def tah(pole, pozice, symbol):

	symbol = symbol.lower()
	rowlen = len(pole)
	radek = ""
	
	if symbol not in ('x', 'o'):
		print("Pozadovany symbol musi byt x nebo o.")
		tah_hrace(pole, symbol)
		#raise ValueError("incorrectSymbol.")
	
	elif pozice not in range(1, rowlen+1):	
		print("Pozice neexistuje.")
		tah_hrace(pole, symbol)
		#raise ValueError("notExist")
	
	elif pole[pozice - 1] != '-':	
		if symbol == 'x':
			print("Pozice je jiz nastavena.")
			tah_hrace(pole, symbol)
		elif symbol == 'o':
			tah_pocitace(pole, symbol)
		#raise ValueError("AlreadySet.")
			
	print("Nastavujeme", pozice)
	
	#draw the row
	for p in range(rowlen):
		
		if pole[p] not in ('x','o'):
			
			if p == pozice - 1 :
					
				radek += symbol
				print("Nastavujeme",symbol," pro pozici", pozice)
				print("Radek vypada takto", radek)
			else:
				radek += pole[p] 	
		else:
			radek += pole[p] 				
	print("Cely radek vypada takto", radek)
	return radek
	
			
def tah_hrace(pole, symbol):
	pozice = int(input("Zadej pozici pro X: "))
	print("Vlozil jsi", pozice)
	return(tah(pole, pozice, symbol))
	
def tah_pocitace(pole, symbol):
	pozice = int(random.randrange(1,rowlenset))
	return(tah(pole, pozice, symbol)) 
		

def piskvorky1d():
	pole = str("-------------------")
	print(pole)
	
	while vyhodnot(pole) == '!' or vyhodnot(pole) == '-':
				
		pole = tah_hrace(pole, "x")
		print("Hrac X zahral", pole)
		
		pole = tah_pocitace(pole, "o")
		print("Hrac O zahral", pole)
			
	print("Vyhral hrac",vyhodnot(pole))	

piskvorky1d()	
