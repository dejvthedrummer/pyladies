from random import randrange, uniform
from turtle import forward
pcRand = randrange(3)
userRes = ""


for i in range(5):
	print(i)

'''

if pcRand == 0:
	pcRes = "kamen"
elif pcRand == 1:
	pcRes = "nuzky"
elif pcRand == 2:
	pcRes = "papir"	
print ("0 = kamen, 1 = nuzky, 2 = papir")

user = int(input("Zadejte vasi volbu: "))

if user == 0:
	userRes = "kamen"
elif user == 1:
	userRes = "nuzky"
elif user == 2:
	userRes = "papir"	

if pcRes == userRes:
	print("REMIZA!")
elif pcRes == "kamen" and userRes == "nuzky":
	print("Pocitac vyhral!")
elif pcRes == "nuzky" and userRes == "papir":
	print("Pocitac vyhral!")
elif pcRes == "papir" and userRes == "kamen":
	print("Pocitac vyhral!")	
		
print("Pocitac mel ", pcRes, "a vy ", userRes )

'''
