import string

def pwcracker(n):
	characters = list(string.ascii_lowercase) + list(string.ascii_uppercase)

	pw = []

	pw.extend(characters)

	if n == 1:
		print(pw)
	else:
		for cycle in range(n - 1):
			copy = []
			for word in pw:
				for char in characters:
					for x in range(len(word)):
						copy.append(word[:x] + char + word[x:])
			pw = copy
		print(pw)
		print(len(copy))

pwcracker(3)
