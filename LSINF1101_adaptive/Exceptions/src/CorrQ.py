#!/usr/bin/python3
# -*- coding: utf-8 -*-


def q(command):
	parameters = command.split ()
	try: # ajouté
		if parameters[0] == "divide":
			print ( "The value of your division is: {0}".format ( float(parameters[1])/float(parameters[2])))
		elif parameters[0] == "showfile":
			with open ( parameters[1] ) as file:  # modifié
				print ( file.read () )
		else:
			raise Exception ( "Command not recognized" ) # modifié
	except:
		print ( "There was an error" )
