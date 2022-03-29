password = 'a123456'
chance = 3
while True:
	answer = input('please enter your password: ')
	if answer == password:
		print('log in successful')
		break
	else:
		chance = chance-1
		if chance > 0:
			print('please try again')
		else:
			print('account locked')
			break