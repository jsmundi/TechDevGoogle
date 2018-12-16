
#Given a non-empty string like "Code" return a string like "CCoCodCode".

def strSplosion(strA):

	resultL = list()

	i = 1
	while i < len(strA) + 1:
		resultL.append(strA[:i])
		i += 1

	resultL = "".join(resultL)

	return resultL

def main():

	strA = 'Jaiteg'
	answer = strSplosion(strA)
	print(answer)

if __name__ == "__main__":
	main()