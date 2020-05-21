import PySimpleGUI as sg
from test import filesOnly
import math

def RepeatBox(num):
    return sg.Checkbox(f'{filesOnly[num]}', size=(18, 1), font='Any 7')
	
def TrueBox(a):
    RowNum=math.floor(len(a)/9)
    ModList=[]
    Remainder=len(a)%9
    if (RowNum > 0):
        for j in range(0,RowNum-1):
            ModList.append([RepeatBox(i) for i in range(j*9,(j+1)*9)])
    if (Remainder > 0):
        ModList.append([RepeatBox(i) for i in range(RowNum*9,(Remainder+(RowNum*9)))])
    for z in range(RowNum+1,33):
        ModList.append('')
    print(ModList)
    return ModList