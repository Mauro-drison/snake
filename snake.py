import curses
import random
import time

alto=15
ancho=50

def jugadores():
    pantalla = curses.initscr()

    #============================
    #===inicializacion de curses=====
    #============================
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    pantalla.keypad(True)
    pantalla.nodelay(True)
    curses.start_color()
    random_colores=random.randint(0,5)
    lista_de_colores=[curses.COLOR_BLUE,curses.COLOR_CYAN,curses.COLOR_GREEN,curses.COLOR_RED,curses.COLOR_GREEN,curses.COLOR_YELLOW]
    curses.init_pair(1, lista_de_colores[random_colores], lista_de_colores[random_colores])
    #============================
    #===inicializacion de snake=====
    #===y de la fruta=====
    #============================

    lista_frutas="o","*","#","m","$"
    #frutaa=random.randint(0,4)
    trut="?"
    x=0 
    y=0
    snake=[[y,x]]
    fruta=[random.randrange(alto),random.randrange(ancho)]
    pantalla.addstr(fruta[0],fruta[1], trut, curses.color_pair(1))
    pantalla.addstr(17,0, "Para agregar otro jugador precion la tecla f2")
    pantalla.addstr(19,0, "jugará primero el jugar que se integre, luego jugará el que estaba jugando por primera vez")
    mov_horizontal = 1
    mov_vertical = 0
    

    pantalla.refresh()
    
    
    #suma de puntaje
    suma_puntaje=0
    sumastr=str(suma_puntaje)
    pantalla.addstr(16,0,"PUNTAJE:"+sumastr)
    #============================
    #===comienzo del juego=====
    #============================

    while True:
        #lista_frutas="o","*","#","t","$"
        #frutaa=random.randint(0,4) 
          

        #colores
        random_colores=random.randint(0,5)
        lista_de_colores=[curses.COLOR_BLUE,curses.COLOR_CYAN,curses.COLOR_GREEN,curses.COLOR_RED,curses.COLOR_GREEN,curses.COLOR_YELLOW]
        curses.init_pair(1, lista_de_colores[random_colores], lista_de_colores[random_colores]) 
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
        elif tecla==curses.KEY_F2:
            
            jugadores()

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
            pantalla.addstr(fruta[0],fruta[1], "#", curses.color_pair(1))
            suma_puntaje=1+suma_puntaje
            sumastr=str(suma_puntaje)
            pantalla.addstr(16,0,"PUNTAJE:"+sumastr)
        #sino, borramos la colita
        else:
            ultimaposicion = snake.pop()
            pantalla.addstr(ultimaposicion[0],ultimaposicion[1]," ")

        #dibujamos la cabeza
        pantalla.addstr(snake[0][0],snake[0][1],"#")
    #Ponemos todo en su lugar    
    curses.nocbreak()
    pantalla.keypad(False)
    curses.echo()
    curses.endwin()
    print("Puntaje del jugador:",suma_puntaje)
        #pantalla.addstr(y,x, "#")   

jugadores()
