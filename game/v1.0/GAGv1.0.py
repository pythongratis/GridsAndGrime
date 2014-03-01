#-------------------------------------------------------------------------------
#
#   Title:  Grids and Grime v1.0
#
#  Author:  David King (pythongratis)
#    Date:  D 27 / M 02 / Y 2014
#
#	Copyright (C) 2014
#
#-------------------------------------------------------------------------------

import easygui

class Room: #Room specific
    def __init__(self,txtfile,actreq):
        self.txtfile = open("\\gridsandgrime\\game\\v1.0\\texts\\%s.txt"%txtfile).read()
        self.visited = False
        self.acted = False if actreq == True else None
    def setacts(self, directions):
        self.acts = directions + player.items

class Entity: #Player Specific
    def __init__(self):
        self.coins = 150
        self.items = ["Action: Stone", "Action: Dagger", "Action: Potion"]


#faster way to check that rooms have been visited
visitcount = 0
actedcount = 0

#Creates the player
player = Entity()

#Title for all windows
title = "GAG v1.0"

#Sets the room variables
intro = Room("intro",False)

r1 = Room("room1",False)
r1.setacts(["Move: Down"])

r2 = Room("room2",False)
r2.setacts(["Move: Down"])

r3 = Room("room3",False)
r3.setacts(["Move: Down","Move: Right"])

r4 = Room("room4",False)
r4.setacts(["Move: Left","Move: Right"])

r5 = Room("room5",False)
r5.setacts(["Move: Up","Move: Down","Move: Left","Move: Right"])

r6 = Room("room6",False)
r6.setacts(["Move: Left","Move: Right"])

r7 = Room("room7",False)
r7.setacts(["Move: Up","Move: Left"])

r8 = Room("room8",False)
r8.setacts(["Move: Up","Move: Down"])

r9 = Room("room9",True)
r9.setacts(["Move: Up"])

r10 = Room("room10",False)
r10.setacts(["Move: Up"])


#If user select cancel
def stop():
    easygui.msgbox("You quit the game!",title)
    quit()


# Nothing Happened
def nores():
    easygui.msgbox("Nothing Happened!",title)


# Checks that all rooms have been visited and all posible actions performed
def allvisited():
    global actedcount
    global visitcount
    if visitcount == 10 and actedcount == 1:
        #Exited the while loop - all rooms visited, all actions performed
        easygui.msgbox(open("\\gridsandgrime\\game\\texts\\end.txt").read(),title)
        quit()

def introduction():
    allvisited()
    global visitcount
    if r1.visited == False:
        r1.visited = True
        visitcount += 1
    choice = easygui.choicebox(intro.txtfile,title,r1.acts)
    if choice in player.items:
        nores()
        introduction()
    elif choice == "Move: Down":
        room5()
    else:
        stop()

def room1(): #Identical to introduction() but after leaving the intro stage
    allvisited()
    r1.setacts(["Move: Down"])
    global visitcount
    if r1.visited == False:
        r1.visited = True
        visitcount += 1
    choice = easygui.choicebox(r1.txtfile,title,r1.acts)
    if choice in player.items:
        nores()
        room1()
    elif choice == "Move: Down":
        room5()
    else:
        stop()

#the room numbers do not reflect any order see \resources\map.pdf
def room2():
    allvisited()
    r2.setacts(["Move: Down"])
    global visitcount
    if r2.visited == False:
        r2.visited = True
        visitcount += 1
    choice = easygui.choicebox(r2.txtfile,title,r2.acts)
    if choice in player.items:
        nores()
        room2()
    elif choice == "Move: Down":
        room7()
    else:
        stop()

def room3():
    allvisited()
    r3.setacts(["Move: Down","Move: Right"])
    global visitcount
    if r3.visited == False:
        r3.visited = True
        visitcount += 1
    choice = easygui.choicebox(r3.txtfile,title,r3.acts)
    if choice in player.items:
        nores()
        room3()
    elif choice == "Move: Right":
        room4()
    elif choice == "Move: Down":
        room8()
    else:
        stop()

def room4():
    allvisited()
    r4.setacts(["Move: Left","Move: Right"])
    global visitcount
    if r4.visited == False:
        r4.visited = True
        visitcount += 1
    choice = easygui.choicebox(r4.txtfile,title,r4.acts)
    if choice in player.items:
        nores()
        room4()
    elif choice == "Move: Right":
        room5()
    elif choice == "Move: Left":
        room3()
    else:
        stop()

def room5():
    allvisited()
    r5.setacts(["Move: Up","Move: Down","Move: Left","Move: Right"])
    global visitcount
    if r5.visited == False:
        r5.visited = True
        visitcount += 1
    choice = easygui.choicebox(r5.txtfile,title,r5.acts)
    if choice in player.items:
        nores()
        room5()
    elif choice == "Move: Up":
        room1()
    elif choice == "Move: Down":
        room9()
    elif choice == "Move: Left":
        room4()
    elif choice == "Move: Right":
        room6()
    else:
        stop()

def room6():
    allvisited()
    r6.setacts(["Move: Left","Move: Right"])
    global visitcount
    if r6.visited == False:
        r6.visited = True
        visitcount += 1
    choice = easygui.choicebox(r6.txtfile,title,r6.acts)
    if choice in player.items:
        nores()
        room6()
    elif choice == "Move: Left":
        room5()
    elif choice == "Move: Right":
        room7()
    else:
        stop()

def room7():
    allvisited()
    r7.setacts(["Move: Up","Move: Left"])
    global visitcount
    if r7.visited == False:
        r7.visited = True
        visitcount += 1
    choice = easygui.choicebox(r7.txtfile,title,r7.acts)
    if choice in player.items:
        nores()
        room7()
    elif choice == "Move: Up":
        room2()
    elif choice == "Move: Left":
        room6()
    else:
        stop()

def room8():
    allvisited()
    r8.setacts(["Move: Up","Move: Down"])
    global visitcount
    if r8.visited == False:
        r8.visited = True
        visitcount += 1
    choice = easygui.choicebox(r8.txtfile,title,r8.acts)
    if choice in player.items:
        nores()
        room8()
    elif choice == "Move: Up":
        room3()
    elif choice == "Move: Down":
        room10()
    else:
        stop()

def room9():
    allvisited()
    r9.setacts(["Move: Up"])
    global actedcount
    global visitcount
    if r9.visited == False:
        r9.visited = True
        visitcount += 1
    choice = easygui.choicebox(r9.txtfile,title,r9.acts)
    if choice == "Action: Stone":
        player.items.remove("Action: Stone") #Deatils about items - \resources\items.txt
        easygui.msgbox("You threw your stone at the target.",title)
        easygui.msgbox("You found 50 coins!",title)
        easygui.msgbox("You now have 200 coins.",title)
        player.coins += 50
        r9.acted = True
        actedcount += 1
        room9()
    elif choice in player.items:
        nores()
        room9()
    elif choice == "Move: Up":
        room5()
    else:
        stop()

def room10():
    allvisited()
    r10.setacts(["Move: Up"])
    global visitcount
    if r10.visited == False:
        r10.visited = True
        visitcount += 1
    choice = easygui.choicebox(r10.txtfile,title,r10.acts)
    if choice in player.items:
        nores()
        room10()
    elif choice == "Move: Up":
        room8()
    else:
        stop()

introduction() # Starts the game at the introductory point