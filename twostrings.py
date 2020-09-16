
def main():
	# input strings
	a = ['hello', 'goodbye']
	b = ['h', 'str']

	# loop
	for i in range(min(len(a), len(b))):
		yes = False
		for j in range(len(a[i])-1):
			if a[i][:j+1] in b[i]:
				yes = True
				break
		if yes:
			print('YES')
			break

		for j in range(len(b[i])-1):
			if b[0][:j+1] in a[i]:
				print('YES')
				break




if __name__ == '__main__':
	main()