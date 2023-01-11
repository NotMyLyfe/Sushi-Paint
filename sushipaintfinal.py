##Sushi Paint Project

###Imports
from pygame import *
from random import *
from math import *
from tkinter import *
from tkinter import filedialog
from statistics import *


playing=99          #playing is a variable to show if music is playing. The 99 is just there so that playing is defined before the loop.
stickerSelect=False #to check if a sticker/stamp is selected
toolSelect = False #to check if a tool is selected

#getting the font
init()
font.init() 
font = font.SysFont("Ink Free", 20, bold = False, italic = False)  #gets the font Ink Free with no bold and no italics


root = Tk() #window for save
root.withdraw() #takes away the window pop up

width,height=1515,840 #size of the screen

screen=display.set_mode((width,height)) #displays the screen

#colour variables
RED=(255,0,0)
GREY=(127,127,127)
BLACK=(0,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
YELLOW=(255,255,0)
WHITE=(255,255,255)
LIGHTBLUE = (168, 230, 247)
PINK = (242, 104, 116)
DARKYELLOW = (255, 195, 49)

col = BLACK #default colour

#####LOADING IMAGES#####
background = image.load("images/background.jpg") #loading background image
colourpicker = image.load("images/RGB.jpeg")     #loading colour picker image
###loading items images###
undo = image.load("images/items/undo.png")
redo = image.load("images/items/redo.png")
save = image.load("images/items/save.png")
op = image.load("images/items/open.png")
###loading tools images###
#pencils
penciloff = image.load("images/tools/pencil/penciloff.png")     #pencil when not clicked image
pencilhover = image.load("images/tools/pencil/pencilhover.png") #pencil when hovered over image
pencilon = image.load("images/tools/pencil/pencilon.png")           #pencil when used image
####The rest are similar to the pencil
#erasers
eraseroff = image.load("images/tools/eraser/eraseroff.png")
eraserhover = image.load("images/tools/eraser/eraserhover.png")
eraseron = image.load("images/tools/eraser/eraseron.png")
#brushes
brushoff = image.load("images/tools/brush/brushoff.png")
brushhover = image.load("images/tools/brush/brushhover.png")
brushon = image.load("images/tools/brush/brushon.png")
#spraypaints
sprayoff = image.load("images/tools/spraypaint/sprayoff.png")
sprayhover = image.load("images/tools/spraypaint/sprayhover.png")
sprayon = image.load("images/tools/spraypaint/sprayon.png")
#highlighter
highoff = image.load("images/tools/highlighter/highlighteroff.png")
highhover = image.load("images/tools/highlighter/highlighterhover.png")
highon = image.load("images/tools/highlighter/highlighteron.png")
#lines
lineoff= image.load("images/tools/line/lineoff.png")
linehover= image.load("images/tools/line/linehover.png")
lineon= image.load("images/tools/line/lineon.png")
#rectangles
rectoff= image.load("images/tools/rect/rectoff.png")
recthover= image.load("images/tools/rect/recthover.png")
recton= image.load("images/tools/rect/recton.png")
#ellipses
ellipseoff= image.load("images/tools/ellipse/ellipseoff.png")
ellipsehover= image.load("images/tools/ellipse/ellipsehover.png")
ellipseon = image.load("images/tools/ellipse/ellipseon.png")
#polygon
polyoff= image.load("images/tools/polygon/polygonoff.png")
polyhover= image.load("images/tools/polygon/polygonhover.png")
polyon = image.load("images/tools/polygon/polygonon.png")

#filters lanterns
filteroff= image.load("images/tools/filter/filteroff.png")
filterhover= image.load("images/tools/filter/filterhover.png")
filteron = image.load("images/tools/filter/filteron.png")

#Filters images
filters = ["images/filters/sepia.jpg","images/filters/grayscale.jpg"] #filter example images list
myfils = []             #empty list to contain loaded images
for fils in filters:            #loop to load images and append them to list
    fil = image.load(fils)
    myfils.append(fil)
    

###stickers###
normal = image.load("images/stickers/normal.png") #loading sticker images
roe = image.load("images/stickers/roe.png")
salmon2 = image.load("images/stickers/salmon2.png")
salmon = image.load("images/stickers/salmon.png")
grass = image.load("images/stickers/grass.png")
egg = image.load("images/stickers/egg.png")
sashimi = image.load("images/stickers/sashimi.png")
plate = image.load("images/stickers/plate.png")

#Loading music buttons images
#made a list with the unloaded image buttons
musicButtons = ["images/buttons/voldown.png","images/buttons/backward.png","images/buttons/pause.png","images/buttons/play.png","images/buttons/forward.png","images/buttons/volup.png"]
buttons = []            #empty list that will store loaded images
for musicButton in musicButtons:            #this loop will get each individual filename in the musicButtons list and load it
    button = image.load(musicButton)            #loads image
    buttons.append(button)          #appends it to a list
    
#loading images for text background
textFrame = image.load("images/text/textframe.png") 
coordinate = image.load("images/text/coordinate.png")

#music
songNames = ["music/Battle Music.mp3","music/Japanese Lanterns.mp3","music/sakura.mp3","music/Sushi.mp3","music/Tea Ceremony.mp3"] #list with all the song filenames
toolsOff = [penciloff,eraseroff,brushoff,sprayoff,highoff,lineoff,rectoff,ellipseoff,polyoff,filteroff]
toolsHover = [pencilhover,eraserhover,brushhover,sprayhover,highhover,linehover,recthover,ellipsehover,polyhover,filterhover]
toolsOn = [pencilon,eraseron,brushon,sprayon,highon,lineon,recton,ellipseon,polyon,filteron]
stickers = [normal,roe,salmon2,salmon,grass,egg,sashimi]
items = [save,op,undo,redo] #undo,save...


screen.blit(background,(0,0)) #background
 

#Basic Rects
canvasRect = Rect(565,205,825,545) #Rectangle for canvas
colourpickerRect = Rect(15,715,colourpicker.get_width(),colourpicker.get_height()) #rectangle for colour picker


####blit items
screen.blit(colourpicker,(15,715)) #blits colourpicker
xItems = [] #used a list to store the x-coordinates of the items so I don't have to write them out manually
for i in range(4): #loop that runs 4 times
    screen.blit(items[i],(16+i*70,20)) #blits items at i (save,open,undo,redo)
    a = 10+i*70
    xItems.append(a)#adds it to the list

###blit music buttons
for i in range(len(musicButtons)):          #this blits all the music buttons in that list
    screen.blit(buttons[i],(795+i*80,770))

switch=False                #switch is a variable so that the user can control when the music changes


#Items Rects
saveRect = Rect(xItems[0],10,49,49) #xItems are the x-coordinates of where the music images were blit
openRect = Rect(xItems[1],10,49,49)
undoRect = Rect(xItems[2],10,49,49)
redoRect = Rect(xItems[3],10,49,49)
    
##drawing rects
draw.rect(screen, WHITE, canvasRect)    #drawing the canvasRect
screen.blit(plate,(535,-55))            #blits the plate that the sushi stamps are on
screen.blit(coordinate,(1330,755))  #blits the frame that holds the coordinates

#blit stickers
for j in range(7): 
    screen.blit(stickers[j],(557+j*120,7))

#music button Rects
voldownRect = Rect(790,765,55,55) #volume down
backwardsRect = Rect(870,765,55,55) #rect for the previous song
pauseRect = Rect(950,765,55,55)
playRect = Rect(1030,765,55,55)
forwardsRect = Rect(1110,765,55,55)
volupRect = Rect(1190,765,55,55)


#stickerRects
normalRect = Rect(557,7,100,100)
roeRect = Rect(677,7,100,100)
salmon2Rect = Rect(797,7,100,100)
salmonRect = Rect(917,7,100,100)
grassRect = Rect(1037,7,100,100)
eggRect = Rect(1157,7,100,100)
sashimiRect = Rect(1277,7,100,100)

#### Tool Rects
pencilRect = Rect(10,110,90,130)
eraserRect = Rect(117,110,90,130)
brushRect = Rect(224,110,90,130)
spraypaintRect = Rect(331,110,90,130)
highlighterRect = Rect(438,110,90,130)

lineRect = Rect(10,260,90,130)
rectRect = Rect(117,260,90,130)
ellipseRect = Rect(224,260,90,130)
polygonRect = Rect(331,260,90,130)
filterRect = Rect(438,260,90,130)



#lists with all of the Rects
toolRects = [pencilRect,eraserRect,brushRect,spraypaintRect,highlighterRect,lineRect,rectRect,ellipseRect,polygonRect,filterRect]
stickerRects = [normalRect,roeRect,salmon2Rect,salmonRect,grassRect,eggRect,sashimiRect]
itemRects = [saveRect,openRect, undoRect, redoRect]
musicRects = [voldownRect,backwardsRect,pauseRect,playRect,forwardsRect,volupRect]


screenCap = screen.subsurface(canvasRect).copy()            #a picture of the blank canvas for the undolist
undolist = [screenCap]          #undolist with screen cap of blank canvas
redolist = []       #list where all the undo screen captures go when you press undo


#Text
screen.blit(textFrame, (20,400))             #blitting the text frame that holds the instructions
start = "Click on a tool to start!"         #intro words on the text frame
startPic = font.render(start,True,BLACK)            #rendering the last variable into a picture
screen.blit(startPic,(35,415))          #bliting it

#toolsText tells you the name of the selected tool
toolsText = ["Tool: Pencil","Tool: Eraser", "Tool: Brush", "Tool: Spray Paint", "Tool: Highlighter","Tool: Line","Tool: Rectangle","Tool: Ellipse","Tool: Polygon","Tool: Filter"]
#stickerText tells you the name of the selected sticker 
stickerText = ["Sticker: The Californian Roll","Sticker: Roe(Fish Eggs) Roll","Sticker: Salmon Roll","Sticker: Salmon Sushi","Sticker: Seaweed Sushi", "Sticker: Egg Sushi", "Sticker: Sashimi"]
#list of instructions tell you the instructions for each tool
instructions = ["Press the RIGHT arrow to increase the size", "Press the LEFT arrow to decrease the size","Press the UP arrow to fill","Press the DOWN arrow to unfill",
                "Press the UP arrow to increase opacity","Press the DOWN arrow to decrease opacity","To draw a polygon: CLICK on multiple points","Press the SPACEBAR to finish","CLICK on other shapes for further instructions",
                "Sepia Filter","Grayscale Filter","Press the UP arrow for the SEPIA filter","Press the DOWN arrow for the GRAYSCALE filter","To RE-FILTER: PRESS the filter tool again",
                "***Filtering an image may take a few seconds***"]
#music text shows you current music button selected
musicText = ["Volume Down","Previous Song","Pause","Play","Next Song","Volume Up"]

#lists for texts that are rendered into images
toolsTextPics = []
stickerTextPics = []

musicTextPics = []
musicTextPics2 = []
instrucPics = []

#these next few loops are for rendering text to pictures
for i in range(len(toolsText)):             #looping the length of the list
    toolsTextPic = font.render(toolsText[i],True,BLACK)             #rendering the string at i with anti-aliasing and a black colour
    toolsTextPics.append(toolsTextPic)          #adding it to the list
    ###next few loops are similar to the previous one
for i in range(len(stickerText)):
    stickerTextPic = font.render(stickerText[i],True,BLACK)
    stickerTextPics.append(stickerTextPic)

for i in range(len(musicText)):
    musicTextPic = font.render(musicText[i],True,BLACK)
    musicTextPics.append(musicTextPic)
for i in range(len(instructions)):
    instrucPic = font.render(instructions[i],True,BLACK)
    instrucPics.append(instrucPic)
    

    
omx,omy,mx,my=0,0,0,0       #defining the old mouse positions and the current mouse positions before the loop

r,g,b,a = 0,0,0,0           #red,green,blue, and alpha #alpha is for transparency

rad = 1             #pencil and polygon tool needs to be limited because there are gaps if the size is too big 
rad2 = 1            #for brush, eraser, rectangle and ellipse
sprayRad = 5            #size for the spray
highlighterRad = 5          #size for the highlighter
transparency = 5            #opacity - the higher the more opaque
fill = 1            #variable for if the shape is filled or unfilled; also used to change the filter example images because there are two filters


pos = 0         #position for position of song
volume = 1.0        #volume for song
pause = False       #variable to see if music is paused

running=True        #see if the loop is running

tool = "no tool"        #a variable to see if there is a tool selected
button = "no button"        #button is a variable for music that is used for the text display shown later

vXY = []                    #a list to hold the vertices for the polygon tool

selectStickers = [0 for i in range(len(stickers))]          #used for selecting stickers #used list comprehension to draw a whole bunch of zeros
selectTools = [0 for i in range(len(toolsOff))]             #used for selecting tools


while running:
    click = False       #click is a variable to check if something is clicked
    mx,my=mouse.get_pos()       #gets positions of mx,my
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type == MOUSEBUTTONDOWN:         #if mouse clicks down
            sx,sy = evt.pos         #gets position when pressed down
            if tool == "polygon": 
                if (sx,sy) not in vXY and canvasRect.collidepoint(sx,sy):       #if the position is not already in the list and it is inside the canvas
                    vXY.append((sx,sy))                                         #adds it to the list
                    draw.rect(screen,col,(vXY[-1][0],vXY[-1][1],1.9,1.9))       #drawing a small rectangle at each spot you click for the polygon


                    

                
                


        if evt.type == MOUSEBUTTONUP: #when mouse button goes up
            screenCap = screen.subsurface(canvasRect).copy() #takes a screen cap of the canvas
            click = True #click = True when mouse button is up
            if canvasRect.collidepoint(mx,my) and tool!="polygon": #if the mouse is on the canvas rect 
                undolist.append(screenCap) #undo list adds the screen cap
                screen.blit(screenCap,canvasRect) #blit the screen cap
                screen.set_clip(canvasRect) #clips so that everything is done inside the canvas

        


              
        
    
            
        if evt.type == KEYDOWN: #if a key is pressed down
            ###changing the size of the tools
            if evt.key == K_LEFT:           #if it is the left arrow
                if rad>1:           # if the pencil/line/polygon radius is greater than one
                    rad -= 1            #subtract 1
                if rad2>1:          #if the rad2 is greater than 1 
                    rad2 -= 1           #subtract 1
                if sprayRad>5:          #if the spray radius is over 5
                    sprayRad -=1            #subtract 1
                if highlighterRad>5:            #if the highlighter radius is over 5
                    highlighterRad-=1           #subtract 1 from the highlighter
            #changing the size part 2
            if evt.key == K_RIGHT: #if the right arrow is pressed #mostly similar to the when the left arrow is pressed but add instead of subtract
                if rad<9:           #if rad is less than ten
                    rad+=1 
                if rad2<70:
                    rad2+=1
                if sprayRad<10:
                    sprayRad+=1
                if highlighterRad<40:
                    highlighterRad+=1
            if evt.key == K_UP:                 #if up arrow is pressed
                if tool == "highlighter":       #if tool is highlighter
                    if transparency<=255:       #if it is not over 255
                        transparency+=2         #add 2
            
                fill = 0 #the fill variable is set to filled mode
            if evt.key == K_DOWN: #if down arrow is pressed
                if tool == "highlighter": #if tool is highlighter
                    if transparency>5: 
                        transparency-=2

                fill = 1#variable set to unfill mode
            if evt.key == K_SPACE: #if the space button is pressed
                if tool == "polygon": 
                    screen.set_clip(canvasRect) #clips so that you can only draw in canvas
                    if fill == 1: 
                        draw.polygon(screen,col,(vXY),rad) #drawing unfilled polygon
                    if fill == 0:
                        draw.polygon(screen,col,(vXY))      #drawing filled polygon
                    screenCap = screen.subsurface(canvasRect).copy()   #takes a screencap
                    undolist.append(screenCap) #adds it to undolist
                    
                    screen.blit(screenCap,canvasRect)  #blits the screenCap
                    vXY = []  #sets the list empty
                    screen.set_clip(None) #unclips canvas so things outside work
                        
                

                
                
                
                       
    mx,my=mouse.get_pos() #current mouse position
    mb=mouse.get_pressed() #shows which mouse is pressed

    #this loop displays text for the music
    for m in range(len(musicRects)):
        if musicRects[m].collidepoint(mx,my):       #if the mouse touches the musicRect then the text will be displayed
            button = musicText[m]
            songText = "Music: "+button 
            sText = font.render(songText,True,BLACK) #renders text
            screen.blit(textFrame,(20,400))         #blits text frame so that words do not overwrite each other
            screen.blit(sText,(35,650))
   
        ###coordinate system
    coord = str(mx-565)+", "+str(my-205)        #this is the coordinate text
    coordPic = font.render(coord,True,BLACK)    #rendering above variable into image
    if canvasRect.collidepoint(mx,my):          #if mouse is on canvas
        screen.blit(coordinate,(1330,755))      #blits the coordinate plane so that the text doesn't overwrite on itself
        screen.blit(coordPic,(1345,770))        #blits the current position of mouse on canvas
    else:
        screen.blit(coordinate,(1330,755))      #if mouse if not on canvas, nothing will show


    
                       
    #Drawing Items Rects
    for i in range(len(itemRects)):   #this loop draws save, open, undo, and redo rects
        draw.rect(screen, LIGHTBLUE, itemRects[i],5)
    #Hovering Item Rects
        if itemRects[i].collidepoint(mx,my): #when you hover over the save, open...etc the rectangle will change to red
            draw.rect(screen, PINK, itemRects[i],5)

     #Drawing Sticker Rects
    for i in range(len(stickerRects)):          #The next four lines (not including comment) are similar to the one above
        draw.rect(screen,LIGHTBLUE,stickerRects[i],2)
    #Hovering Sticker Rects
        if stickerRects[i].collidepoint(mx,my):
            draw.rect(screen, PINK, stickerRects[i],2)
            if mb[0] == 1:
                selectStickers = [0 for i in range(len(stickers))] #this list of 0s is to indicate if one is selected; also resets everything to 0 when something else is selected
                selectStickers[i] = 1                             #selectStickers in position i is selected
                
                
        if selectStickers[i] == 1 and toolSelect == False:          #toolSelect is to check if a tool is selected (for displaying text)
            draw.rect(screen, DARKYELLOW, stickerRects[i],2)        #making a sticker rect yellow that coincides with the selectStickers[i]
            screen.blit(textFrame,(20,400))                         #blits text frame
            screen.blit(stickerTextPics[i],(35,415))                #blits sticker text info

            for m in range(len(musicRects)):                        #same loop as previous one that blitted music text
                if musicRects[m].collidepoint(mx,my):
                    button = musicText[m]
                    songText = "Music: "+button
                    sText = font.render(songText,True,BLACK)
                    screen.blit(sText,(35,650))
        

    #Drawing Music Button Rects
    for i in range(len(musicRects)):   #same idea as drawing item rects 
        draw.rect(screen,LIGHTBLUE,musicRects[i],5)
        
        if musicRects[i].collidepoint(mx,my):
            draw.rect(screen, PINK, musicRects[i],5)
  
    #drawing all tool Rects
    for x in range(10):      #draws all the tools when not used or hovered over
        screen.blit(toolsOff[x],toolRects[x])
    for x in range(10):
        draw.rect(screen,WHITE,toolRects[x],1)#draws tool rects
        
        if toolRects[x].collidepoint(mx,my):
            screen.blit(toolsHover[x],toolRects[x])#hover state #similar to how the items and stickers work except with images
            
            if mb[0] == 1:
                selectTools = [0 for j in range(len(toolsOff))]
                
                selectTools[x] = 1
        if selectTools[x] == 1 and stickerSelect == False: #stickerSelect is showing if stickers are selected or not; making stickerSelect false means tools are selected
            screen.blit(toolsOn[x],toolRects[x])
    

            screen.blit(textFrame,(20,400)) #blits text frame
            screen.blit(toolsTextPics[x],(35,415)) #blits current tool used text
            for m in range(len(musicRects)): #same music text blitting
                if musicRects[m].collidepoint(mx,my):
                    button = musicText[m]
                    songText = "Music: "+button
                    sText = font.render(songText,True,BLACK)
                    screen.blit(sText,(35,650))


            #This section is for tools instructions
            #if statements have to be used since different tools have different instructions
            if x<4:
                screen.blit(instrucPics[0],(35,440)) 
                screen.blit(instrucPics[1],(35,470))
                size = highlighterRad
                if x == 0:                      #if tool is pencil
                    size = "Size: "+str(rad)    #size is the variable that displays the size of the tool (rad,rad2,sprayRad...)
                if x == 1 or x == 2:            #if tool is eraser or brush
                    size = "Size: " +str(rad2)
                if x == 3:
                    size = "Size: " +str(sprayRad)  #if tool is spray
                sizePic = font.render(size,True,BLACK) #rendering above variable into a picture
                screen.blit(sizePic,(35,500)) #blits the text

            if x == 4:                              #if tool is highlighter
                screen.blit(instrucPics[0],(35,440))#blitting instructions (next few lines)
                screen.blit(instrucPics[1],(35,470))
                screen.blit(instrucPics[4],(35,500))
                screen.blit(instrucPics[5],(35,530))
                size = "Size: "+str(highlighterRad) 
                sizePic = font.render(size,True,BLACK)
                screen.blit(sizePic,(35,560))
                opacity = "Opacity: "+str(transparency) #shows the opacity of the highlighter
                opacityPic = font.render(opacity,True,BLACK)
                screen.blit(opacityPic,(35,590))

                
            if x>4 and x!=8 and x!=9: #if tool is circle,rect,and ellipse
                for i in range(4): #blits the next few instructions
                    screen.blit(instrucPics[i],(35,440+i*30))

                size =  "Size: "+str(rad2) #same as for pencil/brushes above
                sizePic = font.render(size,True,BLACK)
                screen.blit(sizePic,(35,560))
                if fill == 1:       # text for if fill is off
                    filled = "Off"
                if fill == 0:       #text for if fill is on
                    filled = "On"
                    
                fillText = "Fill: "+filled 
                fillPic = font.render(fillText,True,BLACK) #displaying if shape is filled or unfilled
                screen.blit(fillPic,(35,590))
                
            if x == 8: #similar to one above (polygon)
                screen.blit(instrucPics[6],(35,440))
                screen.blit(instrucPics[7],(35,470))
                screen.blit(instrucPics[8],(35,500))

                size =  "Size: "+str(rad2)
                sizePic = font.render(size,True,BLACK)
                screen.blit(sizePic,(35,560))
                if fill == 1:
                    filled = "Off"
                if fill == 0:
                    filled = "On"
                    
                fillText = "Fill: "+filled
                fillPic = font.render(fillText,True,BLACK)
                screen.blit(fillPic,(35,590))

            if x == 9: #(filters)
                if fill == 1:
                    screen.blit(instrucPics[10],(35,440)) #grayscale
                if fill == 0:
                    screen.blit(instrucPics[9],(35,440)) #sepia
                for i in range(4): #this loop blits the next few consecutive instructions
                    screen.blit(instrucPics[i+11],(35,470+i*30))


        
            
                
        screen.blit(myfils[fill].subsurface((0,0,70,50)),(448,295)) #blits the grayscale and sepia example on a smaller sub surface
    
    

    draw.rect(screen,col,(480,760,100,60))               #colour display
    brushHead = Surface((50,50),SRCALPHA)                   #surface for highlighter
    draw.circle(brushHead,(r,g,b,transparency),(10,10),highlighterRad) #transparent highlighter


    

    

    if click:                   #clicked on 
        if playRect.collidepoint(mx,my) and pause == False: #if playRect is clicked and music is not paused
            
            switch=True                                     #variable so that music switches to next song
            mixer.music.set_volume(volume)              #sets volume #default is 1.0
            mixer.music.load(songNames[pos])
            mixer.music.play()                          #plays music
        if playRect.collidepoint(mx,my) and pause == True: #if music is paused and play is clicked again then song will unpause
            mixer.music.unpause()

        if pauseRect.collidepoint(mx,my): #pausing music
            pause = True 
            mixer.music.pause()
            


            
    playing = mixer.music.get_busy() #checks to see if a song is playing

    if playing == 0 and switch: #if there is no song playing go to next song
        pos = (pos+1)%len(songNames) #pos increases (taking the modulus makes sure that pos does not go out of range)
        
        mixer.music.load(songNames[pos]) #loads next song
        mixer.music.play()              #plays it
        playing = mixer.music.get_busy()    #checks to see if song is playing
            


    
    
    



        
    #Selecting the stickers
    if mb[0] == 1: #left click

        for st in stickerRects: #this loop sets stickers as currently selected (for text)
            if st.collidepoint(mx,my):
                stickerSelect=True
                toolSelect  = False
            
        if normalRect.collidepoint(mx,my):          #if mouse is on the normal sushi 
            tool = "normal"                         #tool is the normal sushi
            screenCap = screen.subsurface(canvasRect).copy() #takes a screencap of the canvas (next few lines are the similar)
        if roeRect.collidepoint(mx,my):
            tool = "roe"
            screenCap = screen.subsurface(canvasRect).copy()
        if salmon2Rect.collidepoint(mx,my):
            tool = "salmon2"
            screenCap = screen.subsurface(canvasRect).copy()
        if salmonRect.collidepoint(mx,my):
            tool = "salmon"
            screenCap = screen.subsurface(canvasRect).copy()
        if grassRect.collidepoint(mx,my):
            tool = "grass"
            screenCap = screen.subsurface(canvasRect).copy()
        if eggRect.collidepoint(mx,my):
            tool = "egg"
            screenCap = screen.subsurface(canvasRect).copy()
        if sashimiRect.collidepoint(mx,my):
            tool = "sashimi"
            screenCap = screen.subsurface(canvasRect).copy()
            
    #selecting the tools
        for to in toolRects: #same as the stickerSelect loop but opposite
            if to.collidepoint(mx,my):
                toolSelect = True
                stickerSelect = False
        if pencilRect.collidepoint(mx,my): #tells which tool is selected
            tool = "pencil"
        if eraserRect.collidepoint(mx,my):
            tool = "eraser"
        if brushRect.collidepoint(mx,my):
            tool = "brush"
        if spraypaintRect.collidepoint(mx,my):
            tool = "spraypaint"
        if lineRect.collidepoint(mx,my):
            tool = "line"
        if rectRect.collidepoint(mx,my):
            tool = "rect"
        if ellipseRect.collidepoint(mx,my):
            tool = "ellipse"
        if highlighterRect.collidepoint(mx,my):
            tool = "highlighter"
        if polygonRect.collidepoint(mx,my):
            tool = "polygon"
        if filterRect.collidepoint(mx,my):
            if fill == 0: #sepia filter
                for x in range(565,1391):       #this nested loops checks every pixel
                    for y in range(205,750):
                        r,g,b,a = screen.get_at((x,y))      #gets the r,g,b,a at that specific pixel
                        nr = min(255,0.393*r + 0.769*g + 0.189*b)   #formula for sepia filter
                        ng = min(255,0.349*r + 0.686*g + 0.168*b)   #nr,ng,nb is new red,green, and blue colour (takes the minimum)
                        nb = min(255,0.272*r + 0.534*g + 0.131*b)
                        screen.set_at((x,y),(nr,ng,nb)) #sets the pixel at x,y to the new colours
            if fill == 1: #grayscale filter
                for x in range(565,1391): #same concept as sepia filter
                    for y in range(205,750):
                        r,g,b,a = screen.get_at((x,y))
                        nr = min(255,0.30*r + 0.59*g + 0.11*b)
                        ng = min(255,0.30*r + 0.59*g + 0.11*b)
                        nb = min(255,0.30*r + 0.59*g + 0.11*b)
                        screen.set_at((x,y),(nr,ng,nb))
            screenCap = screen.subsurface(canvasRect).copy() #takes a screencap and adds it to the undolist
            undolist.append(screenCap)

    
    
    if click: #mouse is clicked
        if saveRect.collidepoint(mx,my): #save
            try:
                filename = filedialog.asksaveasfilename(defaultextension = ".png") #image automatically saved as png 
                image.save(screen.subsurface(canvasRect).copy(),filename)           #saves screenshot of canvas
            except:                         #when you close the window without saving anything program will not crash
                print("Save Error")

        if openRect.collidepoint(mx,my): #open
            try:
                filename = filedialog.askopenfilename()   #gets filename of image you want to open
                mypic = image.load(filename)              #my pic is your loaded image
                screen.subsurface(canvasRect).fill((255,255,255))   #clears canvas for new image
                screen.set_clip(canvasRect)                         #clips canvas so that image cannot go over boundaries
                screen.blit(mypic,canvasRect)                       #blits your image
                screen.set_clip(None)                               #unclip canvas so you can use other things
                screenCap = screen.subsurface(canvasRect).copy()    #takes a screencap 
                undolist.append(screenCap)                          #adds it to undolist
            except:    #when you close window without opening anything
                print("Load Error")
    if click == True:
        if undoRect.collidepoint(mx,my):
            if len(undolist)>1:       #makes sure that you do not undo the blank canvas
                last = undolist.pop()  #removes last screenshot
                if last != screenCap:  #if the last one is not the screenshot
                    redolist.append(last) #redolist adds the screenshot
                    screen.blit(undolist[-1],canvasRect) #blits the last screenshot
    
        if redoRect.collidepoint(mx,my):
            if len(redolist)>=1: #makes sure you don't remove from an empty list
                first = redolist.pop(-1)  #gets the first from the redo list
                undolist.append(first)    #adds it to the undo list
                screen.blit(undolist[-1],canvasRect)  #blits the screenshot
#

    #Using Music Buttons
        if backwardsRect.collidepoint(mx,my): #previous song
            pos = (pos-1)%len(songNames) #subtracts one from the current position (modulus makes it so that the number does not go out of range)
            mixer.music.load(songNames[pos]) #loads it 
            mixer.music.play() #plays it
        
        if forwardsRect.collidepoint(mx,my):
            pos = (pos+1)%len(songNames) #same as backwards but adding
            mixer.music.load(songNames[pos])
            mixer.music.play()
        if volupRect.collidepoint(mx,my): #volume up
            if volume<=1.0:               #if the current volume is less than the maximum
                volume+=0.01              #increases the volume by 0.01
                mixer.music.set_volume(volume) #sets volume
        if voldownRect.collidepoint(mx,my):   #same as volume up except subtract
            if volume>0:
                volume-=0.01
                mixer.music.set_volume(volume)

    ###   using the stickers
    if canvasRect.collidepoint(mx,my): #if mouse in canvasRect
        screen.set_clip(canvasRect)    #clips canvas


        if mb[0] == 1:
            if tool == "normal":   #if normal sticker is selected
                screen.blit(screenCap,canvasRect) #blits screenCap so it doesn't draw as you move
                screen.blit(normal,(mx-50,my-50)) #blits the sticker (next few are similar)
            if tool == "roe":
                screen.blit(screenCap,canvasRect)
                screen.blit(roe,(mx-50,my-50))
            if tool == "salmon2":
                screen.blit(screenCap,canvasRect)
                screen.blit(salmon2,(mx-50,my-50))
            if tool == "salmon":
                screen.blit(screenCap,canvasRect)
                screen.blit(salmon,(mx-50,my-50))
            if tool == "grass":
                screen.blit(screenCap,canvasRect)
                screen.blit(grass,(mx-50,my-50))
            if tool == "egg":
                screen.blit(screenCap,canvasRect)
                screen.blit(egg,(mx-50,my-50))
            if tool == "sashimi":
                screen.blit(screenCap,canvasRect)
                screen.blit(sashimi,(mx-50,my-50))

        
            ###USING THE TOOLS
            if tool == "pencil":
                draw.line(screen,col,(omx,omy),(mx,my),rad) #drawing a line from old mx,my to current one
                
            if tool == "eraser":
                dx = mx - omx #distance from current mouse position to previous one
                dy = my - omy
                dist = sqrt(dx**2 + dy**2) #distance of hypotenuse
                if dist == 0:               #if mouse does not move and gets pressed
                    draw.circle(screen, WHITE, (mx,my),rad2) #draw a circle that is white
                    
                for i in range(1,int(dist)): #this loop makes sure that circles do not leave gaps while drawing fast
                    cx = int(omx + i*dx/dist)
                    cy = int(omy + i*dy/dist)
                    draw.circle(screen, WHITE, (cx,cy),rad2) #draws eraser
                    
            if tool == "brush": #same as eraser but with colour
                dx = mx - omx
                dy = my - omy
                dist = sqrt(dx**2 + dy**2) 
                if dist == 0:
                    draw.circle(screen, col, (mx,my),rad2)
                    
                for i in range(1,int(dist)):
                    cx = int(omx + i*dx/dist)
                    cy = int(omy + i*dy/dist)
                    draw.circle(screen, col, (cx,cy),rad2)
    
                


##  MAKE THIS FOR HIGHLIGHTER
            if tool == "highlighter": 
                dx = mx - omx #distance from current mouse position to previous mouse position
                dy = my - omy
                dist = sqrt(dx**2 + dy**2) #distance of hypotenuse of dx,dy
                for i in range(0,int(dist)): #loop is so that the circles do not leave gaps in between while drawing fast
                    cx = int(omx + i*dx/dist)
                    cy = int(omy + i*dy/dist)
                    screen.blit(brushHead,(cx-10,cy-10)) #blits brushHead

                if screen.get_at((mx,my)) == (255,255,255,255): #so that you do not continuously blit brushHead 
                    for i in range(5):                      #if you press once draw 5 because transparency is really light
                        screen.blit(brushHead, (mx-10,my-10)) 
                        
            if tool == "spraypaint": 
                if screen.get_at((mx,my)) == (255,255,255,255): #so that the spray does does not continuously draw until its pitch black
                    rx = randint(mx-sprayRad*2,mx+sprayRad*2) #random x-value from mx-sprayRad to mx+sprayRad
                    ry = randint(my-sprayRad*2,my+sprayRad*2) #random y-value
                    r = randint(3,6)                            #random size
                    if (mx-rx)**2 + (my-ry)**2<20**2:
                        draw.circle(screen,col,(rx,ry),r)

            if tool == "line":
                screen.blit(screenCap,canvasRect) #blits screencap
                draw.line(screen,col,(sx,sy),(mx,my),rad2)   #draws line from sx,sy to mx,my
                
            if tool == "rect":       
                screen.blit(screenCap,canvasRect)   #blits screencap
                w = mx - sx             #width
                h = my - sy             #height
                for i in range(rad2):       #draws the rectangle radius amount of times
                    if w>0 and h>0 or w<0 and h<0:                              #if width and height are both negative or positive
                        draw.rect(screen, col, (sx+i,sy+i,w-i*2,h-i*2),fill)       #draws 5 rects 1 pixel up down and right time 
                    if w<0 and h>0:                                                 #if width is negative but height is positive
                        draw.rect(screen, col, (sx-i,sy+i,w+i*2,h-i*2),fill)
                    if w>0 and h<0:                                             #if width is positive and height is negative
                        draw.rect(screen, col, (sx+i,sy-i,w-i*2,h+i*2),fill)
                        
                    
            if tool ==  "ellipse":
                try: 
                    screen.blit(screenCap,canvasRect) #blit screenCap so it doesn't draw every single move you make
                    w = mx - sx       #width
                    h = my - sy       #height
                    ellRect = Rect(sx,sy,w,h) #Rects for ellipse
                    ellRect1 = Rect(sx+1,sy,w,h) #draws five so no gaps are left when thickness changes
                    ellRect2 = Rect(sx-1,sy,w,h)
                    ellRect3 = Rect(sx,sy+1,w,h)
                    ellRect4 = Rect(sx,sy-1,w,h)
                    ellRect.normalize() #normalizes negative values
                    ellRect1.normalize()
                    ellRect2.normalize()
                    ellRect3.normalize()
                    ellRect4.normalize()
                    if fill == 1:      #if ellipse is unfilled 
                        draw.ellipse(screen,col,ellRect,rad2) #draws ellipse
                        draw.ellipse(screen,col,ellRect1,rad2)
                        draw.ellipse(screen,col,ellRect2,rad2)
                        draw.ellipse(screen,col,ellRect3,rad2)
                        draw.ellipse(screen,col,ellRect4,rad2)
                    else: #if ellipse is filled
                        draw.ellipse(screen,col,ellRect) #draws ellipse
                        draw.ellipse(screen,col,ellRect1)
                        draw.ellipse(screen,col,ellRect2)
                        draw.ellipse(screen,col,ellRect3)
                        draw.ellipse(screen,col,ellRect4)
                except:
                    print("Error")

                




                    
                

        screen.set_clip(None)
            
                
    #selecting colours
    if mb[0]==1:
            
        if colourpickerRect.collidepoint(mx,my):
            
            col = screen.get_at((mx,my)) #gets colour at mx,my in colour picker rect
            r = col[0] #col is the colour variable
            g = col[1]
            b = col[2]


            
            
    
    
   
    display.flip() #displays everything
    omx,omy=mx,my #old mx,my = mx,my 
            
quit()
