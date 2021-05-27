import curses

stdscr=curses.initscr()

curses.noecho()

key=stdscr.getch()
stdscr.sddstr(str(key))
key=stdscr.getch()


curses.endwin()