from os import system

system('clear') 

'''
# vypis soubor velkymi pismeny
with open('basnicka.txt',  encoding='utf-8') as soubor:
	
	#obsah = soubor.read()
	
	for line in soubor:
		print(line.rstrip().upper())
	
'''

# procisti slova ze souboru do seznamu 

def valid(word):
	valid = True
	
	capital = "ABCČDĎEFGHIJKLMNOPQRŘSŠTUVWXYZŽ"

	if word.isnumeric() == True:
		valid = False
	
	if word[0] in capital:
		valid = False
		
	if word == '' or word == '\n':
		valid = False
		
	return valid
def procisti_soubor(textak):
	with open(textak,  encoding='utf-8') as soubor:
	
		slovnik = []
		slovniktxt = ""
		for linenum, line in enumerate(soubor):	
		
			line = line.rstrip()
			
			if "/" in line:
				
				slovo = line.split('/')
							
				if not valid(slovo[0]):
					pass
				else:
					#print(slovo[0])
					slovnik.append(slovo[0])
					slovniktxt += slovo[0] + "\n"
			else:
				if not valid(line):
					pass
				else:
					#print(line.rstrip())
					slovnik.append(line)
					slovniktxt += line + "\n"
						
		return slovniktxt


def zapis(textak, obsah):

	with open(textak, mode="w" ,encoding='utf-8') as soubor:
		print(obsah, file=soubor)


obsah = procisti_soubor('index.dic')
zapis('slovnik.txt', obsah)

'''

with open('index.dic',  encoding='utf-8') as soubor:

	slovnik = []
	
	for linenum, line in enumerate(soubor):	
	
		line = line.rstrip()
		
		if "/" in line:
			
			slovo = line.split('/')
						
			if not valid(slovo[0]):
				pass
			else:
				#print(slovo[0])
				slovnik.append(slovo[0])
		else:
			if not valid(line):
				pass
			else:
				#print(line.rstrip())
				slovnik.append(line)
				
	print(slovnik)
'''

