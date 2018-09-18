# -*- coding: utf-8 -*-
"""
název: DataTel.py
popis: Databáze jmen a telefonních čísel
autor: Miroslav Janota
"""

#Deklarace globálních proměnných
database={}
obsah=["1-Vypiš kompletní list", "2-Vyhledej záznam", "3-Smaž záznam", "4-Přidej záznam","5-Odvšivení","6-Ukončit"," "]
ladeni=["1-Vypiš řádek","2-Vypiš proměnnou database","3-Zpět do hlavního menu"," "] 
pocetrad=0

#Otevře soubor a spočítá řádky - vrací počet řádků
def pocet_radku():
	poc=0
	with open('pokus.txt','rt', encoding='utf-8') as soubor:
		for radka in soubor:
			poc+=1
	return poc		

#Načtení řádků souboru do slovníku Database
def inicializace():
	pass

#Hlavní menu
def vyber_fci():
	print("")
	for a in obsah:
		print(a)
	
	print("")	
	vyber=int(input("Zadej svůj výběr: "))
	print("")
	
	if vyber==1:
		vypis()
			
	elif vyber==2:
		hledej()
		
	elif vyber==3:
		smazat()
		
	elif vyber==4:
		novy()
	
	elif vyber==5:
		odvsiveni()
		
	elif vyber==6:
		exit()	
		
	else:
		print("Není v seznamu!")
		anone=input("Přejete si opakovat výběr? [a/n] :")
		print("")
		
		if anone=="a":
			vyber_fci()
		else:
			pass	

#Vypíše seznam na obrazovku
def vypis():
	print("")
	pocetrad=pocet_radku()
	print("Počet záznamů v souboru: ",pocetrad)
	print("")
	with open('pokus.txt', 'rt', encoding='utf-8') as soubor:
		radka=""
		for radka in soubor:
			print(radka.rstrip())
								
	vyber_fci()	

#Vytvoří nový záznam a uloží na poslední řádku souboru
def novy():
	pocetrad=pocet_radku()+1
	while True:
		with open('pokus.txt', "at", encoding='utf-8') as soubor:
			print("")
			jme=input("Zadej jméno: ")	
			pri=input("Zadej příjmení: ")
			cis=input("Zadej telefonní číslo: ")
			database[pocetrad]=[str(pocetrad-1),jme,pri,cis]
			
			#Zápis do souboru - na konec
			soubor.write(database[pocetrad][0]+" ")
			soubor.write(database[pocetrad][1]+" ")
			soubor.write(database[pocetrad][2]+" ")
			soubor.write(database[pocetrad][3]+"\n")				
			soubor.close()
			
			while True:
				#Vstup z klávesnice - Rozhodování o pokračování
				anone=input("Přejete si přidat další záznam? A/N ")
				anone.lower()
				print("")
				if anone=="a":
					break
				elif anone=="n":
					vyber_fci()
				else:
					print("")	
					print("Vyberte si pouze A jako Ano, nebo N jako Ne!")
					print("")					
								
	vyber_fci() 
	
#Smaže vybraný řádek	
def smazat():
	zaznam=input("Který řádek si přejete smazat? ")
	
	pass

#Vyhledá řetězec v souboru	
def hledej():
	pass

#Vypíše různé ladící proměnné
def odvsiveni():
	print("")
	for a in ladeni:
		print(a)
	print("")
	
	vyber=int(input("Zadej svůj výběr: "))
	print("")
	
	if vyber==1:
		nacti()
		vyber=int(input("Zadej číslo řádku seznamu: "))
		print("")
		print(database[vyber])
		odvsiveni()
			
	elif vyber==2:
		nacti()
		print(database)
		odvsiveni()
		
	elif vyber==3:
		vyber_fci()
		
	else:
		print("Není v seznamu!")
		anone=input("Přejete si opakovat výběr? [a/n] :")
		print("")
		
		if anone=="a":
			odvsiveni()
		else:
			pass	

#Načte obsah souboru do slovníku database
def nacti():
	database.clear()
	with open('pokus.txt', 'rt', encoding='utf-8') as soubor:
		por=0
		radka=""
		for radka in soubor:
			database[por]=radka.split()
			por+=1

#Hlavní část programu
if __name__ == "__main__":
	vyber_fci()
	
