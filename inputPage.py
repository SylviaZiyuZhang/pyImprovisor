
from tkinter import *
# def draw(canvas, width, height):
#     canvas.create_rectangle(0,0,150,150, fill="yellow")

# def runDrawing(width=300, height=300):
#     root = Tk()
#     root.resizable(width=False, height=False) # prevents resizing window
#     canvas = Canvas(root, width=width, height=height)
#     canvas.configure(bd=0, highlightthickness=0)
#     canvas.pack()
#     draw(canvas, width, height)
#     root.mainloop()
#     print("bye!")



# runDrawing(800, 1200)




####################################
# Variables
####################################

allChords = ["Am7", NONE, NONE, NONE, NONE, NONE, NONE, NONE,
			"Cm7", NONE, NONE, NONE, NONE, NONE, NONE, "F7",
			"BbM7", NONE, "Bbm7", "Eb7", "AbM7", NONE, "Abm7", "Db7",]

inputs = []


def compileInputs(allChords):
	thisChord = ""
	count = 0
	for chord in allChords:
		if chord != NONE:
			count = count + 1
			if thisChord != "": 
				inputs.append((thisChord, 0.5*count))
			thisChord = chord
			count = 0
		else:
			count = count + 1
	return True

compileInputs(allChords)

print(inputs)

####################################
# Color Scheme
####################################

color1 = "#011935"
color2 = "#00343F"
color3 = "#1DB0B8"
color4 = "#37C6C0"
color5 = "#D0E9FF"


#####################################
# Button Class
#####################################
class Buttons(object):
	allButton=[]
	keyEx=None #Indicate whether there is already a key button on. If there is, the button take the place.
	ShFlEx=None #Indicate whether there is already a sharp/flat button on
	ProEx=None
	Mod=[]
	def __init__(self,size,shape,location,text,ButtonType="Key",on=False,color="red",aff=None):
		Buttons.allButton.append(self)
		self.on=on          # indicate if it's on
		self.size=size      #size of it. 
		self.shape=shape    #1 is a ball and 0 is a square
		self.loc=location   #a tuple in the form (x,y)
		self.text=text      #the text being displayed on it.
		self.color=color
		self.valid=True
		self.ButtonType=ButtonType
		self.mods=[]		#Show what affiliations a tone has
		self.aff=aff		#Affiliation to a tone, only extension options have this

	def drawButton(self,canvas,data): #draw a button
		if self.on:
			color=self.color
		else: color = "white"
		if self.shape==1:
			canvas.create_oval(self.loc[0]-self.size,
				self.loc[1]-self.size,self.loc[0]+self.size,self.loc[1]+self.size,fill=color)
		elif self.shape==0:
			canvas.create_rectangle(self.loc[0]-self.size,
				self.loc[1]-self.size,self.loc[0]+self.size,self.loc[1]+self.size,fill=color)
		canvas.create_text(self.loc[0],self.loc[1],text=self.text)
	
	def detectButton(self,x,y,data): #Detect whether the button is pressed, if pressed do something:
		if abs(self.loc[0]-x)<self.size and abs(self.loc[1]-y)<self.size:
			if self.ButtonType=="Key":
				if Buttons.keyEx!=self:
					if Buttons.keyEx!=None:  		#The case of changing a key button
						Buttons.keyEx.on=False
						Buttons.keyEx=self       #If the button is a key and is not the current key, it's 
						self.on=True              #then switched to this button.
						if Buttons.ShFlEx!=None:    #If previously chose a shfl button, abort the change
							Buttons.ShFlEx.on=False
							Buttons.ShFlEx=None
					else:
						Buttons.keyEx=self
						self.on=True
				else:
					if Buttons.ShFlEx!=None:
							Buttons.ShFlEx.on=False
							Buttons.ShFlEx=None
					self.on=False
					Buttons.keyEx=None
			elif self.ButtonType=="ShFl":
				if Buttons.ShFlEx!=self:
					if Buttons.ShFlEx!=None:
						Buttons.ShFlEx.on=False
						Buttons.ShFlEx=self       #If the button is a flat/sharp and is not the current key, it's 
						self.on=True              #then switched to this button.
					else:
						Buttons.ShFlEx=self
						self.on=True
				else:
					self.on=False
					Buttons.ShFlEx=None
			elif self.ButtonType=="Proceed":
				if Buttons.ProEx!=self:
					if Buttons.ProEx!=None:
						Buttons.ProEx.on=False
						Buttons.ProEx=self       #If the button is a proceed button and is not the current key, it's 
						self.on=True              #then switched to this button.
					else:
						Buttons.ProEx=self
						self.on=True
						RUN_FLAG = False
						print ("run flag is false!")
				else:
					self.on=False
					Buttons.ProEx=None
			elif self.ButtonType==

#####################################
# Grid functions
#####################################

def getIndex(row, col):
	return 8*row + col


def init(data):
	data.rows = 3
	data.cols = 8
	data.margin = 5 # margin around grid
	data.selection = (-1, -1) # (row, col) of selection, (-1,-1) for none
	
	AKeyButton=Buttons(30,0,(900,50+0*70),"A") #Key Buttons
	BKeyButton=Buttons(30,0,(900,50+1*70),"B")
	CKeyButton=Buttons(30,0,(900,50+2*70),"C")
	DKeyButton=Buttons(30,0,(900,50+3*70),"D")
	EKeyButton=Buttons(30,0,(900,50+4*70),"E")
	FKeyButton=Buttons(30,0,(900,50+5*70),"F")
	GKeyButton=Buttons(30,0,(900,50+6*70),"G")

	FlatButtonKey=Buttons(20,1,(900,500+1*50),"b",ButtonType="ShFl")
	SharpButtonKey=Buttons(20,1,(900,500+2*50),"#",ButtonType="ShFl")
	SharpButton5=Buttons(20,1,(1000,50+0*70),"#",ButtonType="Tone")
	FlatButton5=Buttons(20,1,(1100,50+0*70),"b",ButtonType="Tone")
	FlatButton9=Buttons(20,1,(1100,50+2*70),"b",ButtonType="Tone")
	SharpButton9=Buttons(20,1,(1000,50+2*70),"#",ButtonType="Tone")
	SharpButton11=Buttons(20,1,(1000,50+3*70),"#",ButtonType="Tone")
	FlatButton13=Buttons(20,1,(1100,50+4*70),"b",ButtonType="Tone")


	Button5=Buttons(25,1,(1050,50+0*70),"5",ButtonType="Tone")
	Button7=Buttons(25,1,(1050,50+1*70),"7",ButtonType="Tone")
	Button9=Buttons(25,1,(1050,50+2*70),"9",ButtonType="Tone")
	Button11=Buttons(25,1,(1050,50+3*70),"11",ButtonType="Tone")
	Button13=Buttons(25,1,(1050,50+4*70),"13",ButtonType="Tone")
	ButtonM=Buttons(25,1,(1050,50+5*70),"M",ButtonType="Quality")
	Buttonm=Buttons(25,1,(1050,50+6*70),"m",ButtonType="Quality")

def pointInGrid(x, y, data):
	# return True if (x, y) is inside the grid defined by data.
	return ((data.margin <= x <= (data.width*2)/3-data.margin) and
			(data.margin <= y <= data.height/2-data.margin))

def getCell(x, y, data):
	# aka "viewToModel"
	# return (row, col) in which (x, y) occurred or (-1, -1) if outside grid.
	if (not pointInGrid(x, y, data)):
		return (-1, -1)
	gridWidth  = 2*data.width/3 - 2*data.margin
	gridHeight = data.height/2 - 2*data.margin
	cellWidth  = gridWidth / (data.cols)
	cellHeight = gridHeight / (data.rows)
	row = ((y - 50) - data.margin) // cellHeight 
	col = (x - data.margin) // cellWidth
	# triple-check that we are in bounds
	row = min(data.rows-1, max(0, row))
	col = min(data.cols-1, max(0, col))
	return (row, col)

def getCellBounds(row, col, data):
	# aka "modelToView"
	# returns (x0, y0, x1, y1) corners/bounding box of given cell in grid
	gridWidth  = 2*data.width/3 - 2*data.margin
	gridHeight = data.height/2 - 2*data.margin
	columnWidth = gridWidth / data.cols
	rowHeight = gridHeight / data.rows
	x0 = data.margin + col * columnWidth
	x1 = data.margin + (col+1) * columnWidth
	y0 = data.margin + row * rowHeight 
	y1 = data.margin + (row+1) * rowHeight 
	return (x0, y0, x1, y1)

def mousePressed(event, data):
	for button in Buttons.allButton: #Check buttons status
		button.detectButton(event.x,event.y)
	if (not pointInGrid(event.x, event.y, data)):
		return
	(row, col) = getCell(event.x, event.y, data)
	# select this (row, col) unless it is selected
	if (data.selection == (row, col)):
		data.selection = (-1, -1)
	else:
		data.selection = (row, col)

def keyPressed(event, data):
	pass

def redrawAll(canvas, data):

	# draw grid of cells
	for row in range(data.rows):
		for col in range(data.cols):
			(x0, y0, x1, y1) = getCellBounds(row, col, data)
			fill = color5 if (data.selection == (row, col)) else "white"
			canvas.create_rectangle(x0, y0 + 50, x1, y1 + 50, fill=fill, outline=color3, dash=(1,5))

	# The first extra bar line as start
	canvas.create_line(15, 65, 15, 175, fill=color2, width=2)

	# draw barlines
	for row in range(data.rows):
		for col in range(data.cols//2 + 1):
			(x0, y0, x1, y1) = getCellBounds(row, col, data)
			canvas.create_line(x0*2, y0+10 + 50, x0*2, y1-10 + 50, fill=color2, width=2)

	# show symbols
	for row in range(data.rows):
		for col in range(data.cols):
			(x0, y0, x1, y1) = getCellBounds(row, col, data)
			text = allChords[getIndex(row, col)]
			if text != NONE:
				bass = text[0]
				optionalFlat = True if (text[1]=="b") else False
				quality = text[2:] if optionalFlat == True else text[1:]

				# display the bass
				canvas.create_text((x0 + x1)/2 , (y0 + y1)/2 + 50, text=bass+("b" if optionalFlat==True else ""), 
					font=("Comic Sans MS", "30"), fill=color2)
				# display the quality
				canvas.create_text((x0 + x1)/2 + 20, (y0 + y1)/2 - 10 + 50, text=quality, 
					font=("Comic Sans MS", "15"), fill=color2)



	canvas.create_text(360, 25, text="New song 0",
					   font=("Comic Sans MS", "30"), fill=color2)
	for button in Buttons.allButton:
		button.drawButton(canvas,data)


####################################
# use the run function as-is
####################################

def runInputPage(width=400, height=600):

	global RUN_FLAG
	RUN_FLAG = True

	def redrawAllWrapper(canvas, data):
		canvas.delete(ALL)
		canvas.create_rectangle(0, 0, data.width, data.height,
								fill='white', width=0)
		redrawAll(canvas, data)
		canvas.update()    

	def mousePressedWrapper(event, canvas, data):
		mousePressed(event, data)
		redrawAllWrapper(canvas, data)

	def keyPressedWrapper(event, canvas, data):
		keyPressed(event, data)
		redrawAllWrapper(canvas, data)

	# Set up data and call init
	class Struct(object): pass
	data = Struct()
	data.width = width
	data.height = height
	root = Tk()
	root.resizable(width=False, height=False) # prevents resizing window
	init(data)
	# create the root and the canvas
	canvas = Canvas(root, width=data.width, height=data.height)
	canvas.configure(bd=0, highlightthickness=0)
	canvas.pack()


	# set up events
	root.bind("<Button-1>", lambda event:
							mousePressedWrapper(event, canvas, data))
	root.bind("<Key>", lambda event:
							keyPressedWrapper(event, canvas, data))
	redrawAll(canvas, data)
	# and launch the app

	if RUN_FLAG==False:
		root.destroy()

	root.mainloop()  # blocks until window closed

	print("bye!")


runInputPage(1200, 800)