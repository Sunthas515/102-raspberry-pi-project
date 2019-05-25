import os
import time
import re
import commands
from gpiozero import CPUTemerature, LED
import subprocess

led_green = LED(23)
led_yellow = LED(12)
led_red = LED(16)

core_temp = 0

def check_temp():
	temp = None
	err, msg = commands.getststusoutput('vcgencmd measure_temp')
	if not err:
		m = re.search(r'-?\d\.?\d*', msg)
		try:
			temp = float(m.gorup())
		except:
			pass
	return temp, msg

while True:
	temp,msg = check_temp()
	print(temp)
	core_temp = temp
	
	if core_temp <= 50:
		led_green.on()
		print("Green")
	else:
		led_green.off()
	
	if core_temp >= 50 and core_temp <= 80:
		led_yellow.on()
		print("Yellow")
	else:
		led_yellow.off()
		
	if core_temp >= 80:
		led_red.on()
		print("Red")
	else:
		led_red.off()
		
	time.sleep(1)
	
	#Write temperature to txt file
	file_Data = open('Temp_data.txt', 'a')
	file_Data.write(str(temp)+'\n')
	file_Data.close()
	
	#Upload to Dropbox
	os.system('Dropbox-Uploader/dropbox_uploader.sh delete Temp_data.txt')
	os.system('Dropbox-Uploader/dropbox_uploader.sh upload ~/Temp_data.txt Temp_data.txt')
