password = 'a123456'
chance = 4
while chance > 0:
	chance = chance - 1
	answer = input('please enter your password: ')
	if answer == password:
		print('log in successful')
		break
	else:
		if chance > 1:
			print('wrong passord, you still have', chance, 'chances')
		elif chance == 1:
			print('wrong passord, you still have', chance, 'chance')
		elif chance == 0:
			print('account locked')