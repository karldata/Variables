from random import randint
while True:
	print('Choose Input:')
	Player = input()
	Computer = randint(0,2)


	if Computer == 0:
		Computer = 'Scissor'
	if Computer == 1:
		Computer = 'Paper'
	if Computer == 2:
		Computer = 'Rock'

	print('You choose:' + str(Player))
	print('Computer chooses:' + str(Computer))


	if Player == Computer:
			print('Draw')

	else:
			if 'Scissor' in Player:
				if Computer == 'Paper':
					print('You Win')
				else:
					print('You Lose')
			elif Player == 'Rock':
				if Computer == 'Paper':
					print('You Lose')
				else:
					print('You Win')
			elif Player == 'Paper':
				if Computer == 'Rock':
					print('You Lose')
				else:
					print('You Win')
			elif Player == "Quit":
					print("Quitting game...")
					break

			else:
				print('Wrong Input!')


