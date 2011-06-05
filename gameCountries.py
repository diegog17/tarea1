#!/usr/bin/python
# -*- coding: utf_8 -*-
# gameCountries.py: juego para adivinar paises
import random

def datosPais(pais):
	# Imprime las pistas para adivinar el pais en cuestion
	if (pais == "Argentina"):
		print "1) Messi, Agüero and Maradona were born in this country."
		print "2) The most popular tv show of this country is “Bailando por un sueño”."
		print "3) They are very famous for their tango."
	elif (pais == "Australia"):
		print "1) This country is an island and it is the only country with kangaroos."
		print "2) Surfers all around the world wants to go there because they have the best beaches to surf."
		print "3) The Olympics games in 2000 were held in this country."
	elif (pais == "Austria"):
		print "1) This country is located in central Europe"
		print "2) Amadeus Mozart, Sigmud Freud, Ludwig Van Beethoven were born there."
		print "3) The Capital city is Vienna"
	elif (pais == "Brazil"):
		print "1) This country is very famous for their “Carnaval”."
		print "2) This country is one of the two countries that speak Portuguese."
		print "3) They have won more world cups than anyone."
	elif (pais == "Canada"):
		print "1) The flag of this country has a leaf."
		print "2) The citizens of this country speak two languages, English and French."
		print "3) The weather in this country is too cold."
	elif (pais == "China"):
		print "1) It is the most populated country and one of the biggest in the world."
		print "2) Their language is very difficult to learn."
		print "3) Every tourist that goes to this country wants to visit The Great Wall."
	elif (pais == "Colombia"):
		print "1) This country is very famous for producing “Cafe”."
		print "2) The capital city of this country is Bogota."
		print "3) The colors of this country flag are yellow, red and blue."
	elif (pais == "Egypt"):
		print "1) This country has many deserts and the weather is really hot and dry."
		print "2) They are very famous for the pyramids and mommies."
		print "3) One of the most common animal is the camel."
	elif (pais == "England"):
		print "1) Their cities buses have two storeys."
		print "2) David Beckham was born in this country."
		print "3) This country has a queen and her name is Isabel."
	elif (pais == "France"):
		print "1) They are very famous for their perfumes."
		print "2) The Eiffel Tower is the most famous monument in this country."
		print "3) Many people say that the people of this country do not bathe a lot."
	elif (pais == "Germany"):
		print "1) This country is very famous for drinking lots of beer."
		print "2) They won four times the world cup."
		print "3) They defeated Argentina 4-0 in South Africa 2010 World cup."
	elif (pais == "Italy"):
		print "1) They are very famous for their “pasta” (spaghetti, ravioli, etc)"
		print "2) The shape of this country is very similar to a boot."
		print "3) Edinson Cavani(Uruguayan footballer) plays for a team of this country."
	elif (pais == "Jamaica"):
		print "1) This country is very well known for its reggae."
		print "2) Bob Marley was born there."
		print "3) The capital city is Kingston."
	elif (pais == "Japan"):
		print "1) This country is an island."
		print "2) The Playstation and Nintendo are originary from this country."
		print "3) Recently they had earthquakes that put many people in danger."
	elif (pais == "Mexico"):
		print "1) This country is very famous for their Tequila and spicy food."
		print "2) Marichi groups are very famous around the world."
		print "3) Uruguay defeated this country 1-0 in South Africa 2010 World Cup."
	elif (pais == "Netherlands"):
		print "1) They played against Uruguay in the World cup 2010."
		print "2) The capital city of this country is Amsterdam."
		print "3) Luis Suarez played for Ajax(Football team of this country)."
	elif (pais == "Russia"):
		print "1) This country is the biggest country in the world."
		print "2) The weather is really cold."
		print "3) The capital of this country is Moscow."
	elif (pais == "South Africa"):
		print "1) This country is one of the most powerful countries in Africa."
		print "2) The capital city of this country is Cape Town."
		print "3) The last World Cup was held in this country."
	elif (pais == "Spain"):
		print "1) They speak the same language that we do."
		print "2) We were once a colony of this country."
		print "3)”Las corridas de toros” are originally from this country."
	elif (pais == "Switzerland"):
		print "1) It is a very famous country because they have the best chocolate in the world."
		print "2) The capital of this country is Bern."
		print "3) Roger Ferderer (Tennis player) was born in this country."
	elif (pais == "United States of America"):
		print "1) This country is divided in fifty states."
		print "2) Michael Jordan, Madonna and Michael Jackson were born in this country."
		print "3) The statue of liberty is the most popular monument of this country."
	elif (pais == "Uruguay"):
		print "1) Carlos Gardel was born in this country."
		print "2) Football is the most popular sport in this country."
		print "3) The most popular drink in this country is “el mate”."

def crearPregunta(n, lPais):
	#Crea las opciones al azar eligiendo una posicion para la correcta
	correct = random.randint(1,5)
	used = []
	#Se asegura de no repetir paises en las opciones
	for i in range (1,6):
		if (i == correct):
			print i,")",lPais[n]
			used.append(n)
		else:
			op = random.randint(0,len(lPais)-1)
			while (op == correct) or (used.count(op) != 0):
				op = random.randint(0,len(lPais)-1)
			used.append(op)
			print i,")",lPais[op]

def countries():
	#Inicializacion de la lista de paises que integran el juego
	paises = ["Argentina", "Australia", "Austria", "Brazil", "Canada",
	"China", "Colombia", "Egypt", "England", "France", "Germany",
	"Italy", "Jamaica", "Japan", "Mexico", "Netherlands", "Russia",
	"South Africa", "Spain", "Switzerland", "United States of America",
	"Uruguay"]
	salir = False
	print "--------------------------------------------------"
	print "|Welcome to Countries Trivia                     |"
	print "|Guess the country using the hints to make points|"
	print "|Good Luck                                       |"
	print "--------------------------------------------------"
	answ = raw_input ("Are you ready? (write yes or no): ")
	if (answ.lower() == "no"):
		salir = True
	else:
		print ""
	
	while not salir:
		#Inicializacion de la lista que marca los paises sobre los
		#que ya se pregunto de manera de no repetir
		usado = []
		for i in range(len(paises)):
			usado.append(False)
		#Variables a usar en el juego
		contador = len(paises)
		a = random.randint(0,len(paises)-1)
		puntaje = 0
		#Comienzo del juego
		while (contador != 0):
			if (not usado[a]):
				usado[a] = True
				contador = contador - 1
				print "HINTS:"
				datosPais(paises[a])
				print ""
				print "OPTIONS:"
				crearPregunta(a, paises)
				print ""	
				resp = raw_input("Write your answer: ")
				if (resp.lower() == paises[a].lower()):
					print "CORRECT! You won 3 points"
					puntaje = puntaje + 3
				else:
					print ""
					print "Sorry but your answer is not correct"
					print "Last chance"
					resp = raw_input("Write your answer: ")
					if (resp.lower() == paises[a].lower()):
						print "CORRECT! You won 1 point"
						puntaje = puntaje + 1
					else:
						print ""
						print "Sorry but your answer is not correct"
						print "The correct answer is", paises[a]
						if (contador != 0): 
							print "You lost 1 point, better luck next one"
						else:
							print "You lost 1 point"
						puntaje = puntaje - 1
				print "You now have", puntaje, "points"
				print ""
			a = random.randint(0,len(paises)-1)
		print "Final result:",puntaje,"points"
		again = raw_input("Do you want to play again? (write yes or no): ")
		if (again.lower() != "yes"):
			print "See you next time"
			salir = True
		else:
			print "Ok, let's go again"
			print""
	
if (__name__ == "__main__"):
	countries()
	
