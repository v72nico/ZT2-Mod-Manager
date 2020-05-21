import PySimpleGUI as sg
import os
from test import modfiles, filesOnly, totalfiles, activelen
from rowmanage1 import RepeatBox
import subprocess

try:
    os.mkdir("C:\\Program Files (x86)\\Microsoft Games\\Zoo Tycoon 2\\ModsNotinUse\\")
except:
    print("Directory Present or failed")
else:
    print("Directory Created")

print(totalfiles)

sg.theme('DarkAmber')





def TrueBox(num):   
    MODSPERROW = 9
    returnList = []
    counter = -1
    for i in range(0, len(num)):
        if i % MODSPERROW == 0:
            counter += 1
    #counter is number of times MODSPERROW is reached
    for i in range(1, counter+1):
        returnList.append([RepeatBox(j) for j in range(i*MODSPERROW - MODSPERROW, i*MODSPERROW)])
    returnList.append([RepeatBox(i) for i in range((counter)*MODSPERROW, len(num))])
    for i in range(counter+2, 47):
        returnList.append('')
    return returnList


layout = [ [sg.Text('Check the mods you would like to use')],
           TrueBox(filesOnly)[0],
           TrueBox(filesOnly)[1],
           TrueBox(filesOnly)[2],
           TrueBox(filesOnly)[3],
           TrueBox(filesOnly)[4],
           TrueBox(filesOnly)[5],
           TrueBox(filesOnly)[6],
           TrueBox(filesOnly)[7],
           TrueBox(filesOnly)[8],
           TrueBox(filesOnly)[9],
           TrueBox(filesOnly)[10],
           TrueBox(filesOnly)[11],
           TrueBox(filesOnly)[12],
           TrueBox(filesOnly)[13],
           TrueBox(filesOnly)[14],
           TrueBox(filesOnly)[15],
           TrueBox(filesOnly)[16],
           TrueBox(filesOnly)[17],
           TrueBox(filesOnly)[18],
           TrueBox(filesOnly)[19],
           TrueBox(filesOnly)[20],
           TrueBox(filesOnly)[21],
           TrueBox(filesOnly)[22],
           TrueBox(filesOnly)[23],
           TrueBox(filesOnly)[24],
           TrueBox(filesOnly)[25],
           TrueBox(filesOnly)[26],
           TrueBox(filesOnly)[27],
           TrueBox(filesOnly)[28],
           TrueBox(filesOnly)[29],
           TrueBox(filesOnly)[30],
           TrueBox(filesOnly)[31],
		   TrueBox(filesOnly)[32],
		   TrueBox(filesOnly)[33],
		   TrueBox(filesOnly)[34],
		   TrueBox(filesOnly)[35],
		   TrueBox(filesOnly)[36],
		   TrueBox(filesOnly)[37],
		   TrueBox(filesOnly)[38],
		   TrueBox(filesOnly)[39],
		   TrueBox(filesOnly)[40],
		   TrueBox(filesOnly)[41],
		   TrueBox(filesOnly)[42],
		   TrueBox(filesOnly)[43],
		   TrueBox(filesOnly)[44],
		   TrueBox(filesOnly)[45],
           [sg.Button('Submit'), sg.Button('Exit')]      ]

window = sg.Window('ZT2 Mod Manager').Layout(layout)
print(activelen)
print(len(totalfiles))

window.finalize()
for i in range(0, activelen):
    window[i].Update(True)
#for i in range(activelen, len(totalfiles)):
    #window[i].Update(True)
    
while True:             # Event Loop
    (event, values) = window.Read()
    print(event, values)
    if event is None or event == 'Exit':
        break
    if event == 'Submit':
        for i in range(0, len(totalfiles)):
            if values[i] == True:
                os.replace(totalfiles[i], "C:\\Program Files (x86)\\Microsoft Games\\Zoo Tycoon 2\\"+filesOnly[i])
        for i in range(0, len(totalfiles)):
            if values[i] == False:
                os.replace(totalfiles[i], "C:\\Program Files (x86)\\Microsoft Games\\Zoo Tycoon 2\\ModsNotinUse\\"+filesOnly[i])
        window.Close()
        subprocess.call(['C:\\Program Files (x86)\\Microsoft Games\\Zoo Tycoon 2\\Startup.exe'])
window.Close()