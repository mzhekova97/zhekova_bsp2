import servo

def openDoor(pwm):
	servo.SetAngle(90,pwm)
	print("The door is open")

