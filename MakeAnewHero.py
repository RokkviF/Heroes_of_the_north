import csv
def makeAnew():
	with open('Classes.csv') as csvfile:
		types = csv.DictReader(csvfile)
		hero = {}
		printAllclasses()
		print('\n' 'press 1 for warrior \npress 2 for mage \npress 3 for rouge\n')
		inp = input('class number: ')
		pickedClass = ''
		if inp == '1':
			pickedClass = 'warrior'
		elif inp == '2':
			pickedClass = 'mage'
		elif inp == '3':
			pickedClass = 'rouge'
		for row in types:
			if row['class'] == pickedClass:
				tmpdic = {}
				for key in row:
					tmpval = str(row[key])
					tmpkey = str(key)
					tmpdic.update({tmpkey:tmpval})
				hero = tmpdic
		return hero

def printAllclasses():
	with open('Classes.csv') as csvfile:
		types = csv.DictReader(csvfile)
		print("so you want to make a new hero ??" '\n')
		print("So now for the class " '\n')
		print('you can choose: ''\n')
		for row in types:
			print('Class: ' + row['class'])
			print('Main weapon: '+ row['weapon'])
			print('Stats: ')
			print('   Health: ' +row['health'])
			print('   Damage: ' +row['damage'])
			print('   Luck: ' +row['luck'])

