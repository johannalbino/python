import re

patterns = ['term1', 'term2']

text = 'This is a string with term1. This another with term2.'

for pattern in patterns:
	print ('Searching for "%s" in: \n "%s"' %(pattern, text))

	if re.search(pattern, text):
		print ("\n")
		print ("")