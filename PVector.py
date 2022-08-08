# Based on following repo by Alexandre B A Villares, with small changes
# https://gist.github.com/villares/5c476cbc44c1153fed159eae36fc016b

import math
from math import sqrt

class PVector:

	def __init__(self, x=0, y=0, z=0):
		self.x = x
		self.y = y
		self.z = z        
		self.add = self.__instance_add__
		self.sub = self.__instance_sub__
		self.mult = self.__instance_mult__
		self.div = self.__instance_div__
		self.cross = self.__instance_cross__
		self.dist = self.__instance_dist__
		self.dot = self.__instance_dot__
		self.lerp = self.__instance_lerp__

	def mag(self):
		return math.sqrt(self.magSq())

	def magSq(self):
		return self.x * self.x + self.y * self.y + self.z * self.z

	def setMag(self, mag):
		return self.normalize().mult(n)
 
	def normalize(self):
		mag = self.mag()
		if mag != 0:
			self.mult(1 / mag)
		return self

	def limit(self, max_mag):
		mSq = self.magSq()
		if mSq > max_mag * max_mag:
			self.div(math.sqrt(mSq)).mult(max_mag)
		return self

	def heading(self):
		return math.atan2(self.y, self.x)

	def rotate(self, angle):
		new_h = self.heading() + angle
		mag = self.mag()
		self.x = math.cos(new_h) * mag;
		self.y = math.sin(new_h) * mag;
		return self

	def __instance_add__(self, *args):
		if len(args) == 1:
			return PVector.add(self, args[0], self)
		else:
			return PVector.add(self, PVector(*args), self)

	def __instance_sub__(self, *args):
		if len(args) == 1:
			return PVector.sub(self, args[0], self)
		else:
			return PVector.sub(self, PVector(*args), self)

	def __instance_mult__(self, o):
		return PVector.mult(self, o, self)

	def __instance_div__(self, f):
		return PVector.div(self, f, self)

	def __instance_cross__(self, o):
		return PVector.cross(self, o, self)

	def __instance_dist__(self, o):
		return PVector.dist(self, o)

	def __instance_dot__(self, *args):
		if len(args) == 1:
			v = args[0]
		else:
			v = args
		return self.x * v[0] + self.y * v[1] + self.z * v[2]

	def __instance_lerp__(self, *args):
		if len(args) == 2:
			return PVector.lerp(self, args[0], args[1], self)
		else:
			vx, vy, vz, f = args
			return PVector.lerp(self, PVector(vx, vy, vz), f, self)

	def get(self):
		return PVector(self.x, self.y, self.z)

	def copy(self):
		return PVector(self.x, self.y, self.z)

	def __getitem__(self, k):
		return getattr(self, ('x', 'y', 'z')[k])

	def __setitem__(self, k, v):
		setattr(self, ('x', 'y', 'z')[k], v)

	def __copy__(self):
		return PVector(self.x, self.y, self.z)

	def __deepcopy__(self, memo):
		return PVector(self.x, self.y, self.z)

	def __repr__(self):  # PROVISÓRIO
		return f'PVector({self.x}, {self.y}, {self.z})'
	
	def set(self,ax,ay,az):
		self.x, self.y, self.z = (ax,ay,az)

	@classmethod
	def add(cls, a, b, dest=None):
		if dest is None:
			return PVector(a.x + b[0], a.y + b[1], a.z + b[2])
		dest.set(a.x + b[0], a.y + b[1], a.z + b[2])
		return dest

	@classmethod
	def sub(cls, a, b, dest=None):
		if dest is None:
			return PVector(a.x - b[0], a.y - b[1], a.z - b[2])
		dest.set(a.x - b[0], a.y - b[1], a.z - b[2])
		return dest

	@classmethod
	def mult(cls, a, b, dest=None):
		if dest is None:
			return PVector(a.x * b, a.y * b, a.z * b)
		dest.set(a.x * b, a.y * b, a.z * b)
		return dest

	@classmethod
	def div(cls, a, b, dest=None):
		if dest is None:
			return PVector(a.x / b, a.y / b, a.z / b)
		dest.set(a.x / b, a.y / b, a.z / b)
		return dest

	@classmethod
	def dist(cls, a, b):
		return a.dist(b)

	@classmethod
	def dot(cls, a, b):
		return a.dot(b)

	def __add__(a, b):
		return PVector.add(a, b, None)

	def __sub__(a, b):
		return PVector.sub(a, b, None)

	def __isub__(a, b):
		a.sub(b)
		return a

	def __iadd__(a, b):
		a.add(b)
		return a

	def __mul__(a, b):
		if not isinstance(b, Number):
			raise TypeError(
				"The * operator can only be used to multiply a PVector by a number")
		return PVector.mult(a, float(b), None)

	def __rmul__(a, b):
		if not isinstance(b, Number):
			raise TypeError(
				"The * operator can only be used to multiply a PVector by a number")
		return PVector.mult(a, float(b), None)

	def __imul__(a, b):
		if not isinstance(b, Number):
			raise TypeError(
				"The *= operator can only be used to multiply a PVector by a number")
		a.mult(float(b))
		return a

	def __truediv__(a, b):
		if not isinstance(b, Number):
			raise TypeError(
				"The * operator can only be used to multiply a PVector by a number")
		return PVector(a.x / float(b), a.y / float(b), a.z / float(b))

	def __itruediv__(a, b):
		if not isinstance(b, Number):
			raise TypeError(
				"The /= operator can only be used to multiply a PVector by a number")
		a.set(a.x / float(b), a.y / float(b), a.z / float(b))
		return a

	def __eq__(a, b):
		return a.x == b[0] and a.y == b[1] and a.z == b[2]

	def __lt__(a, b):
		return a.magSq() < b.magSq()

	def __le__(a, b):
		return a.magSq() <= b.magSq()

	def __gt__(a, b):
		return a.magSq() > b.magSq()

	def __ge__(a, b):
		return a.magSq() >= b.magSq()

	@classmethod
	def lerp(cls, a, b, f, dest=None):
		v = PVector(a.x, a.y, a.z)
		v.lerp(b, f)
		if dest is None:
			return PVector(v.x, v.y, v.z)
		dest.set(v.x, v.y, v.z)
		return dest

	@classmethod
	def cross(cls, a, b, dest=None):
		x = a.y * b[2] - b[1] * a.z
		y = a.z * b[0] - b[2] * a.x
		z = a.x * b[1] - b[0] * a.y
		if dest is None:
			return PVector(x, y, z)
		dest.set(x, y, z)
		return dest

	@classmethod
	def fromAngle(cls, angle, length=1):
		# based on https://github.com/processing/p5.js/blob/3f0b2f0fe575dc81c724474154f5b23a517b7233/src/math/p5.Vector.js
		return PVector(length * cos(angle), length * sin(angle), 0)

	@classmethod
	def fromAngles(theta, phi, length=1):
		# based on https://github.com/processing/p5.js/blob/3f0b2f0fe575dc81c724474154f5b23a517b7233/src/math/p5.Vector.js
		cosPhi = cos(phi)
		sinPhi = sin(phi)
		cosTheta = cos(theta)
		sinTheta = sin(theta)
		return PVector(length * sinTheta * sinPhi,
					   -length * cosTheta,
					   length * sinTheta * cosPhi)
	@classmethod
	def angleBetween(cls, a, b):
		return math.acos(a.dot(b) / sqrt(a.magSq() * b.magSq()))

	# Other harmless p5js methods

	def equals(self, v):
		return self == v

	def toString(self):
		# Returns a string representation of a vector v by calling String(v) or v.toString().
		# return self.__vector.toString() would be something like "p5.vector
		# Object […, …, …]"
		return str(self)