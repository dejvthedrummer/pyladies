a = float(input('Zadej stranu čtverce v centimetrech: '))
positive = a >= 0
print(positive)

if positive:
	print('Obvod čtverce se stranou', a, 'je', 4 * a, 'cm')
	print('Obsah čtverce se stranou', a, 'je', a * a, 'cm2')
else:
	print("Obsah a obvod ctverce nemuze byt pocitany na zaklade zaporneho cisla")
