import string

password = []

for i in range(4):
	for a in range(48,123):
		for b in range(48,123):
			for c in range(48,123):
				for d in range(48,123):
					res = (a|b)&(c|d)
					if res == 73:
						password.append(chr(a))
						password.append(chr(b))
						password.append(chr(c))
						password.append(chr(d))
						print("Password: ", ''.join(password))
						exit()