password = 'a123456'
chance = 3
while True:
	answer = input('please enter your password: ')
	if answer == password:
		print('log in successful')
		break
	else:
		chance = chance-1
		if chance > 1:
			print('wrong passord, you still have', chance, 'chances')
		elif chance == 1:
			print('wrong passord, you still have', chance, 'chance')
		elif chance == 0:
			print('account locked')
			break