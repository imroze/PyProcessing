import pygame
import time

class PyProcessing(object):

	def __init__(self):
		self.fillCol = [0,0,0]
		self.strokeCol = [0,0,0]
		self.frame_rate = 60
		self.stroke_weight = 2
		self.fontSize = 12
		self.frameCount = 1
		self.mouseX = 0
		self.mouseY = 0
		self.doFill = True
		self.keyCode = 0
		self.font=[]
		self.clock = pygame.time.Clock()
		self.exiting = False
		self.size(300,300)
		self.frameRate(60)
		self.ESC = 27
		self.ENTER = 13
		self.SHIFT = 103
		self.LEFT = 276
		self.UP = 273
		self.RIGHT = 275
		self.DOWN = 274 

	def size(self,w,h):
		self.width = w
		self.height = h
		self.initScreen()

	def ellipse(self,x,y,d1,d2):
		x = int( x-d1/2 )
		y = int( y-d2/2 )
		if self.doFill:
			pygame.draw.ellipse(self.screen, self.fillCol , [ x, y, d1, d2],width=0)
		pygame.draw.ellipse(self.screen, self.strokeCol , [x, y, d1, d2],width=self.stroke_weight)

	def rect(self,x,y,w,h):
		if self.doFill:
			pygame.draw.rect(self.screen, self.fillCol, [x, y, w, h],width=0)
		pygame.draw.rect(self.screen, self.strokeCol, [x, y, w, h],width=self.stroke_weight)

	def line(self,x1,y1,x2,y2):
		pygame.draw.line(self.screen, self.strokeCol, [x1, y1], [x2,y2], width=self.stroke_weight)

	def triangle(self,x1,y1,x2,y2,x3,y3):
		pygame.draw.polygon(self.screen, self.strokeCol, [[x1, y1], [x2,y2], [x3, y3]],width=self.stroke_weight)
		if self.doFill:
			pygame.draw.polygon(self.screen, self.fillCol, [[x1, y1], [x2,y2], [x3, y3]],width=0)
			
	def text(self,stri,x,y):
		txt = self.font.render(stri, True, (self.fillCol[0],self.fillCol[1],self.fillCol[2])) 
		textRect = txt.get_rect()  
		textRect.center = (x,y) 
		self.screen.blit(txt, textRect)

	def text_vertical(self,stri,x,y):
		yn = y
		for i in range( len(stri)  ):
			self.text(stri[i],x,yn)
			yn += self.fontSize

	def millis(self,ms):
		time.sleep( ms / 1000.0 )

	def textSize(self,txt_size):
		self.fontSize = txt_size
		self.font = pygame.font.Font('freesansbold.ttf',self.fontSize)

	def fill(self,r,g,b):
		self.doFill = True
		self.fillCol = [r,g,b]

	def noFill(self):
		self.doFill = False

	def strokeWeight(self,stroke_weight):
		self.stroke_weight = stroke_weight

	def stroke(self,r,g,b):
		self.strokeCol = [r,g,b]

	def background(self,r,g,b):
		self.screen.fill([r,g,b])

	def exit(self):
		self.exiting = True

	def frameRate(self,val):
		self.frame_rate = val

	def initFont(self):
		self.font = pygame.font.Font('freesansbold.ttf',self.fontSize)

	def setup(self):
		self.size(300,300)
		self.frameRate(30)

	def draw(self):
		self.background(200,200,200)

	def mousePressed(self):
		print( (self.mouseX,self.mouseY) )

	def keyPressed(self):
		print(self.keyCode)
		if self.keyCode == self.ENTER :
			self.exit()

	def initScreen(self):
		self.screen = pygame.display.set_mode([self.width,self.height])

	def setFont(self,fntName,fntSz):
		self.fontSize = fntSz
		self.font = pygame.font.Font(fntName, fntSz)

	def loadImage(self,filePath):
		loaded_image = pygame.image.load(filePath)
		return loaded_image

	def image(self,img_obj,x,y):
		self.screen.blit(img_obj, (x,y) )

	def saveFrame(self,filePath=None):
		if filePath:
			pygame.image.save(self.screen, filePath)
		else:
			pygame.image.save(self.screen,"screenshot.jpg")

	def run_Processing(self):
		pygame.init()
		self.initFont()
		self.setup()
		
		while not self.exiting:
			start_time = time.time()
			event = pygame.event.poll()
			if event.type == pygame.MOUSEMOTION:
				self.mouseX, self.mouseY = event.pos
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				self.mousePressed()
			if event.type == pygame.KEYDOWN:
				self.keyCode = event.key
				self.keyPressed()
			self.draw()
			pygame.display.flip()
			reqDelay =  1.0 / self.frame_rate
			elapsed_time = time.time() - start_time
			sleepSecs = reqDelay - elapsed_time
			if sleepSecs > 0:
				self.millis(sleepSecs*1000)
			self.frameCount += 1