import random

lst = [("Albania", "Tirana"), ("Andorra", "Andorra la Vella"), ("Armenia", "Yerevan"), 
("Austria", "Vienna"), ("Azerbaijan", "Baku"), ("Belarus", "Minsk"), ("Belgium", "Brussels"), 
("Bosnia and Herzegovina", "Sarajevo"), ("Bulgaria", "Sofia"), ("Croatia", "Zagreb"), 
("Cyprus", "Nicosia"), ("Czech Republic", "Prague"), ("Denmark", "Copenhagen"), 
("Estonia", "Tallinn"), ("Finland", "Helsinki"), ("France", "Paris"), ("Georgia", "Tbilisi"), 
("Germany", "Berlin"), ("Greece", "Athens"), ("Hungary", "Budapest"), ("Iceland", "Reykjavik"), 
("Ireland", "Dublin"), ("Italy", "Rome"), ("Kazakhstan", "Nur-Sultan"), ("Kosovo", "Pristina"), 
("Latvia", "Riga"), ("Liechtenstein", "Vaduz"), ("Lithuania", "Vilnius"), 
("Luxembourg", "Luxembourg City"), ("Malta", "Valetta"), ("Moldova", "Chisinau"), 
("Monaco", "Monaco"), ("Montenegro", "Podgorica"), ("Netherlands", "Amsterdam"), 
("North Macedonia", "Skopje"), ("Norway", "Oslo"), ("Poland", "Warsaw"), 
("Portugal", "Lisbon"), ("Romania", "Bucharest"), ("Russia", "Moscow"), 
("San Marino", "San Marino"), ("Serbia", "Belgrade"), ("Slovakia", "Bratislava"), 
("Slovenia", "Ljubljana"), ("Spain", "Madrid"), ("Sweden", "Stockholm"), 
("Switzerland", "Bern"), ("Turkey", "Ankara"), ("Ukraine", "Kiev"), 
("United Kingdom", "London"), ("Vatican City", "Vatican City")]

questions_asked = 0
score = 0
for k,v in lst:
	tup = random.choice(lst)
	country, capital = tup
	print("What is the capital of", country + "?",  "\n" + \
		"Enter \'End Game\' to end the game and view your score.")
	questions_asked += 1
	ans = input()
	if ans.lower() == 'end game':
		break
	if ans.lower() == capital.lower():
		print("Correct!")
		score += 1
		lst.remove(tup)
	else:
		print("Wrong!", '\n' + "The capital of", country, "is", capital)
		lst.remove(tup)
print("You answered", score, "out of", questions_asked, "questions correctly.")
