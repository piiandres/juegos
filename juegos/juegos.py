import hangman
import reversegam
import tictactoeModificado
import json
import os
import PySimpleGUI as sg



def main(args):
	j=''
	#Almacenara los juegos que juegue el jugador
	sigo_jugando = True
	while sigo_jugando:
		diseno=[[sg.Text('Elegí juego a jugar')],[sg.Combo(['Hangman', 'TicTacToe','Otello','Salir'])],[sg.Button('Ok'), sg.Button('Cancel')]]
		window= sg.Window('juego',diseno)
		s,opcion=window.read()
		window.close()
	
		#print('''
		#Elegí con qué juego querés jugar:
		#1.- Ahorcado
		#2.- Ta-TE-TI
		#3.- Otello
		#4.- Salir''')
	
		

		if opcion[0] == 'Hangman':
			hangman.main()
			j=j+'-Hangman'
		elif opcion[0] == 'TicTacToe':
			tictactoeModificado.main()
			j=j+'-Tictactoe'
		elif opcion[0] == 'Otello':
			reversegam.main()
			j=j+'-Otello'
		elif opcion[0] == 'Salir':
			sigo_jugando = False
			
			
	layout = [[sg.Text('Ingrese su nombre:')],[sg.InputText()],[sg.Ok(), sg.Cancel()]]
	window= sg.Window('juego', layout)    
	event, values = window.read()    
	window.close()
	
	aux=[{'nombre': values[0], 'jugo': j}]
	
	if os.path.exists("jugadores.txt"):  
		#chequea que exista el archivo
		archivo= open("jugadores.txt", "r+")
		data = json.load(archivo) 
		data.append(aux) 
		archivo.seek(0) 
		#Retorna al comienzo del archivo para no perder lo anterior
		json.dump(data, archivo) 
		#Lo carga
		
		
	else:
		archivo= open("jugadores.txt","x") #la primera vez va a ir al else para generarlo
		json.dump(aux,archivo)
	archivo.close()
		
	jugador=open("jugadores.txt","r")
	datos=json.load(jugador)
	print(json.dumps(datos))
	jugador.close()

					
		
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
    

