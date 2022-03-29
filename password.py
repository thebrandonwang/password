password = 'a123456'
chance = 2
while True:
	answer = input('please enter your password: ')
	if answer == password:
		print('log in successful')
		break
	elif chance > 0:
		chance = chance-1
		print('please try again')
	elif chance == 0:
		print('account locked')
		break