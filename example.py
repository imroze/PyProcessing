from PyProcessing import PyProcessing
from PVector import PVector

vecs = [] # list storing PVectors representing positions of chaser circles 
img = None

class PyProcessingSubclass(PyProcessing):

	def setup(self):
		global img
		self.size(600,600)
		self.frameRate(60)
		img = self.loadImage('bgd_img.jpg')

	def draw(self):
		global vecs,img
		self.image(img,0,0)
		self.fill(0,0,0)
		self.textSize(20)
		self.text("Mouse Pointer Chasers",self.width*0.5,self.height*0.1)
		self.fill(0,206,209)
		self.stroke(0,50,0)
		self.strokeWeight(4)
		# draw and move all chaser circles
		for vec in vecs:
			self.ellipse(vec.x,vec.y,40,40)
			# create a unit vector in direction of mouse pointer
			# use it as velocity and add to position
			veloc = PVector( self.mouseX-vec.x , self.mouseY-vec.y)
			veloc.normalize()  
			vec.x += veloc.x
			vec.y += veloc.y
		self.textSize(10)
		self.fill(255,255,255)
		# draw blinking text by drawing during first 20 in every 30 frames
		if self.frameCount % 30 < 20:
			self.text("Press ENTER Key to Exit",self.width*0.5,self.height*0.95)

	def keyPressed(self):
		# exit if Enter key pressed
		if self.keyCode == self.ENTER :
			self.exit()

	def mousePressed(self):
		global vecs
		# create chaser vector wiht position of mouse pointer and add to list
		new_vec = PVector(self.mouseX,self.mouseY)
		vecs.append(new_vec)

def main():
	pyproc = PyProcessingSubclass()
	pyproc.run_Processing()

if __name__== "__main__":
	main()