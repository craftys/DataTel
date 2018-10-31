# -*- coding: utf-8 -*-
"""
název: DataTel.py
popis: Databáze jmen a telefonních čísel
autor: Miroslav Janota
"""

#import knihoven
import os


#Deklarace globálních proměnných
database={}
obsah=["------------------------------------", " 1-Vypiš kompletní list", " 2-Vyhledej záznam", " 3-Smaž záznam", " 4-Smaž celý seznam", " 5-Přidej záznam"," 6-Odvšivení"," 7-Ukončit","------------------------------------", " "]
ladeni=["------------------------------------", " 1-Vypiš řádek"," 2-Vypiš proměnnou database"," 3-Informace o databázi"," 5-Zpět do hlavního menu", "------------------------------------"," "] 
pocetrad=0

#Ošetření vyjimky - pro případ, že soubor neexistuje
def je_soubor():
	print()
	if (not os.path.isfile('pokus.txt')):
		print("Soubor s databází neexistuje!")
		print("Bude vytvořen nový soubor s názvem pokus.txt")
		#Vytvoření prázdného souboru pokus.txt
		with open('pokus.txt','wt', encoding='utf-8') as soubor:
			soubor.close()
							
	else:
		with open('pokus.txt','rt', encoding='utf-8') as soubor:
			if pocet_radku()==0:
				print("Soubor je prázdný")
			else:
				print("V souboru je " + str(pocet_radku()) + " záznamů")	
			

#Otevře soubor a spočítá řádky - vrací počet řádků
def pocet_radku():
	poc=0
	with open('pokus.txt','rt', encoding='utf-8') as soubor:
		for radka in soubor:
			poc+=1
	return poc		

#Načtení řádků souboru do slovníku Database
def inicializace():
	je_soubor()
	vyber_fci()

#Hlavní menu
def vyber_fci():
	print()
	
	#Vypíše seznam položek menu
	for a in obsah:
		print(a)
	
	#Zabránění uživateli v zadání jiného znaku než čísla
	while True:
		print("")
		vstup=input("Zadej svůj výběr: ")
		if str.isdigit(vstup):
			vyber=int(vstup)
			break
		else:
			print("")
			print("Nebyla zadaná číselná hodnota!")
			

	#Řízení toku programu podle volby menu
	if vyber==1:	#Vypíše celý seznam
		vypis()
			
	elif vyber==2:	#Vyhledá položku v seznamu
		hledej()
		
	elif vyber==3:	#Smaže položku v seznamu
		smazat()
		
	elif vyber==4:	#Smaže kompletně celý seznam
		smazatvse()
			
	elif vyber==5:	#Vloží novou položku do seznamu
		novy()
			
	elif vyber==6:	#Debug
		odvsiveni()
		
	elif vyber==7:	#Ukončí program
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
	print("Počet záznamů v souboru: " + str(pocet_radku()))
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
	#Zabránění uživateli v zadání jiného znaku než čísla
	nacti()
	while True:
		print("")
		print("Který řádek si přejete smazat?")
		print()
		vstup=input("Zadej svůj výběr: ")
		if str.isdigit(vstup):
			vyber=int(vstup)
			#DEBUG 1
			print("Výběr ",type(vyber)," ",vyber)
			print("Vstup",type(vstup)," ",vstup)
			print(len(database))
			#DEBUG 1
			if (vyber<len(database)-1):
				print("Prošlo !!!")
				print()
				break
			
			else:
				print("Database má méně položek")
				zapis()
				vyber_fci()
			
					
		else:
			print("")
			print("Nebyla zadaná číselná hodnota!")
	
	#del database[vyber]
	del database[vyber]
	print(database)
	print()
	#zapis()
	vyber_fci()	

#Smaže celý seznam
def smazatvse():
	#with open('pokus.txt', 'wt', encoding="utf-8") as soubor:
	pass	


#Zapíše slovník database do souboru
def zapis():
	#nacti()   
	with open('pokus.txt', "wt", encoding="utf-8") as soubor:
		for klic in database:
			soubor.write(database[klic][0]+" ")
			soubor.write(database[klic][1]+" ")
			soubor.write(database[klic][2]+" ")
			soubor.write(database[klic][3]+"\n")				
			soubor.close()


#Vyhledá řetězec v souboru	a vypíše řádek, ve kterém se vyskytuje
def hledej():
	nacti()
	print()
	hledany=input("Zadej hledané jméno nebo číslo: ")
	print()
	for klic in range(len(database)):
		for polozka in database[klic]:
			if hledany == polozka:
				print(database[klic])
	vyber_fci()
				
				

#Vypíše různé ladící proměnné
def odvsiveni():
	print("")
	for a in ladeni:
		print(a)

	#Zabránění uživateli v zadání jiného znaku než čísla
	while True:
		print("")
		vstup=input("Zadej svůj výběr: ")
		if str.isdigit(vstup):
			vyber=int(vstup)
			break
		else:
			print("")
			print("Nebyla zadaná číselná hodnota!")
	
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
		print("Počet řádků databáze je: " + str(pocet_radku()))
		print()
		odvsiveni()
		
	elif vyber==5:
		vyber_fci()
		
	else:
		print("")
		print("Není v seznamu!")
		print("")
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
	inicializace()
	
