from pynput.mouse import Button, Controller
from pynput import mouse
import threading
import time

global stopped
stopped = False

global secs
secs = 0

global p,q
p,q=0,0

mouse2 = Controller()

def on_click(x, y, button, pressed):
	global p,q
	print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
	p=x
	q=y
	if pressed:
		return False

def init():
	global p,q,secs
	print("Welcome to recursive mouse clicker!!")
	print("Please click your mouse on the place you want to click on")
	with mouse.Listener(on_click=on_click) as listener:
		listener.join()
	print("Got the position\n")
	secs = int(input("Enter the time to keep clicking in seconds"))

	#threading.Thread( target=inp_stopper ).start()
	threading.Thread( target=time_stopper ).start()

	mouse.position = (p,q)
	while stopped==False:
		print("Clicked")
		mouse2.click(Button.left, 1)

"""
def inp_stopper():
	global stopped
	while stopped==False:
		try: #used try so that if user pressed other than the given key error will not be shown
			if keyboard.is_pressed('q'):#if key 'q' is pressed 
				print('You Pressed quit Key!')
				stopped=True
				break
			else:
				pass
		except:
			pass 
"""
def time_stopper():
	
	global stopped,secs
	print("here",secs)
	time.sleep(secs)
	stopped=True
	print("Stopped time")



if __name__ == '__main__':
	threading.Thread( target=init ).start()