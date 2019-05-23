import servo

def closeDoor(pwm):
	servo.SetAngle(0,pwm)
	print("The door is closed.")
