import curses
import random
import time

alto=15
ancho=50
pantalla = curses.initscr()

#============================
#===inicializacion de curses=====
#============================
curses.noecho()
curses.cbreak()
curses.curs_set(0)
pantalla.keypad(True)
pantalla.nodelay(True)


#============================
#===inicializacion de snake=====
#===y de la fruta=====
#============================

lista_frutas="o","*","#","m","$"
frutaa=random.randint(0,4)
trut=lista_frutas[frutaa]
x=0 
y=0
snake=[[y,x]]
fruta=[random.randrange(alto),random.randrange(ancho)]
pantalla.addstr(fruta[0],fruta[1],trut)
mov_horizontal = 1
mov_vertical = 0


#suma de puntaje
suma_puntaje=0

#============================
#===comienzo del juego=====
#============================

while True:
    lista_frutas="o","*","#","t","$"
    frutaa=random.randint(0,4) 
    trut=lista_frutas[frutaa]   
    #leemos la tecla
    tecla = pantalla.getch()        
    #le asignamos una dirección a cada cursor
    if tecla==curses.KEY_LEFT:
        mov_horizontal = -1
        mov_vertical = 0
    elif tecla==curses.KEY_RIGHT:
        mov_horizontal = 1
        mov_vertical = 0
    elif tecla==curses.KEY_UP:
        mov_horizontal = 0
        mov_vertical = -1
    elif tecla==curses.KEY_DOWN:
        mov_horizontal = 0
        mov_vertical = 1

    elif tecla==10:
        break
    
    x = (x + mov_horizontal) % ancho
    y = (y + mov_vertical) % alto

    posicion=[y,x]

    #si nos comemos una parte de snake, el juego se enoja y se sale    
    if posicion in snake:
        break

    snake.insert(0,posicion)    
    #ponemos una pausa, probá que sucede si la comentás
    time.sleep(0.1)

    #verificamos si nos morfamos una fruta
    if fruta in snake:        
        fruta=[random.randrange(alto),random.randrange(ancho)]
        pantalla.addstr(fruta[0],fruta[1],trut)
        suma_puntaje=1+suma_puntaje
    #sino, borramos la colita
    else:
        ultimaposicion = snake.pop()
        pantalla.addstr(ultimaposicion[0],ultimaposicion[1]," ")

    #dibujamos la cabeza
    pantalla.addstr(snake[0][0],snake[0][1],"#")

    #pantalla.addstr(y,x, "#")   
print(suma_puntaje)   
#Ponemos todo en su lugar    
curses.nocbreak()
pantalla.keypad(False)
curses.echo()
curses.endwin()
'''
stdscr = curses.initscr()
while True:
    c = stdscr.getch()
    if c == ord('p'):
        print("perra")
    elif c == ord('q'):
        break  # Exit the while loop
    elif c == ord("w"):
        
    elif c == curses.KEY_HOME:
        x = y = 0
'''