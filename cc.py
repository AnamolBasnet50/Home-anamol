from pyfirmata import Arduino, util
import time

board = Arduino('COM5') # Replace 'COM3' with the name of your serial port

analog_input = board.get_pin('a:0:i') # Get the analog input pin connected to the microphone
led = board.get_pin('d:13:o') # Get the digital output pin connected to the LED

iter = util.Iterator(board)
iter.start()

analog_input.enable_reporting()

clap_count = 0 # Initialize a counter for the number of claps
last_clap_time = 0 # Initialize a variable to store the time of the last clap

while True:
    soundLevel = analog_input.read() # Read the data from the analog input pin

    if soundLevel is not None and soundLevel > 0.54: # Check if the sound level is above a certain threshold
        current_time = time.time() # Get the current time

        # Check if the time since the last clap is less than 1 second
        if current_time - last_clap_time < 1:
            clap_count += 1 # Increase the clap count
        else:
            clap_count = 1 # Reset the clap count

        last_clap_time = current_time # Update the time of the last clap

    if clap_count == 1: # If a single clap is detected
        led.write(1) # Turn the LED on
        
        
    elif clap_count == 2: # If two claps are detected
        led.write(0) # Turn the LED off
        clap_count = 0 # Reset the clap count

    time.sleep(0.1) # Sleep for a short period to avoid overloading the serial port
