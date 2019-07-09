import json
with open('resources/input.json', 'r') as input:
	obj = json.load(input)
	print( 'Hello ' + obj['name'])

	with open('build/output.md', 'w') as output:
			output.write('**' + obj['name'] + "'s hobbies**   \n" )
			for hobby in obj['hobbies']:
				output.write(' - ' + hobby + ' \n')		
