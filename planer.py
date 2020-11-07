import datetime # is that really necesary to explain?
import curses # i use it for read keys (but more powerful)
import os  #run console commands 

def getTime( task , date ): #I use it to get the time with keys
    
    # assing parts of time 
    day = date.day
    month = date.month
    year = date.year

    # get the curses screen window
    screen = curses.initscr()
     
    # turn off input echoing
    curses.noecho()

    # respond to keys immediately (don't wait for enter)

    curses.cbreak()
    # map arrow keys to special values+

    screen.keypad(True)
    try:
        while True:
            screen.addstr(0,0, task)
            screen.addstr(1, 0, date.strftime("%d-%a, %B %Y" ))  

    #        screen.addstr(0, 0, s )  
    #        screen.refresh()
    #        curses.noecho()
            char = screen.getch()

            if char == ord('s'):
                break
           
            #Change day
            elif char == ord('d'): 


                if ( day == 30 ): #Verificar los dias 31, 30, 27 del mes ¿try?
                    day = 1
                    if ( month == 12 ): #Crear funciones que verifiquen
                        month = 1
                        year += 1
                    else:
                        month +=1 
                else: 
                    day += 1

                date = datetime.datetime(year, month, day)
                screen.addstr(1, 0, "                           " )  
                screen.addstr(1, 0, date.strftime("%d-%a, %B %Y" ))  

            #Change back day
            elif char == ord('D'): 
                if ( day == 1 ): #Verificar los dias 31, 30, 27 del mes ¿try?
                    day = 30
                    if ( month == 1 ): #Crear funciones que verifiquen
                        month = 12
                        year -= 1
                    else:
                        month-=1
                else: 
                    day -= 1

                date = datetime.datetime(year, month, day)
                screen.addstr(1, 0, "                           " )  
                screen.addstr(1, 0, date.strftime("%d-%a, %B %Y" ))  
     
            #Change month 
            elif char == ord('m'):
                if ( month == 12 ): #Crear funciones que verifiquen
                     month = 1
                     year += 1
                else:
                     month +=1 
                date = datetime.datetime(year, month, day)
                screen.addstr(1, 0, "                           " )  
                screen.addstr(1, 0, date.strftime("%d-%a, %B %Y" )) 
     
            #Change back month       
            elif char == ord('M'):
                if ( month == 1 ): #Crear funciones que verifiquen
                     month = 12
                     year -= 1
                else:
                     month -=1 
                date = datetime.datetime(year, month, day)
                screen.addstr(1, 0, "                           " )  
                screen.addstr(1, 0, date.strftime("%d-%a, %B %Y" )) 
     
            #Change year      
            elif char == ord('y'):
                year += 1
                date = datetime.datetime(year, month, day)
                screen.addstr(1, 0, "                           " )  
                screen.addstr(1, 0, date.strftime("%d-%a, %B %Y" ))

            #Change back year
            elif char == ord('Y'):
                year += -1
                date = datetime.datetime(year, month, day)
                screen.addstr(1, 0, "                           " )  
                screen.addstr(1, 0, date.strftime("%d-%a, %B %Y" ))
    finally:
        # shut down cleanly
        curses.nocbreak(); screen.keypad(0); curses.echo()
        curses.endwin()

    return date

def clear():
    # os.system('cls') # on windows 
    os.system('clear') # on Linux <3

# "MAIN" ---------------------------
hoy = datetime.datetime.now()

task = input("Nombre de la tarea: ")
newDate = getTime(task, hoy) 

clear()
print(task)
print(newDate.strftime("%d-%a, %B %Y"))
#------------------------------------






