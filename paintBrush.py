import random

def pickUpPaintBrush(grip):
	if grip:
		print("You picked up the paint brush")
		putBrushInSoup(random.randint(0,1))
	else:
		print("You couldn't pick up the brush")
		pickUpPaintBrush(random.randint(0,1))

def putBrushInSoup(grip):
	if grip:
		print("You put the brush in the soup")
		applyToFace(random.randint(0,1))
	else:
		print("You dropped the brush in the soup")
		pickUpPaintBrush(random.randint(0,1))

def applyToFace(grip):
	if grip:
		print("You applied it to your face")
	else:
		print("You could not apply to face")
		pickUpPaintBrush(random.randint(0,1))

pickUpPaintBrush(random.randint(0,1))

