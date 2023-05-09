import logging
import time
import Adafruit_DHT
import tinytuya
import colorlog

# Configure logging to save to a file and include the temperature in the message
logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = colorlog.ColoredFormatter(
    '%(asctime)s - %(log_color)s%(levelname)s - Temperature: %(temperature)s - Humidity: %(humidity)s - %(message)s',
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
    }
)
file_handler = logging.FileHandler('smart_plug.log')
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logging.Formatter.converter = time.gmtime

# Connect to Tuya Cloud
c = tinytuya.Cloud(
    apiRegion="eu",
    apiKey="5fa3aeh894r74w9ughv4",
    apiSecret="8e0e8536dc1d43eca989c8d65c0f7970",
    apiDeviceID="bf75b215f8323e600fo47c"
)

#humidity = ""
#temperature = ""
# Display list of devices
devices = c.getdevices()
#logging.info(f"Device List: {devices}")

# Select a Device ID to monitor
device_id = "bf75b215xxxxxxxxxxx" # Put your Device ID to monitor
device_id2 = "bfe8639238xxxxxxxx" # Put your Device ID to monitor
#logging.info(f"Monitoring Smart Plug with ID {device_id}")

# Define the DHT22 sensor pin
DHT_PIN = 4

retry_limit = 50

while True:
    for attempt in range(retry_limit):
          
        try:
            # Read the humidity and temperature levels from the DHT22 sensor
            humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, DHT_PIN)
        
            if humidity is None or temperature is  None:
                logging.CRITICAL("Sensor not Working")
                raise Exception("Sensor not working")
            else:
                break
            
        except Exception as e:
            
            if attempt < retry_limit - 1:
                logging.error(f"Error: {e}. Retrying... (Attempt {attempt + 1}/{retry_limit})")
                time.sleep(5)
                continue
            else:
                logging.critical(f"Error: {e}. Maximum retries reached. Closing program.")
                exit()
            
    if humidity is not None and temperature is not None:
        # Log the humidity and temperature levels
        #logging.info(f"Humidity: {humidity:.1f}%, Temperature: {temperature:.1f}°C")
        humidity = round(humidity, 2)
        temperature = round(temperature, 2)

        if humidity < 88:
            # Turn on the Tuya smart socket
            commands = {
                "commands": [
                    {"code": "switch_1", "value": True},
                    {"code": "countdown_1", "value": 0},
                ]
            }
            #logging.debug(f"Monitoring Smart Plug with ID {device_id}")
            logging.info("Sending command to Turn On Humidifier.", extra={'temperature': temperature, 'humidity': humidity})
            result = c.sendcommand(device_id, commands)
            #time.sleep(80)

            # Turn off the Tuya smart socket
            #commands = {
            #    "commands": [
            #        {"code": "switch_1", "value": False},
            #        {"code": "countdown_1", "value": 0},
            #    ]
            #}
            ##logging.debug(f"Monitoring Smart Plug with ID {device_id}")
            #logging.info("Sending command to Turn off Humidifier.", extra={'temperature': temperature, 'humidity': humidity})
            #result = c.sendcommand(device_id, commands)
            #time.sleep(10)

        elif humidity > 94:
            # Turn off the Tuya smart socket
            commands = {
                "commands": [
                    {"code": "switch_1", "value": False},
                    {"code": "countdown_1", "value": 0},
                ]
            }
            #logging.debug(f"Monitoring Smart Plug with ID {device_id}")
            logging.info("Sending command to Turn off Humidifier.", extra={'temperature': temperature, 'humidity': humidity})
            result = c.sendcommand(device_id, commands)
        
        if temperature < 19.5:
            # Turn on the Tuya smart socket
            commands = {
                "commands": [
                    {"code": "switch_1", "value": True},
                    {"code": "countdown_1", "value": 0},
                ]
            }
            
            #logging.debug(f"Monitoring Smart Plug with ID {device_id}")
            logging.info("Sending command to Turn On Heater.", extra={'temperature': temperature, 'humidity': humidity})
            result = c.sendcommand(device_id2, commands)
            time.sleep(50)
            # Turn off the Tuya smart socket
            commands = {
                "commands": [
                    {"code": "switch_1", "value": False},
                    {"code": "countdown_1", "value": 0},
                ]
            }
            #logging.debug(f"Monitoring Smart Plug with ID {device_id}")
            logging.info("Sending command to Turn off Heater.", extra={'temperature': temperature, 'humidity': humidity})
            result = c.sendcommand(device_id2, commands)
            time.sleep(10)
        
    
        elif temperature > 20:
            # Turn off the Tuya smart socket
            commands = {
                "commands": [
                    {"code": "switch_1", "value": False},
                    {"code": "countdown_1", "value": 0},
                ]
            }
            #logging.debug(f"Monitoring Smart Plug with ID {device_id}")
            logging.info("Sending command to Turn off Heater.", extra={'temperature': temperature, 'humidity': humidity})
            result = c.sendcommand(device_id2, commands)

    # Wait for 1 minute before checking again
    #logging.DEBUG(f"Monitoring Smart Plug with ID {device_id}")
    logging.info("Waiting 30sec...", extra={'temperature': temperature, 'humidity': humidity})
    time.sleep(30)
