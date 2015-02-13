import random

def pickUpPaintBrush(grip):
	if grip:
		print("You pick up the paint brush")
		putBrushInSoup(random.randint(0,1))
	else:
		print("You can't pick up the brush")
		pickUpPaintBrush(random.randint(0,1))

def putBrushInSoup(grip):
	if grip:
		print("You put the brush in the soup")
		applyToFace(random.randint(0,1))
	else:
		print("You drop the brush in the soup")
		pickUpPaintBrush(random.randint(0,1))

def applyToFace(grip):
	if grip:
		print("You apply brush to your face")
	else:
		print("You go to eat but drop the brush")
		pickUpPaintBrush(random.randint(0,1))

pickUpPaintBrush(random.randint(0,1))

