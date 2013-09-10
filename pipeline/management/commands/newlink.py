from pipeline import links
try:
	while True:
		input = raw_input("Encode: ")
		if input=='':
			break
		print "http://4ve.es/" + links.set_link(input)
except EOFError:
	print "Ending"	
