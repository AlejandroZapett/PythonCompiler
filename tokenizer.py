def tokenizer(file):
	tokens = {'(':'Open parenthesis', ')': 'Close parenthesis', '{': 'Open brace', '}': 'Close brace', ';': 'Semicolon'}
	#las key words se pueden leer de un archivo
	keywords = { 'int': 'Int keyword', 'return': 'Return keyword'}
	program = open(file, 'r').read().replace("\n", "").replace("\t", "")
	for x in tokens:
		program = program.replace(x, ' '+x+' ')
	return [item for item in program.split(" ") if len(item) != 0]

print(tokenizer('cprogram.c'))