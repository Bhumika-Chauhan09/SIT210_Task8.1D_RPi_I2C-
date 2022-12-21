#System management bus library preinstalled after enabling I2C option
#its is to0 implement the I2c interface 
import smbus
import time

#For the BH1750 sensor, I2C addresses 7-bit addresses in hexadecimal format.
address = 0x23	#BH1750 sensor default address 
start_on = 0x01	#represent 1 if the power is on or for starting the data transfer
stop_on = 0x00	#represent 0 if the power is off or  for stopping the data transfer .
reset = 0x07	#An address used for resetting the whole process

#Insiating the smbus library
bus = smbus.SMBus(1)

#A fucntion to read the data from the sensor in bytes and convert it to recognizable values
def Light_Reading():
	newAddress = bus.read_i2c_block_data(address, address)
	value = light_intensity(newAddress)
	return value
	
def light_intensity(newAddress):
	conversion = ((newAddress[1] + (256 * newAddress[0]))/1.2)
	return conversion

#Main conditions and overall output
try:
	while 1:
		intensity = Light_Reading()
		print(f"Reading: {intensity}")
		
		if(intensity >= 3000):
			print("Status: Too bright")
		elif(intensity >= 500 and intensity < 3000):
			print("Status: Bright")
		elif(intensity >= 100 and intensity < 500):
			print("Status: Medium")
		elif(intensity > 50 and intensity < 100):
			print("Status: Dark")
		elif(intensity < 50):
			print("Status: Too dark")
		time.sleep(1)

except KeyboardInterrupt:
	print("Exitting")