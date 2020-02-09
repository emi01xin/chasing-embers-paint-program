#paint project
from pygame import *
import os
from random import *
from math import *
from tkinter import *                
from tkinter.colorchooser import *

init()
root=Tk()         
root.withdraw()
inf=display.Info()
os.environ['SDL_VIDEO_WINDOW_PO5S']='-30,30'

screen=display.set_mode((1345,935))
display.set_caption('Chasing Embers')

cover=Surface((1345,935)).convert() #for transparency tool

#loading screen
startPic1=image.load("Images/startPic1.jpg")
screen.blit(startPic1,(0,0))
display.flip()
time.wait(600)

startPic2=image.load("Images/startPic2.jpg")
screen.blit(startPic2,(0,0))
display.flip()
time.wait(600)

startPic3=image.load("Images/startPic3.jpg")
screen.blit(startPic3,(0,0))
display.flip()
time.wait(600)

startPic1=image.load("Images/startPic1.jpg")
screen.blit(startPic1,(0,0))
display.flip()
time.wait(600)

startPic2=image.load("Images/startPic2.jpg")
screen.blit(startPic2,(0,0))
display.flip()
time.wait(600)

startPic3=image.load("Images/startPic3.jpg")
screen.blit(startPic3,(0,0))
display.flip()
time.wait(600)

startPic1=image.load("Images/startPic1.jpg")
screen.blit(startPic1,(0,0))
display.flip()
time.wait(600)

startPic2=image.load("Images/startPic2.jpg")
screen.blit(startPic2,(0,0))
display.flip()
time.wait(600)

startPic3=image.load("Images/startPic3.jpg")
screen.blit(startPic3,(0,0))
display.flip()
time.wait(600)

#images
bgPic=image.load("Images/bgPic.png")
screen.blit(bgPic,(0,0))

canvasRect=Rect(190,30,940,570)
draw.rect(screen,(255,255,255),canvasRect)

colorp=image.load("Images/colorp1.gif")
resizedcolorp=transform.scale(colorp,(730,160))
screen.blit(resizedcolorp,(420,610))

accPic1=image.load("Images/tumblr_o8e6hzr8Wi1t8bmhqo1_1280_edit.gif")
screen.blit(accPic1,(1135,30))

accPic2=image.load("Images/tumblr_obwy7lKBLB1t8bmhqo1_1280_edit.gif")
screen.blit(accPic2,(1090,250))

accPic3=image.load("Images/tumblr_oeyh6yRgnK1t8bmhqo1_1280_edit.gif")
screen.blit(accPic3,(1175,150))

accPic4=image.load("Images/tumblr_oey2vgtjaP1t8bmhqo1_1280_edit.gif")
screen.blit(accPic4,(1130,780))

backgroundsPic=image.load("Images/backgrounds.png")
screen.blit(backgroundsPic,(18,678))

bg1Pic=image.load("Images/bg1.png")

bg2Pic=image.load("Images/bg2.png")

bg3Pic=image.load("Images/bg3.png")

bg1Picp=image.load("Images/bg1p.png")
screen.blit(bg1Picp,(18,738))

bg2Picp=image.load("Images/bg2p.png")
screen.blit(bg2Picp,(18,798))

bg3Picp=image.load("Images/bg3p.png")
screen.blit(bg3Picp,(18,858))

#audio
mixer.music.load("audio/Young Forever Inst..mp3")
mixer.music.play()
            
clickSound=mixer.Sound("audio/clicksound.wav")
    
#colors
white=(255,255,255)
black=(0,0,0)
themecolor1=(217,187,111)
themecolor2=(196,189,194)
themecolor3=(207,193,170)
themecolor4=(208,204,207)
drawcolor=(160, 134, 135)
drawcolorAsString="(160, 134, 135)"
trans=5

#default
tool="pencil" #starting tool
tool2="musicon" #starts with music playing
infoline1="Scroll up or down to increase"
infoline2="decrease size."
mx,my=0,0
undo=[(screen.subsurface(canvasRect)).copy()] #undo list
redo=[] #redo list
linewid=2 #width of unfilled rect and line
brushwid=10 #width of paintbrush, transbrush and eraser
pencwid=2 #width of pencil
sprayrad=30 #radius of spraypaint
trans=255 #transparency
stampsize=150 #size of stamp
angle=0 #angle of stamp rotation
sz1=30
sz2=27
sz3=19

#flags
oncanvas=False #when mouse is not on canvas

#font
#Font1=font.Font("font/Expressive Inks.ttf",sz1)
#Font2=font.Font("font/Expressive Inks.ttf",sz2)
#Font3=font.Font("font/Expressive Inks.ttf",sz3)

Font1=font.SysFont("FF DIN",sz1)
Font2=font.SysFont("FF DIN",sz2)
Font3=font.SysFont("FF DIN",sz3)

#tool rects
stampsRect=Rect(190,775,941,133)
draw.rect(screen,(white),stampsRect)

colorpRect=Rect(420,610,730,160) #color palette

undoRect=Rect(18,510,40,40)
redoRect=Rect(68,510,40,40)
saveRect=Rect(118,510,40,40)
openRect=Rect(18,560,40,40)
newRect=Rect(68,560,40,40)
colorchooserRect=Rect(118,560,40,40)
musiconRect=Rect(18,610,40,40)
musicoffRect=Rect(68,610,40,40)

bg1Rect=Rect(18,738,150,50)
bg2Rect=Rect(18,798,150,50)
bg3Rect=Rect(18,858,150,50)

pencilRect=Rect(18,30,60,60)
paintbrushRect=Rect(98,30,60,60)
transbrushRect=Rect(18,110,60,60)
eraserRect=Rect(98,110,60,60)
spraypaintRect=Rect(18,190,60,60)
eyedropperRect=Rect(98,190,60,60)
fillRect=Rect(18,270,60,60)

rectRect=Rect(98,270,60,60)
frectRect=Rect(18,350,60,60)
ellipseRect=Rect(98,350,60,60)
fellipseRect=Rect(18,430,60,60)
lineRect=Rect(98,430,60,60)

#stamp rects
stamp1sRect=Rect(210,780,120,120)
stamp2sRect=Rect(340,780,120,120)
stamp3sRect=Rect(475,780,120,120)
stamp4sRect=Rect(600,780,120,120)
stamp5sRect=Rect(740,780,120,120)
stamp6sRect=Rect(860,780,120,120)
stamp7sRect=Rect(990,780,120,120)

#selected tool icons
undoIcon2=image.load("icons/icon-undo2.gif")

redoIcon2=image.load("icons/icon-redo2.gif")

saveIcon2=image.load("icons/icon-save2.gif")

openIcon2=image.load("icons/icon-open2.gif")

newIcon2=image.load("icons/icon-new2.gif")

colorchooserIcon2=image.load("icons/icon-color2.gif")

musiconIcon2=image.load("icons/icon-musicon2.gif")

musicoffIcon2=image.load("icons/icon-musicoff2.gif")

#-------

pencilIcon2=image.load("icons/icon-pencil2.gif")

paintbrushIcon2=image.load("icons/icon-paintbrush2.gif")

transbrushIcon2=image.load("icons/icon-trans2.gif")

eraserIcon2=image.load("icons/icon-eraser2.gif")

spraypaintIcon2=image.load("icons/icon-spraypaint2.gif")

eyedropperIcon2=image.load("icons/icon-eyedropper2.gif")

fillIcon2=image.load("icons/icon-fill2.gif")

rectIcon2=image.load("icons/icon-rect2.gif")

frectIcon2=image.load("icons/icon-frect2.gif")

ellipseIcon2=image.load("icons/icon-ellipse2.gif")

fellipseIcon2=image.load("icons/icon-fellipse2.gif")

lineIcon2=image.load("icons/icon-line2.gif")

#tool icons
undoIcon=image.load("icons/icon-undo.gif")
screen.blit(undoIcon,(18,510))

redoIcon=image.load("icons/icon-redo.gif")
screen.blit(redoIcon,(68,510))

saveIcon=image.load("icons/icon-save.gif")
screen.blit(saveIcon,(118,510))

openIcon=image.load("icons/icon-open.gif")
screen.blit(openIcon,(18,560))

newIcon=image.load("icons/icon-new.gif")
screen.blit(newIcon,(68,560))

colorchooserIcon=image.load("icons/icon-color.gif")
screen.blit(colorchooserIcon,(118,560))

musiconIcon=image.load("icons/icon-musicon.gif")
screen.blit(musiconIcon,(18,610))

musicoffIcon=image.load("icons/icon-musicoff.gif")
screen.blit(musicoffIcon,(68,610))

#-------

pencilIcon=image.load("icons/icon-pencil.gif")
screen.blit(pencilIcon,(18,30))

paintbrushIcon=image.load("icons/icon-paintbrush.gif")
screen.blit(paintbrushIcon,(98,30))

transbrushIcon=image.load("icons/icon-trans.gif")
screen.blit(transbrushIcon,(18,110))

eraserIcon=image.load("icons/icon-eraser.gif")
screen.blit(eraserIcon,(98,110))

spraypaintIcon=image.load("icons/icon-spraypaint.gif")
screen.blit(spraypaintIcon,(18,190))

eyedropperIcon=image.load("icons/icon-eyedropper.gif")
screen.blit(eyedropperIcon,(98,190))

fillIcon=image.load("icons/icon-fill.gif")
screen.blit(fillIcon,(18,270))

rectIcon=image.load("icons/icon-rect.gif")
screen.blit(rectIcon,(98,270))

frectIcon=image.load("icons/icon-frect.gif")
screen.blit(frectIcon,(18,350))

ellipseIcon=image.load("icons/icon-ellipse.gif")
screen.blit(ellipseIcon,(98,350))

fellipseIcon=image.load("icons/icon-fellipse.gif")
screen.blit(fellipseIcon,(18,430))

lineIcon=image.load("icons/icon-line.gif")
screen.blit(lineIcon,(98,430))

#selected stamps
stamp1s=image.load("stamps/stamp1s.gif")
resizedstamp1sRect=transform.scale(stamp1s,(120,120))
screen.blit(resizedstamp1sRect,(210,780))

stamp2s=image.load("stamps/stamp2s.gif")
resizedstamp2sRect=transform.scale(stamp2s,(120,120))
screen.blit(resizedstamp2sRect,(340,780))

stamp3s=image.load("stamps/stamp3s.gif")
resizedstamp3sRect=transform.scale(stamp3s,(120,120))
screen.blit(resizedstamp3sRect,(475,780))

stamp4s=image.load("stamps/stamp4s.gif")
resizedstamp4sRect=transform.scale(stamp4s,(120,120))
screen.blit(resizedstamp4sRect,(600,780))

stamp5s=image.load("stamps/stamp5s.gif")
resizedstamp5sRect=transform.scale(stamp5s,(120,120))
screen.blit(resizedstamp5sRect,(740,780))

stamp6s=image.load("stamps/stamp6s.gif")
resizedstamp6sRect=transform.scale(stamp6s,(120,120))
screen.blit(resizedstamp6sRect,(860,780))

stamp7s=image.load("stamps/stamp7s.gif")
resizedstamp7sRect=transform.scale(stamp7s,(120,120))
screen.blit(resizedstamp7sRect,(990,780))

#stamps   
stamp1=image.load("stamps/stamp1.png")
stamp1Rect=Rect(210,780,120,120)
resizedstamp1Rect=transform.scale(stamp1,(120,120))
screen.blit(resizedstamp1Rect,(210,780))

stamp2=image.load("stamps/stamp2.png")
stamp2Rect=Rect(340,780,120,120)
resizedstamp2Rect=transform.scale(stamp2,(120,120))
screen.blit(resizedstamp2Rect,(340,780))

stamp3=image.load("stamps/stamp3.png")
stamp3Rect=Rect(475,780,120,120)
resizedstamp3Rect=transform.scale(stamp3,(120,120))
screen.blit(resizedstamp3Rect,(475,780))

stamp4=image.load("stamps/stamp4.png")
stamp4Rect=Rect(600,780,120,120)
resizedstamp4Rect=transform.scale(stamp4,(120,120))
screen.blit(resizedstamp4Rect,(600,780))

stamp5=image.load("stamps/stamp5.png")
stamp5Rect=Rect(740,780,120,120)
resizedstamp5Rect=transform.scale(stamp5,(120,120))
screen.blit(resizedstamp5Rect,(740,780))

stamp6=image.load("stamps/stamp6.png")
stamp6Rect=Rect(860,780,120,120)
resizedstamp6Rect=transform.scale(stamp6,(120,120))
screen.blit(resizedstamp6Rect,(860,780))

stamp7=image.load("stamps/stamp7.png")
stamp7Rect=Rect(990,780,120,120)
resizedstamp7Rect=transform.scale(stamp7,(120,120))
screen.blit(resizedstamp7Rect,(990,780))

#-----------

running=True
while running:
    
    for e in event.get():
        if e.type==QUIT:
            running=False
            
        if e.type==MOUSEBUTTONDOWN:
            cover.fill((255,0,255))
            if canvasRect.collidepoint(mx,my):
                redo=[] #resets redo list

            if e.button==1: #left click
                if undoRect.collidepoint(mx,my):
                    if len(undo)>1: #if there's at least 2 elements
                        screen.blit(undo[-2],(190,30))  #blit the second last element
                        redo.append(undo.pop()) #add last element of redo to undo list   

                if redoRect.collidepoint(mx,my):
                    if len(redo)>=1: #if there's one or no element
                        screen.blit(redo[-1],(190,30)) #blit the last element
                        undo.append(redo.pop()) #add last element of undo to redo list        
                        
                copy=screen.copy() #captures screen
                sx,sy=e.pos #gets position when user presses mouse button
            
        if e.type==MOUSEBUTTONUP:
            angle=0 #resets angle when a new stamp is selected
            
            if canvasRect.collidepoint(mx,my) and e.button!=4 and e.button!=5: #doesn't add scrolling to increase/decrease size to list
                undo.append(screen.subsurface(canvasRect).copy()) #adds screen capture to undo list when drawing on canvas
                    
            if e.button==4: #scroll up to increase size
                if tool=="pencil":
                    pencwid+=1
                    pencwid=min(pencwid,5)
                    
                if tool=="paintbrush" or tool=="eraser":
                    brushwid+=1
                    brushwid=min(brushwid,50)
                    
                if tool=="transbrush":
                    trans+=10
                    trans=min(trans,255)
                                        
                if tool=="spray paint":
                    sprayrad+=5
                    sprayrad=min(sprayrad,100)
                                        
                if tool=="unfilled rect" or tool=="line":
                    linewid+=2
                    linewid=min(linewid,40)

                if tool=="stamp 1" or tool=="stamp 2" or tool=="stamp 3" or tool=="stamp 4" or tool=="stamp 5" or tool=="stamp 6" or tool=="stamp 7":
                    stampsize+=5
                    stampsize=min(stampsize,300)
                    
            if e.button==5: #scroll down to increase size
                if tool=="pencil":
                    pencwid-=1
                    pencwid=max(1,pencwid)
                    
                if tool=="paintbrush" or tool=="eraser":
                    brushwid-=1
                    brushwid=max(6,brushwid)

                if tool=="transbrush":
                    trans-=10
                    trans=max(15,trans)
                    
                if tool=="spray paint":
                    sprayrad-=5
                    sprayrad=max(30,sprayrad)

                if tool=="unfilled rect" or tool=="line":
                    linewid-=2
                    linewid=max(1,linewid)
                    
                if tool=="stamp 1" or tool=="stamp 2" or tool=="stamp 3" or tool=="stamp 4" or tool=="stamp 5" or tool=="stamp 6" or tool=="stamp 7":
                    stampsize-=5
                    stampsize=max(stampsize,100)

    mb=mouse.get_pressed() 
    omx,omy=mx,my #gets the previous position and stores as old position
    mx,my=mouse.get_pos() #gets new mouse position    
    keys=key.get_pressed()
      
    if keys[K_RIGHT]: #press right key on keyboard to rotate clockwise
        angle-=2
    elif keys[K_LEFT]: #press left key on keyboard to rotate counter-clockwise
        angle+=2

#-----------
        
    #selected tools
    if tool2=="undo": #if tool is undo, blit selected image
        screen.blit(undoIcon2,(18,510))
        tool2=" "
    else: #if tool is not undo, blit icon image
        screen.blit(undoIcon,(18,510))
        
    if tool2=="redo":
        screen.blit(redoIcon2,(68,510))
        tool2=" "
    else:
        screen.blit(redoIcon,(68,510))

    if tool2=="save":
        screen.blit(saveIcon2,(118,510))
        tool2=" "
    else:
        screen.blit(saveIcon,(118,510))

    if tool2=="open":
        screen.blit(openIcon2,(18,560))
        tool2=" "
    else:
        screen.blit(openIcon,(18,560))

    if tool2=="new":
        screen.blit(newIcon2,(68,560))
        tool2=" "
    else:
        screen.blit(newIcon,(68,560))
        
    if tool2=="colorchooser":
        screen.blit(colorchooserIcon2,(118,560))
        tool2=" "
    else:
        screen.blit(colorchooserIcon,(118,560))

    if tool2=="musicon":
        screen.blit(musiconIcon2,(18,610))
        screen.blit(musicoffIcon,(68,610))

    elif tool2=="musicoff":
        screen.blit(musiconIcon,(18,610))
        screen.blit(musicoffIcon2,(68,610))

    #-------
        
    if tool=="pencil":
        screen.blit(pencilIcon2,(18,30))

    else:
        screen.blit(pencilIcon,(18,30))

    if tool=="paintbrush":
        screen.blit(paintbrushIcon2,(98,30))

    else:
        screen.blit(paintbrushIcon,(98,30))

    if tool=="transbrush":
        screen.blit(transbrushIcon2,(18,110))

    else:
        screen.blit(transbrushIcon,(18,110))
        
    if tool=="eraser":
        screen.blit(eraserIcon2,(98,110))

    else:
        screen.blit(eraserIcon,(98,110))

    if tool=="spray paint":
        screen.blit(spraypaintIcon2,(18,190))

    else:
        screen.blit(spraypaintIcon,(18,190))

    if tool=="eyedropper":
        screen.blit(eyedropperIcon2,(98,190))

    else:
        screen.blit(eyedropperIcon,(98,190))

    if tool=="fill":
        screen.blit(fillIcon2,(18,270))

    else:
        screen.blit(fillIcon,(18,270))

    if tool=="unfilled rect":
        screen.blit(rectIcon2,(98,270))

    else:
        screen.blit(rectIcon,(98,270))

    if tool=="filled rect":
        screen.blit(frectIcon2,(18,350))

    else:
        screen.blit(frectIcon,(18,350))

    if tool=="unfilled ellipse":
        screen.blit(ellipseIcon2,(98,350))

    else:
        screen.blit(ellipseIcon,(98,350))

    if tool=="filled ellipse":
        screen.blit(fellipseIcon2,(18,430))

    else:
        screen.blit(fellipseIcon,(18,430))

    if tool=="line":
        screen.blit(lineIcon2,(98,430))

    else:
        screen.blit(lineIcon,(98,430))

    #selected stamps
    if tool=="stamp 1":
        screen.blit(resizedstamp1sRect,(210,780))

    else:
        screen.blit(resizedstamp1Rect,(210,780))        
        
    if tool=="stamp 2":
        screen.blit(resizedstamp2sRect,(340,780))

    else:
        screen.blit(resizedstamp2Rect,(340,780))

    if tool=="stamp 3":
        screen.blit(resizedstamp3sRect,(475,780))

    else:
        screen.blit(resizedstamp3Rect,(475,780))

    if tool=="stamp 4":
        screen.blit(resizedstamp4sRect,(600,780))

    else:
        screen.blit(resizedstamp4Rect,(600,780))

    if tool=="stamp 5":
        screen.blit(resizedstamp5sRect,(740,780))

    else:
        screen.blit(resizedstamp5Rect,(740,780))

    if tool=="stamp 6":
        screen.blit(resizedstamp6sRect,(860,780))

    else:
        screen.blit(resizedstamp6Rect,(860,780))

    if tool=="stamp 7":
        screen.blit(resizedstamp7sRect,(990,780))

    else:
        screen.blit(resizedstamp7Rect,(990,780))

        
    #tool select
    if undoRect.collidepoint(mx,my):
        screen.blit(undoIcon2,(18,510)) #if mouse is hovering over icon blit selected image
        if mb[0]==1:
            clickSound.play()
            tool2="undo"
        
    if redoRect.collidepoint(mx,my):
        screen.blit(redoIcon2,(68,510))
        if mb[0]==1:
            clickSound.play()
            tool2="redo"

    if saveRect.collidepoint(mx,my):
        screen.blit(saveIcon2,(118,510))
        if mb[0]==1:
            clickSound.play()
            tool2="save"

    if openRect.collidepoint(mx,my):
        screen.blit(openIcon2,(18,560))
        if mb[0]==1:
            clickSound.play()
            tool2="open"

    if newRect.collidepoint(mx,my):
        screen.blit(newIcon2,(68,560))
        if mb[0]==1:
            clickSound.play()
            tool2="new"

    if colorchooserRect.collidepoint(mx,my):
        screen.blit(colorchooserIcon2,(118,560))
        if mb[0]==1:
            clickSound.play()
            tool2="colorchooser"

    if musiconRect.collidepoint(mx,my):
        screen.blit(musiconIcon2,(18,610))
        if mb[0]==1:
            clickSound.play()
            tool2="musicon"

    if musicoffRect.collidepoint(mx,my):
        screen.blit(musicoffIcon2,(68,610))
        if mb[0]==1:
            clickSound.play()
            tool2="musicoff"

    #-------
        
    if pencilRect.collidepoint(mx,my):
        screen.blit(pencilIcon2,(18,30))
        if mb[0]==1:
            clickSound.play()
            tool="pencil"
            tool2=" "
            infoline1="Scroll up or down to increase"
            infoline2="decrease size"

    if paintbrushRect.collidepoint(mx,my):
        screen.blit(paintbrushIcon2,(98,30))
        if mb[0]==1:
            clickSound.play()
            tool="paintbrush"
            tool2=" "
            infoline1="Scroll up or down to increase"
            infoline2="decrease size"

    if transbrushRect.collidepoint(mx,my):
        screen.blit(transbrushIcon2,(18,110))
        if mb[0]==1:
            clickSound.play()
            tool="transbrush"
            tool2=" "
            infoline1="Scroll up or down to increase"
            infoline2="decrease transparency"
        
    if eraserRect.collidepoint(mx,my):
        screen.blit(eraserIcon2,(98,110))
        if mb[0]==1:
            clickSound.play()
            tool="eraser"
            tool2=" "
            infoline1="Scroll up or down to increase"
            infoline2="decrease size"
        
    if spraypaintRect.collidepoint(mx,my):
        screen.blit(spraypaintIcon2,(18,190))
        if mb[0]==1:
            clickSound.play()
            tool="spray paint"
            tool2=" "
            infoline1="Scroll up or down to increase"
            infoline2="decrease size"
        
    if eyedropperRect.collidepoint(mx,my):
        screen.blit(eyedropperIcon2,(98,190))
        if mb[0]==1:
            clickSound.play()
            tool="eyedropper"
            tool2=" "
            infoline1="Click area on canvas to"
            infoline2="identify color"

    if fillRect.collidepoint(mx,my):
        screen.blit(fillIcon2,(18,270))
        if mb[0]==1:
            clickSound.play()
            tool="fill"
            tool2=" "
            infoline1="Click area on canvas to fill"
            infoline2="with color"

    if rectRect.collidepoint(mx,my):
        screen.blit(rectIcon2,(98,270))
        if mb[0]==1:
            clickSound.play()
            tool="unfilled rect"
            tool2=" "
            infoline1="Scroll up or down to increase"
            infoline2="decrease size"

    if frectRect.collidepoint(mx,my):
        screen.blit(frectIcon2,(18,350))
        if mb[0]==1:
            clickSound.play()
            tool="filled rect"
            tool2=" "
            infoline1="Click and drag to draw"
            infoline2="a filled rectangle"

    if ellipseRect.collidepoint(mx,my):
        screen.blit(ellipseIcon2,(98,350))
        if mb[0]==1:
            clickSound.play()
            tool="unfilled ellipse"
            tool2=" "
            infoline1="Click and drag to draw"
            infoline2="an unfilled ellipse"

    if fellipseRect.collidepoint(mx,my):
        screen.blit(fellipseIcon2,(18,430))
        if mb[0]==1:
            clickSound.play()
            tool="filled ellipse"
            tool2=" "
            infoline1="Click and drag to draw"
            infoline2="a filled ellipse"

    if lineRect.collidepoint(mx,my):
        screen.blit(lineIcon2,(98,430))
        if mb[0]==1:
            clickSound.play()
            tool="line"
            tool2=" "
            infoline1="Scroll up or down to increase"
            infoline2="decrease size"
        
    #additional tools
    if mb[0]==1:
        if colorpRect.collidepoint(mx,my):
            drawcolor=screen.get_at((mx,my)) #gets color at place where mouse clicks
            drawcolorAsString=screen.get_at((mx,my)) #gets color as a string at place where mouse clicks
            print(drawcolor,drawcolorAsString)

        if saveRect.collidepoint(mx,my):
            result=filedialog.asksaveasfilename()
            image.save(screen.subsurface(canvasRect),result)
            print(result)

        if openRect.collidepoint(mx,my):
            result=filedialog.askopenfilename()
            image=image.load(result)
            screen.blit(image,(200,30))
            screen.set_clip(None)
            
        if newRect.collidepoint(mx,my):
            draw.rect(screen,(255,255,255),canvasRect)

        if colorchooserRect.collidepoint(mx,my):
            drawcolor,drawcolorAsString=askcolor(title='pick a color') #gets color selected as string
            print(drawcolor,drawcolorAsString)
            tool="pencil" #sets tool to pencil

        if musiconRect.collidepoint(mx,my):
            mixer.music.unpause()

        if musicoffRect.collidepoint(mx,my):
            mixer.music.pause()

        if bg1Rect.collidepoint(mx,my):
            screen.blit(bg1Pic,(190,30)) #sets as canvas background

        if bg2Rect.collidepoint(mx,my):
            screen.blit(bg2Pic,(190,30))

        if bg3Rect.collidepoint(mx,my):
            screen.blit(bg3Pic,(190,30))
            
            
    #draw on canvas
    if canvasRect.collidepoint(mx,my) and mb[0]==1:
        screen.set_clip(canvasRect) #cannot paint outside of canvas
        
        if tool=="pencil":
            draw.line(screen,(drawcolor),(omx,omy),(mx,my),pencwid)
            
        if tool=="paintbrush":
            dx=mx-omx
            dy=my-omy
            dist=int(sqrt(dx**2+dy**2))
            for i in range(1,dist+1):
                gapX=int(omx+i*dx/dist)
                gapY=int(omy+i*dy/dist)
                draw.circle(screen,(drawcolor),(gapX,gapY),brushwid)  #draws on every point between old and new mouse position
            time.wait(20)

        if tool=="transbrush":
            cover.set_alpha(trans) #sets alpha value for brush surface
            cover.set_colorkey((255,0,255))
            dx=mx-omx
            dy=my-omy
            dist=int(sqrt(dx**2+dy**2))
            for i in range(1,dist+1):
                gapX=int(omx+i*dx/dist)
                gapY=int(omy+i*dy/dist)
                draw.circle(cover,(drawcolor),(gapX,gapY),brushwid)
            screen.blit(copy,(0,0))
            screen.blit(cover,(0,0))

        if tool=="eraser":
            if mb[0]==1:
                dx=mx-omx
                dy=my-omy
                dist=int(sqrt(dx**2+dy**2))
            for i in range(1,dist+1):
                gapX=int(omx+i*dx/dist)
                gapY=int(omy+i*dy/dist)
                draw.circle(screen,(white),(gapX,gapY),brushwid)

        if tool=="spray paint":
            for i in range(int(8*2)):
                px=randint(-sprayrad,sprayrad) #random position in list
                py=randint(-sprayrad,sprayrad)
                if px**2+py**2<sprayrad**2: #hypotenuse #to make oval
                    screen.set_at((mx+px,my+py),drawcolor) #sets position of pixels

        if tool=="eyedropper":
            drawcolor=screen.get_at((mx,my))
            tool="pencil" #sets tool to pencil

        if tool=="fill":
            mx,my=mouse.get_pos()
            rc=screen.get_at((mx,my)) #gets the color of spot clicked 
            spots=[(mx,my)] 
            while len(spots)>0: #when the spots list has at least one element 
                newSpots=[] #list of new spots
                for fx,fy in spots: #spot clicked
                    if 190<fx<1140and 30<fy<600 and screen.get_at((fx,fy))==rc:  #if fx and fy are within the range of the canvas
                        screen.set_at((fx,fy),drawcolor) #and the color of the pixel of fx,fy is the same color as the one selected before, begin to fill the area 
                                     #right    #left    #down       #up
                        newSpots+=[(fx+1,fy),(fx-1,fy),(fx,fy+1),(fx,fy-1)]  #points to fill from the initial point
                    spots=newSpots #each time from the newSpots, they become spots and the right, left, up and down of these points are counted as newSpots and then the pixels are colored in
            
        if tool=="unfilled rect":
            screen.blit(copy,(0,0))
            draw.line(screen,drawcolor,(sx,sy),(sx,my),linewid)
            draw.line(screen,drawcolor,(sx,my),(mx,my),linewid)
            draw.line(screen,drawcolor,(mx,my),(mx,sy),linewid)
            draw.line(screen,drawcolor,(mx,sy),(sx,sy),linewid)

        if tool=="filled rect":
            screen.blit(copy,(0,0))
            draw.rect(screen,drawcolor,(sx,sy,(mx-sx),(my-sy)))

        if tool=="unfilled ellipse":
            screen.blit(copy,(0,0))
            rec=Rect(sx,sy,mx-sx,my-sy)
            rec.normalize() #makes negative value positive 
            if abs(mx-sx)>3 and abs(my-sy)>3: #width cannot be greater than radius
                draw.ellipse(screen,drawcolor,(rec),2)
            else:
                draw.ellipse(screen,drawcolor,(rec))
        
        if tool=="filled ellipse":
            screen.blit(copy,(0,0))
            rec=Rect(sx,sy,mx-sx,my-sy)
            rec.normalize() 
            draw.ellipse(screen,drawcolor,(rec))
            
        if tool=="line":
            screen.blit(copy,(0,0))
            draw.line(screen,drawcolor,(sx,sy),(mx,my),linewid)
            
    screen.set_clip(None)
    
    #stamps
    if mb[0]==1:
        screen.set_clip(canvasRect) #cannot paint outside of canvas
        if stamp1Rect.collidepoint(mx,my):
            clickSound.play()
            tool="stamp 1"
            infoline1="Use left and right keys while"
            infoline2="holding sticker to rotate."

        if stamp2Rect.collidepoint(mx,my):
            clickSound.play()
            tool="stamp 2"
            infoline1="Use left and right keys while"
            infoline2="holding sticker to rotate."
                
        if stamp3Rect.collidepoint(mx,my):
            clickSound.play()
            tool="stamp 3"
            infoline1="Use left and right keys while"
            infoline2="holding sticker to rotate."

        if stamp4Rect.collidepoint(mx,my):
            clickSound.play()
            tool="stamp 4"
            infoline1="Use left and right keys while"
            infoline2="holding sticker to rotate."

        if stamp5Rect.collidepoint(mx,my):
            clickSound.play()
            tool="stamp 5"
            infoline1="Use left and right keys while"
            infoline2="holding sticker to rotate."

        if stamp6Rect.collidepoint(mx,my):
            clickSound.play()
            tool="stamp 6"
            infoline1="Use left and right keys while"
            infoline2="holding sticker to rotate."

        if stamp7Rect.collidepoint(mx,my):
            clickSound.play()
            tool="stamp 7"
            infoline1="Use left and right keys while"
            infoline2="holding sticker to rotate."

    screen.set_clip(None)

    #stamps
    if mb[0]==1:
        if tool=="stamp 1":
            screen.set_clip(canvasRect)
            resizedstamp1=transform.scale(stamp1,(stampsize,stampsize))
            screen.blit(resizedstamp1,(mx-100,my-100))

            screen.blit(copy,(0,0))
            rotatedstamp1=transform.rotate(resizedstamp1,angle) #rotates stamp
            screen.blit(rotatedstamp1,(mx-rotatedstamp1.get_width()//2,my-rotatedstamp1.get_height()//2))
            display.flip()
            time.wait(10)
            
        if tool=="stamp 2":
            screen.set_clip(canvasRect)
            resizedstamp2=transform.scale(stamp2,(stampsize,stampsize))
            screen.blit(resizedstamp2,(mx-100,my-100))
            
            screen.blit(copy,(0,0))
            rotatedstamp2=transform.rotate(resizedstamp2,angle)
            screen.blit(rotatedstamp2,(mx-rotatedstamp2.get_width()//2,my-rotatedstamp2.get_height()//2))
            display.flip()
            time.wait(10)

        if tool=="stamp 3":
            screen.set_clip(canvasRect)
            resizedstamp3=transform.scale(stamp3,(stampsize,stampsize))
            screen.blit(resizedstamp3,(mx-100,my-100))

            screen.blit(copy,(0,0))
            rotatedstamp3=transform.rotate(resizedstamp3,angle)
            screen.blit(rotatedstamp3,(mx-rotatedstamp3.get_width()//2,my-rotatedstamp3.get_height()//2))
            display.flip()
            time.wait(10)

        if tool=="stamp 4":
            screen.set_clip(canvasRect)
            resizedstamp4=transform.scale(stamp4,(stampsize,stampsize))
            screen.blit(resizedstamp4,(mx-100,my-100))

            screen.blit(copy,(0,0))
            rotatedstamp4=transform.rotate(resizedstamp4,angle)
            screen.blit(rotatedstamp4,(mx-rotatedstamp4.get_width()//2,my-rotatedstamp4.get_height()//2))
            display.flip()
            time.wait(10)
            
        if tool=="stamp 5":
            screen.set_clip(canvasRect)
            resizedstamp5=transform.scale(stamp5,(stampsize,stampsize))
            screen.blit(resizedstamp5,(mx-100,my-100))

            screen.blit(copy,(0,0))
            rotatedstamp5=transform.rotate(resizedstamp5,angle)
            screen.blit(rotatedstamp5,(mx-rotatedstamp5.get_width()//2,my-rotatedstamp5.get_height()//2))
            display.flip()
            time.wait(10)

        if tool=="stamp 6":
            screen.set_clip(canvasRect)
            resizedstamp6=transform.scale(stamp6,(stampsize,stampsize))
            screen.blit(resizedstamp6,(mx-100,my-100))

            screen.blit(copy,(0,0))
            rotatedstamp6=transform.rotate(resizedstamp6,angle)
            screen.blit(rotatedstamp6,(mx-rotatedstamp6.get_width()//2,my-rotatedstamp6.get_height()//2))
            display.flip()
            time.wait(10)

        if tool=="stamp 7":
            screen.set_clip(canvasRect)
            resizedstamp7=transform.scale(stamp7,(stampsize,stampsize))
            screen.blit(resizedstamp7,(mx-100,my-100))

            screen.blit(copy,(0,0))
            rotatedstamp7=transform.rotate(resizedstamp7,angle)
            screen.blit(rotatedstamp7,(mx-rotatedstamp7.get_width()//2,my-rotatedstamp7.get_height()//2))
            display.flip()
            time.wait(10)

    screen.set_clip(None)
            
    #previewbox
    previewbRect=Rect(190,620,224,140)
    colorRect=Rect(200,630,203,30)
    draw.rect(screen,themecolor3,previewbRect)
    draw.rect(screen,drawcolor,colorRect) #displays color selected
    
    position="x:             y:"
    colorcode=str(drawcolorAsString) #converts color code to string
    
    if canvasRect.collidepoint(mx,my): #converts mouse position to string
        mxp=str(mx) 
        myp=str(my)
    else: #if off canvas
        mxp="off" 
        myp="canvas"

    #color preview
    txtPic=Font1.render(colorcode,True,white)
    screen.blit(txtPic,(210,635))

    #position
    txtPic=Font2.render(position,True,white)
    screen.blit(txtPic,(200,665))

    txtPic=Font2.render(mxp,True,white)
    screen.blit(txtPic,(225,665))

    txtPic=Font2.render(myp,True,white)
    screen.blit(txtPic,(314,665))

    #tool preview
    txtPic=Font1.render("tool:",True,white)
    screen.blit(txtPic,(200,688))
    
    txtPic=Font2.render(tool,True,white)
    screen.blit(txtPic,(250,689))

    txtPic=Font3.render(infoline1,True,white)
    screen.blit(txtPic,(200,714))

    txtPic=Font3.render(infoline2,True,white)
    screen.blit(txtPic,(200,734))

    display.flip()
font.quit()
del Font1
del Font2
del Font3
quit()
