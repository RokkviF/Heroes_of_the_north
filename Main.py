from time import sleep
from os import system, name 
import MakeAnewHero
def clear():
	system( 'clear' )

def welcome():
	print('Welcome to Heroes of the north')
	print('Would You like 1 player or 2player :')
	inp = input()
	return inp

def chooseAStory():
	story1 = 'The long night'
	story2 = 'Son of Odinn'
	print('The long night')
	print('Son of Odinn')
	inp = input('what story would you like to play ')
	if inp == 1:
		return story1
	else:
		return story2
def startTheGame():
	inp = welcome()
	clear()
	sleep(1)
	print('So chose a character to play')
	clear()
	sleep(1)
	hero = MakeAnewHero.makeAnew()
	sleep(1)
	clear()
	sleep(0.3)
	print('last thing chose a story')
	story = chooseAStory()
	clear()
	print('let the game begin')
	print('story: ' + story)
	print(hero['class'])
	

	



startTheGame()