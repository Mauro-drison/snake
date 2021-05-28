import curses
stdscr=curses.initscr()

#para silenciar la tecla que precionamos
#curses.noecho()

#pondemos mostrar una tecla por comando
#key=stdscr.getch()
#stdscr.addstr(str(key))
#key=stdscr.getch()

#sirve para mover el cursor en x e y
#stdscr.move(3, 10)
#stdscr.getch()

#para utilizar colores
curses.start_color()
#para darle el color: el primer parametro es el del texto y el segundo es el del fondo 
curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)

stdscr.addnstr("hola mundo", curses.color_pair(3))
stdscr.getch()


curses.endwin()