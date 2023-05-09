# Fruiting Room Temperature and Humidity Control with Tuya Smart Device

This code uses the Adafruit_DHT library to read temperature and humidity levels from a DHT22 sensor and control the temperature and humidity levels in a fruiting room with a Tuya smart device. The Tuya smart device can be turned on or off using the tinytuya library.

# Requirements
Raspberry Pi with Python 3 installed
Adafruit_DHT library
tinytuya library
Tuya Smart device
DHT22 sensor
Tuya Cloud account with an API key, API secret, and device ID

# Usage

Connect the DHT22 sensor to the Raspberry Pi.
Create a Tuya Cloud account and obtain an API key, API secret, and device ID for the Tuya Smart device.
Install the required libraries using pip: pip install Adafruit_DHT tinytuya colorlog
Configure the logger settings to save to a file and include the temperature and humidity levels in the message.
Set the DHT_PIN variable to the GPIO pin connected to the DHT22 sensor.
Set the device_id and device_id2 variables to the device IDs for the Tuya Smart devices.
Set the desired temperature and humidity levels in the if statements.
Run the
script using python fruiting_room_control.py.

# Notes
The Tuya Smart device is turned on or off based on the humidity and temperature levels. If the humidity is below the desired level, the humidifier is turned on. If the humidity is above the desired level, the humidifier is turned off. If the temperature is below the desired level, the heater is turned on. If the temperature is above the desired level, the heater is turned off.
The retry_limit variable controls the number of times the DHT22 sensor is read in case of an error.
The time.sleep function can be adjusted to control the length of time the Tuya Smart device is turned on or off.

## we are passionate about growing high-quality mushrooms. We know that controlling the temperature and humidity in our fruiting room is essential for producing the best possible harvest. That's why we have developed a smart system that allows us to monitor and control these conditions with ease.

Our code, which is available on Github, uses an Adafruit DHT sensor to measure temperature and humidity levels. Based on these readings, it sends commands to a Tuya smart device to turn on and off a humidifier or a heater, as needed. This way, we can ensure that the fruiting room stays within the optimal temperature and humidity range at all times.

If you're interested in growing your own mushrooms, we invite you to visit our website, [smurfmushroom.co.uk] . Here, you can learn more about our growing process and our commitment to sustainability. We believe that mushrooms are not only delicious but also incredibly beneficial for our health and the environment. So why not give them a try? With our smart system, you can be sure that you'll get the best possible results.
