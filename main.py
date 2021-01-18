import time
from djikstrasto import *



def askdata():		#Kysytään datan sisältävän tiedoston nimi
	txt = ".txt"
	print("Anna datan sisältävän .txt tiedoston nimi (ilman päätettä!):")
	file = input("> ")
	filename = file+txt
	try:
		data = open(filename, "r")	#avataan tiedosto, jos sellainen löytyy annetulla nimellä, muuten kutsutaan uudestaan askdataa
		try:
			main(data)
		except ValueError:	#Jos reittiä ei ole, "djikstraalgo" aiheuttaa ValueErrorin, joten jos näin käy, tulostetaan vain ilmoitus asiasta
			noroute()
	except FileNotFoundError:
		print("")
		print("Ei löydy tuollaista tiedostoa! Varmista, että se on samassa kansiossa .py tiedostojen kanssa")
		print("")
		askdata()

def main(data):
	startTime = time.time()
	dijkstra(data)
	exectime = time.time()-startTime
	print('')
	print("Algoritmin suoritus kesti: {} sekuntia".format(exectime))
	

askdata()

