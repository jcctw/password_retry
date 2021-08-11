#passwords retry

password = 'a123456'
print('You have 3 chances to input your passwords!')
trial = input('Please input the passwords:') 

i = 1 #password count
j = 3 - i #password count left

while i <= 3:
	if trial != password:
		print('Wrong passowrd!')
		if j > 0:
			print('You still have', j,'chance(s)!')
			trial = input('Please input the passwords:')
		else: #when count left = 0
			print('Sorry! You are not authorized to access!')
		i = i + 1 
		j = 3 - i
	else:
		print ('Log in sucess!')
		break

