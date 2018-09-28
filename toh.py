from graphics import *

class rod:
    def __init__(self,discList,pos):
        self.discList = discList
        self.pos = pos
    
print("TOWER OF HANOI!")
x = int(input("How many disks? "))
width = int(50/x)
move = 0

win = GraphWin("My Window",1000,1000)
win.setBackground('black')

def clear(win):
    for item in win.items[:]:
        item.undraw()
    win.update()

def initText():
    txt = Text(Point(160,450),"SOURCE")
    txt.setTextColor('white')
    txt.setSize(20)
    txt.setFace('courier')
    txt.draw(win)

    txt = Text(Point(480,450),"AUXILIARY")
    txt.setTextColor('white')
    txt.setSize(20)
    txt.setFace('courier')
    txt.draw(win)

    txt = Text(Point(810,450),"DESTINATION")
    txt.setTextColor('white')
    txt.setSize(20)
    txt.setFace('courier')
    txt.draw(win)

    txt = Text(Point(470,100),"Moves: ")
    txt.setTextColor('white')
    txt.draw(win)
    txt = Text(Point(510,100),move)
    txt.setTextColor('white')
    txt.draw(win)

def initRods():
    base = Rectangle(Point(30,400),Point(930,415))
    base.setOutline('white')
    base.setFill('white')

    peg1 = Rectangle(Point(150,200),Point(160,400))
    peg1.setOutline('white')
    peg1.setFill('white')

    peg2 = Rectangle(Point(470,200),Point(480,400))
    peg2.setOutline('white')
    peg2.setFill('white')

    peg3 = Rectangle(Point(800,200),Point(810,400))
    peg3.setOutline('white')
    peg3.setFill('white')

    base.draw(win)
    peg1.draw(win)
    peg2.draw(win)
    peg3.draw(win)

def draw_configuration(beg,aux,end,move):
    clear(win)

    initText()

    initRods()

    # Destination Tower
    rodY = 390
    if(end.pos==1):
        endX = 150
    elif(end.pos==2):
        endX = 470
    elif(end.pos==3):
        endX = 800
    for disc in reversed(end.discList):
        startX = endX-disc*width
        startY = rodY
        endXX = endX+10+disc*width
        endY = rodY+8
        drawDisc = Rectangle(Point(int(startX),int(startY)),Point(int(endXX),int(endY)))
        drawDisc.setOutline('white')
        drawDisc.setFill('white')
        drawDisc.draw(win)
        rodY -= 10
    
    # Source Tower
    if(beg.pos==1):
        begX = 150
    elif(beg.pos==2):
        begX = 470
    elif(beg.pos==3):
        begX = 800
    rodY = 390
    for disc in reversed(beg.discList):
        startX = begX-disc*width
        startY = rodY
        endX = begX+10+disc*width
        endY = rodY+8
        drawDisc = Rectangle(Point(int(startX),int(startY)),Point(int(endX),int(endY)))
        drawDisc.setOutline('white')
        drawDisc.setFill('white')
        drawDisc.draw(win)
        rodY -= 10

    # Auxiliary Tower
    rodY = 390
    if(aux.pos==1):
        auxX = 150
    elif(aux.pos==2):
        auxX = 470
    elif(aux.pos==3):
        auxX = 800
    for disc in reversed(aux.discList):
        startX = auxX-disc*width
        startY = rodY
        endX = auxX+10+disc*width
        endY = rodY+8
        drawDisc = Rectangle(Point(int(startX),int(startY)),Point(int(endX),int(endY)))
        drawDisc.setOutline('white')
        drawDisc.setFill('white')
        drawDisc.draw(win)
        rodY -= 10

def hanoi(n,beg,aux,end):
    if(n>0):
        global move

        hanoi(n-1,beg,end,aux)
        
        # Push disc from source to destination
        top = beg.discList.pop(0)
        end.discList.insert(0,top)

        # Increment move and draw current configuration
        move += 1
        draw_configuration(beg,aux,end,move)
        time.sleep(1)

        hanoi(n-1,aux,beg,end)

def main():

    # Initialize the 3 towers
    iBeg = []
    iAux = []
    iEnd = []
    for i in range(1,x+1):
        iBeg.append(i)

    beg = rod(iBeg,1)
    aux = rod(iAux,2)
    end = rod(iEnd,3)

    # Draw initial configuration
    draw_configuration(beg,aux,end,move)
    time.sleep(1)
    
    hanoi(x,beg,aux,end)

    win.getMouse()
    win.close()

main()