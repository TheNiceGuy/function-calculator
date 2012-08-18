# -*-coding:Latin-1 -*
#-------------------------MODULE------------------------------
from Tkinter import *
from ttk import *
import sys
import os
import Pmw
import mtTkinter as Tkinter
from package.function.volumefunction import *
from package.function.airefunction import *
from package.function.pythagorefunction import *
from package.function.basefunction import *
#-------------------------CLASS-------------------------------
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        quitbutton = Button(
                    self,
                    width   = 20,
                    command = self.quit,
                    text    = "Quit")
        quitbutton.place()
        self.validate = (self.register(self.OnValidate), '%d', '%i', '%s', '%S')
        #------------------------ENTRY VARIABLE
        #0 = Does It Have An Entry?
        #1 = Variable Type
        self.globalvariable = [[True , float()], # 0 = airelargeur
                               [True , float()], # 1 = airelongeur
                               [True , float()], # 2 = airerayon
                               [True , float()], # 3 = aireapotheme
                               [True , float()], # 4 = airenombrecote
                               [True , float()], # 5 = volumelargeur
                               [True , float()], # 6 = volumelongeur
                               [True , float()], # 7 = volumehauteur
                               [True , float()], # 8 = volumerayon
                               [True , float()], # 9 = volumeapotheme
                               [True , float()], #10 = volumenombrecote
                               [True , float()], #11 = Cathète 1
                               [True , float()], #12 = Cathète 2
                               [True , float()], #13 = Hypoténuse
                               [False, float()]] #14 = base
        #------------------------LIST TAB/PAGE
        self.pagelistinfo  = [["Aire"     , False],
                              ["Volume"   , True ],
                              ["Pythagore", False],
                              ["Console"  , False]]
        self.pagelist      = []
        #------------------------LIST GROUP
        #0 = Tab Index
        #1 = Widget Name
        #2 = Widget Row
        #3 = Widget Column
        #4 = Widget Padx
        #5 = Widget Pady
        #6 = Widget Sticky
        #7 = Widget Columnspan
        self.grouplistinfo = [[0, "Mode"    , 0, 0, 5, 5, W+E+N+S, 1], # 0
                              [0, "Variable", 0, 1, 5, 5, W+E+N+S, 1], # 1
                              [0, "Calcul"  , 1, 0, 5, 5, W+E+N+S, 3], # 2
                              [1, "Mode"    , 0, 0, 5, 5, W+E+N+S, 1], # 3
                              [1, "Base"    , 0, 1, 5, 5, W+E+N+S, 1], # 4
                              [1, "Variable", 0, 2, 5, 5, W+E+N+S, 1], # 5
                              [1, "Calcul"  , 1, 0, 5, 5, W+E+N+S, 3], # 6
                              [2, "Mode"    , 0, 0, 5, 5, W+E+N+S, 1], # 7
                              [2, "Variable", 0, 1, 5, 5, W+E+N+S, 1], # 8
                              [2, "Calcul"  , 1, 0, 5, 5, W+E+N+S, 3], # 9
                              [3, "Console" , 1, 0, 5, 5, W+E+N+S, 1]] #10
        self.grouplist     = []
        #------------------------LIST RADIO VAR
        # If There Is A Base, It MUST Be The Next Var
        self.radiovariable = [IntVar(), #0 = Aire Mode Variable
                              IntVar(), #1 = Volume Mode Variable
                              IntVar(), #2 = Volume Base Variable
                              IntVar()] #3 = Pythagore Mode Variable
        #------------------------LIST RADIO BUTTON
        # 0 = Group Index
        # 1 = Widget Name
        # 2 = Widget Variable
        # 3 = Widget Command
        # 4 = Widget Row
        # 5 = Widget Column
        # 6 = Widget Sticky
        # 7 = Need Base:
        #     None  = Base
        #     False = Don't Need Base
        #     True  = Need Base
        # 8 = Entry Needed:
        #     0 = Don't Need This Entry
        #     1 = Depends Of The Base/Mode
        #     2 = Need This Entry
        #     3 = Don't Touch This Entry
        # 9 = Widget Value
        #10 = Widget Index
        #11 = Tab Index
        #12 = Var Index
        #13 = Var Link Index
        #14 = Radio Index To Disabled/Enable
        #     [0] = Start Of Index
        #     [1] = End Of Index
        self.radiolistinfo = [[0, "Triangle"  , self.radiovariable[0], lambda: self.radiobuttoneven(0) , 0, 0, W, False, [2, 0, 0, 2, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3], 0 , 0, 0, 0, 0, [0, 0]], # 0
                              [0, "Rectangle" , self.radiovariable[0], lambda: self.radiobuttoneven(1) , 1, 0, W, False, [2, 2, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3], 1 , 1, 0, 0, 0, [0, 0]], # 1
                              [0, "Polygone"  , self.radiovariable[0], lambda: self.radiobuttoneven(2) , 2, 0, W, False, [2, 0, 0, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3], 2 , 2, 0, 0, 0, [0, 0]], # 2
                              [0, "Cercle"    , self.radiovariable[0], lambda: self.radiobuttoneven(3) , 3, 0, W, False, [0, 0, 2, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3], 3 , 3, 0, 0, 0, [0, 0]], # 3
                              [3, "Prisme"    , self.radiovariable[1], lambda: self.radiobuttoneven(4) , 0, 0, W, True , [3, 3, 3, 3, 3, 1, 1, 2, 1, 1, 1, 3, 3, 3], 4 , 4, 1, 1, 2, [7, 9]], # 4
                              [3, "Pyramide"  , self.radiovariable[1], lambda: self.radiobuttoneven(5) , 1, 0, W, True , [3, 3, 3, 3, 3, 1, 1, 2, 1, 1, 1, 3, 3, 3], 5 , 1, 1, 1, 2, [7, 9]], # 5
                              [3, "Sphere"    , self.radiovariable[1], lambda: self.radiobuttoneven(6) , 2, 0, W, False, [3, 3, 3, 3, 3, 0, 0, 0, 2, 0, 0, 3, 3, 3], 6 , 2, 1, 1, 0, [7, 9]], # 6
                              [4, "Rectangle" , self.radiovariable[2], lambda: self.radiobuttoneven(7) , 0, 0, W, None , [3, 3, 3, 3, 3, 1, 1, 0, 0, 0, 0, 3, 3, 3], 7 , 0, 1, 2, 1, [0, 0]], # 7
                              [4, "Polygone"  , self.radiovariable[2], lambda: self.radiobuttoneven(8) , 1, 0, W, None , [3, 3, 3, 3, 3, 1, 0, 0, 0, 1, 1, 3, 3, 3], 8 , 1, 1, 2, 1, [0, 0]], # 8
                              [4, "Cercle"    , self.radiovariable[2], lambda: self.radiobuttoneven(9) , 2, 0, W, None , [3, 3, 3, 3, 3, 0, 0, 0, 1, 0, 0, 3, 3, 3], 9 , 2, 1, 2, 1, [0, 0]], # 9
                              [7, "Hypoténuse", self.radiovariable[3], lambda: self.radiobuttoneven(10), 0, 0, W, False, [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 0], 10, 2, 1, 2, 1, [0, 0]], #10
                              [7, "Cathète"   , self.radiovariable[3], lambda: self.radiobuttoneven(11), 1, 0, W, False, [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2], 11, 2, 1, 2, 1, [0, 0]]] #11
        self.radiolist     = []
        #------------------------LIST LABEL/ENTRY FOR DATA INPUT
        #0 = Group Index
        #1 = Widget Width In Letter
        #2 = Widget Name
        #3 = System Name
        #4 = Widget Row
        #5 = Widget Column
        #6 = Widget Padx
        #7 = Widget Pady
        self.entrylistinfo = [[1, 15, "Largeur/Mesure Coté", "airelargeur"     , 0, 1, 5, 5], # 0
                              [1, 15, "Longeur"            , "airelongeur"     , 1, 1, 5, 5], # 1
                              [1, 15, "Rayon"              , "airerayon"       , 2, 1, 5, 5], # 2
                              [1, 15, "Apotheme"           , "aireapotheme"    , 3, 1, 5, 5], # 3
                              [1, 15, "Nombre Coté"        , "airenombrecote"  , 4, 1, 5, 5], # 4
                              [5, 15, "Largeur/Mesure Coté", "volumelargeur"   , 0, 1, 5, 5], # 5
                              [5, 15, "Longeur"            , "volumelongeur"   , 1, 1, 5, 5], # 6
                              [5, 15, "Hauteur"            , "volumehauteur"   , 2, 1, 5, 5], # 7
                              [5, 15, "Rayon"              , "volumerayon"     , 3, 1, 5, 5], # 8
                              [5, 15, "Apotheme"           , "volumeapotheme"  , 4, 1, 5, 5], # 9
                              [5, 15, "Nombre Coté"        , "volumenombrecote", 5, 1, 5, 5], #10
                              [8, 15, "Cathète 1"          , "cathète1"        , 0, 1, 5, 5], #11
                              [8, 15, "Cathète 2"          , "cathète2"        , 1, 1, 5, 5], #12 
                              [8, 15, "Hypoténuse"         , "hypoténuse"      , 2, 1, 5, 5]] #13
        self.entrylist     = []
        #------------------------LIST LABEL/ENTRY FOR RESULT INPUT
        #0 = Group Index
        #1 = Widget Name
        #2 = Widget Row
        #3 = Widget Column
        #4 = Widget Padx
        #5 = Widget Pady
        self.entryresultlistinfo = [[2, 40, 0, 5, 5, 5, W+E], #TAB 0 RESULT ENTRY
                                    [6, 40, 0, 5, 5, 5, W+E], #TAB 1 RESULT ENTRY
                                    [None,],
                                    [9, 40, 0, 5, 5, 5, W+E]] #TAB 2 RESULT ENTRY
        self.entryresultlist     = []
        #------------------------LIST BUTTON
        #0 = Group Index
        #1 = Widget Width In Letter
        #2 = Widget Name
        #3 = Widget Row
        #4 = Widget Column
        #5 = Widget Padx
        #6 = Widget Pady
        #7 = Widget Command
        self.buttonlistinfo = [[2, 10, "Calculer", 0, 0, 5, 5, lambda: self.calculer(0)],
                               [6, 10, "Calculer", 0, 0, 5, 5, lambda: self.calculer(1)],
                               [9, 10, "Calculer", 0, 0, 5, 5, lambda: self.calculer(3)]]
        self.buttonlist     = []
        #------------------------LIST FORMULE/BASE FUNCTION
        self.functionlistinfo = [lambda arglist = self.globalvariable:      triangle(self.globalvariable), # 0
                                 lambda arglist = self.globalvariable:     rectangle(self.globalvariable), # 1
                                 lambda arglist = self.globalvariable:      polygone(self.globalvariable), # 2
                                 lambda arglist = self.globalvariable:        cercle(self.globalvariable), # 3
                                 lambda arglist = self.globalvariable:        prisme(self.globalvariable), # 4
                                 lambda arglist = self.globalvariable:      pyramide(self.globalvariable), # 5
                                 lambda arglist = self.globalvariable:        sphere(self.globalvariable), # 6
                                 lambda arglist = self.globalvariable: baserectangle(self.globalvariable), # 7
                                 lambda arglist = self.globalvariable:  basepolygone(self.globalvariable), # 8
                                 lambda arglist = self.globalvariable:    basecercle(self.globalvariable), # 9
                                 lambda arglist = self.globalvariable:   hypothenuse(self.globalvariable), #10
                                 lambda arglist = self.globalvariable:       cathete(self.globalvariable)] #11
        #Create all the group, notebook tab, console and the widget
        self.creategroups()
        self.createconsole()
        self.createwidgets()
        #Select the default radiobutton
        for index in [0, 4, 7, 10]:   
            self.radiolist[index].invoke()
            self.radiobuttoneven(index)
        #Update the window size
        self.notebook.setnaturalsize()

    def creategroups(self):
        self.notebook = Pmw.NoteBook()
        self.notebook.grid()
        #------------------------WIDGET TAB/PAGE
        for listinfo in self.pagelistinfo:
            page = self.notebook.add(listinfo[0])
            self.pagelist.append(page)

        #------------------------WIDGET GROUP    
        for listinfo in self.grouplistinfo:
            widget = Pmw.Group(
                    self.pagelist[listinfo[0]],
                    tag_text   = listinfo[1])
            widget.grid(
                    row        = listinfo[2],
                    column     = listinfo[3],
                    padx       = listinfo[4],
                    pady       = listinfo[5],
                    sticky     = listinfo[6],
                    columnspan = listinfo[7])
            self.grouplist.append(widget)
                    
    def createwidgets(self):
        #------------------------WIDGET RADIO BUTTON
        for listinfo in self.radiolistinfo:
            widget = Radiobutton(
                    self.grouplist[listinfo[0]].interior(),
                    text       = listinfo[1],
                    value      = listinfo[9],
                    variable   = listinfo[2],
                    command    = listinfo[3])
            widget.grid(
                    row        = listinfo[4],
                    column     = listinfo[5],
                    sticky     = listinfo[6])
            self.radiolist.append(widget)
        #------------------------WIDGET LABEL/ENTRY FOR DATA INPUT
        for listinfo in self.entrylistinfo:
            widgetlabel = Label(
                    self.grouplist[listinfo[0]].interior(),
                    text       = listinfo[2])
            widgetlabel.grid(
                    row        = listinfo[4],
                    column     = listinfo[5])
            widgetentry = Entry(
                    self.grouplist[listinfo[0]].interior(),
                    width      = listinfo[1],
                    validate   = "key")
            widgetentry.grid(
                    row        = listinfo[4],
                    column     = listinfo[5] + 1,
                    padx       = listinfo[6],
                    pady       = listinfo[7])
            widgetentry["validatecommand"] = self.validate
            widgetentry.insert(0, 0)
            self.entrylist.append(widgetentry)
        #------------------------WIDGET LABEL/ENTRY FOR RESULT INPUT
        for listinfo in self.entryresultlistinfo:
            if listinfo[0] != None:
                widget = Entry(
                        self.grouplist[listinfo[0]].interior(),
                        width      = listinfo[1],)
                widget.grid(
                        row        = listinfo[2],
                        column     = listinfo[3],
                        padx       = listinfo[4],
                        pady       = listinfo[5],
                        sticky     = listinfo[6])
                widget.insert(0, 0)
                self.entryresultlist.append(widget)
            else:
                self.entryresultlist.append(None)
        print self.entryresultlist
        #------------------------WIDGET BUTTON FOR RESULT INPUT
        for listinfo in self.buttonlistinfo:
            widget = Button(
                    self.grouplist[listinfo[0]].interior(),
                    width      = listinfo[1],
                    text       = listinfo[2],
                    command    = listinfo[7])
            widget.grid(
                    row        = listinfo[3],
                    column     = listinfo[4],
                    padx       = listinfo[5],
                    pady       = listinfo[6],)
            self.buttonlist.append(widget)
    
    def createconsole(self):
        #Create the console text widget
        self.consoleoutput = Text(
                    self.grouplist[10].interior(),
                    width      = 47,
                    heigh      = 15,
                    background = "black",
                    foreground = "white",
                    state      = "disabled")
        #Grid the text widget
        self.consoleoutput.grid(
                    row        = 0,
                    column     = 0,
                    padx       = 0,
                    pady       = 5,)
        #Create a scroll bar for the text widget
        self.consolescroll = Scrollbar(
                    self.grouplist[10].interior())
        #Grid the scroll bar
        self.consolescroll.grid(
                    row        = 0,
                    column     = 1,
                    ipady      = 97)
        #Link the scroll bar to the console text widget
        self.consoleoutput.config(yscrollcommand=self.consolescroll.set)
        self.consolescroll.config(command=self.consoleoutput.yview)
        
    def OnValidate(self, d, i, s, S,):
        #This function validate if the entered number
        #in a entry widget is a number that contain
        #only number, "-" and dot "."
        #
        #Check if the entered value is a "-" and their is 
        #no other "-"
        if S == "-" and s.count('-') != 1 and int(i) == 0:
            return True
        #Check if it delete something
        # 1 = Insert Input
        # 0 = Delete Input
        #-1 = Other Input
        elif d == "0":
            return True
        #Except an error if the enterd value is not a number
        try:
            #Check if it a number, convert the string to a int,
            #Ex: "a" cannot be convert to int, it return a error
            return int(S) >= 0 and int(S) <= 9
        except:
            #A dot cannot be converted to a int
            #Check if it a dot
            if S == "." and s.count('.') != 1:
                return True
            #Probably a letter
            return False
    
    def calculer(self, indexnumber):
        #indexnumber = The tab index
        #This loop will refresh all the variable in the global
        #variable list.
        for index, number in enumerate(self.globalvariable):
            #Check if the global vatiable have a entry
            if self.globalvariable[index][0] == True:
                #Check if there is something in the entry
                if self.entrylist[index].get() != "":
                    #Set the global variable to the entry value
                    self.globalvariable[index][1] = float(self.entrylist[index].get())
                else:
                    #If there is nothing in the entry set it to 0
                    self.globalvariable[index][1] = 0
        #Get the variable value of the radio button we need
        radiomodeindex = self.radiovariable[indexnumber].get()
        #Check if we need a base
        if self.radiolistinfo[radiomodeindex][7] == True:
            #Execute the function for the base
            radiobaseindex             = self.radiovariable[indexnumber + 1].get()
            base                       = self.functionlistinfo[radiobaseindex]()
            self.globalvariable[11][1] = base
        #Execute the function for the result
        result = self.functionlistinfo[radiomodeindex](self.globalvariable)
        #Insert the result in the correct entry
        self.entryresultlist[indexnumber].delete(0, END)
        self.entryresultlist[indexnumber].insert(END, result)

    def radiobuttoneven(self, value):
        tabindex = self.radiolistinfo[value][11]
        needbase = self.radiolistinfo[value][7]
        newlist = []

        if needbase == False:
            if self.radiolistinfo[value][14][0] == 0 and self.radiolistinfo[value][14][1] == 0:
                pass
            else:
                start = self.radiolistinfo[value][14][0]
                end   = self.radiolistinfo[value][14][1]
                for index, widget in enumerate(self.radiolist[start:end + 1], start):
                    widget["state"] = "disabled"
            newlist = self.radiolistinfo[value][8] 
                    
        elif needbase == True:
            start        = self.radiolistinfo[value][14][0]
            end          = self.radiolistinfo[value][14][1]
            basevarindex = self.radiolistinfo[value][13]
            base         = self.radiovariable[basevarindex].get()
            listmode     = self.radiolistinfo[value][8]
            listbase     = self.radiolistinfo[base] [8]
            
            for a, b in zip(listmode, listbase):
                if a == 3 or b == 3:
                    newlist.append(3)
                else:
                    c = a + b
                    newlist.append(c)
            for index, widget in enumerate(self.radiolist[start:end + 1], start):
                widget["state"] = "normal"
        elif needbase == None:
            modevarindex = self.radiolistinfo[value][13]
            mode         = self.radiovariable[modevarindex].get()
            listmode     = self.radiolistinfo[mode] [8]
            listbase     = self.radiolistinfo[value][8]
            
            for a, b in zip(listmode, listbase):
                if a == 3 or b == 3:
                    newlist.append(3)
                else:
                    c = a + b
                    newlist.append(c)
            
        for index, number in enumerate(newlist):
            if number == 0 or number == 1:
                self.entrylist[index]["state"] = "disabled"
            if number == 2:
                self.entrylist[index]["state"] = "normal"
#--------------------------MAIN-------------------------------
if __name__ == "__main__": 
    os.system("pause")