while True:
	servos[3].angle = 0
	for i in range(90):
		servos[3].angle = i*2
		time.sleep(0.025)
	time.sleep(0.5)
	servos[3].angle = 0
