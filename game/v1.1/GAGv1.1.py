#-------------------------------------------------------------------------------
#
#   Title:  Grids and Grime v1.1
#
#  Author:  David King (pythongratis)
#    Date:  D 27 / M 02 / Y 2014
#
#	Copyright (C) 2014
#
#-------------------------------------------------------------------------------

import easygui



def text(txtfile):
    return open("\\GridsandGrime\\game\\v1.1\\texts\\room%s.txt"%txtfile).read()

def acts(directions):
    return directions + player.items

def item(item):
    if item == "Action: Stone":
        easygui.msgbox("You have found 50 coins! You now have 200!",title)



class Entity: #Player Specific
    def __init__(self):
        self.coins = 150
        self.items = ["Action: Stone", "Action: Dagger", "Action: Potion"]



d = ["Move: Up","Move: Down","Move: Left","Move: Right"]
o = "easygui.choicebox(text(room),title,moves)"

#Creates the player
player = Entity()

#Title for all windows
title = "GAG v1.1"



def window(room):
    if room == 1:
        moves = [d[1]]
        choice = eval(o)
        if choice in player.items:
            nores()
            window(1)
        else:
            window(9)
#repeat process for all rooms

