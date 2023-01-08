string = ""
bar = 1

while bar <= 7:
	kol = bar	
	while kol > 1:
		string = string + " "
		kol = kol - 1
	kanan = 0
	while kanan <= (7 - bar):
		string = string + "#"
		kanan = kanan + 1	
		
	string = string + "\n"
	bar = bar + 1
print (string)