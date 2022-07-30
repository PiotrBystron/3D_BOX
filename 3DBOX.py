import pyautogui as pg
import keyboard
import win32api
import sys


win32api.MessageBox(0, 
'''< - zapis lokalizacji unsure
> - zapis lokalizacji zmiany box-a

` - kliknij unsure
1 - wpisz XYZ obiektu 1
2 - wpisz XYZ obiektu 2
3 - wpisz XYZ obiektu 3
4 - wpisz XYZ obiektu 4
5 - wpisz XYZ obiektu 5

Naciśnij Q aby wyłączyć program''', 'Clicker')


def load_data(line_number):
    f = open('data.txt')
    data = f.read()
    line_data = []
    line = data.split('\n')[line_number]
    line_data = [i for i in line.split(",")]
    f.close()
    return line_data

def mouse_position():
    XYposition = pg.position()
    return XYposition

def save(position,XY):
    with open('data.txt', 'r') as file:
        data = file.readlines()
    
    data[position] = str(XY[0])+ ","+ str(XY[1])+"\n"

    with open('data.txt', 'w') as file:
        file.writelines(data)

    file.close()

def save_to_file(position):
    save(position,mouse_position())

def typing_XYZ(X,Y,Z):
    keyboard.write(X)
    keyboard.send("tab")
    keyboard.write(Y)
    keyboard.send("tab")
    keyboard.write(Z)
    keyboard.send("enter")

def options(arg):
    XYunsure=load_data(0)
    XYbox=load_data(1)
    DANE=load_data(2)

    match arg:
        case "<":
            #save unsure position
            save_to_file(0)

        case ">":
            #save XYZ box position
            save_to_file(1)

        case "`":
            #unsure click
            pg.moveTo(XYunsure)
            pg.leftClick()

        case "1":
            #object_1
            pg.moveTo(XYbox)
            pg.leftClick()
            typing_XYZ(DANE[1],DANE[2],DANE[3])
            
        case "2":
            #object_2
            pg.moveTo(XYbox)
            pg.leftClick()
            typing_XYZ(DANE[5],DANE[6],DANE[7])

        case "3":
            #object_3
            pg.moveTo(XYbox)
            pg.leftClick()
            typing_XYZ(DANE[9],DANE[10],DANE[11])

        case "4":
            #object_4
            pg.moveTo(XYbox)
            pg.leftClick()
            typing_XYZ(DANE[13],DANE[14],DANE[15])

        case "5":
            #object_5
            pg.moveTo(XYbox)
            pg.leftClick()
            typing_XYZ(DANE[17],DANE[18],DANE[19])

        case "q":
            win32api.MessageBox(0, 'Program został wyłączony', 'Clicker')
            sys.exit()

        
#car,4.2,2,1.5,transporter_slim,4.4,2,3,transporter,8, 2 ,4 ,truck_slim, 10.5, 3 , 6, truck, 16.5, 3  , 7
# 0   1  2  3       4            5  6 7      8      9 10  11   12        13   14  15    16    17   18  19


def clicker():

    while True:
        key = keyboard.read_key()
        options(key)


clicker()