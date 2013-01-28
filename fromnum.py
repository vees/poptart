from pipeline import links
try:
	while True:
		input = raw_input("Encode: ")
		if input=='':
			break
		print links.num_decode(input)
except EOFError:
	print "Ending"	
