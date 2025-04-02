import serial
import time

# Set up the serial connection to Arduino
ser = serial.Serial('COM5', 9600)  # Replace 'COM5' with your Arduino's port "/dev/ttyUSB0" for Linux

ser.timeout = 1  # Set a timeout for reading from the serial port
time.sleep(2)  # Give Arduino time to reset

def send_pwm_values(pwm_values):
    # Ensure we are sending exactly 4 PWM values
    if len(pwm_values) == 4:
        for pwm_value in pwm_values:
            if 1100 <= pwm_value <= 1900:  # Valid PWM range from 1100 to 1900
                # Split the PWM value into two bytes (high byte and low byte)
                high_byte = pwm_value >> 8  # Get the high byte
                low_byte = pwm_value & 0xFF  # Get the low byte
                ser.write(bytes([high_byte, low_byte]))  # Send both bytes
            else:
                print("Error: PWM value out of range (1100-1900)")
    else:
        print("Error: You must send exactly 4 PWM values.")

# Example usage:
pwm_values = [1280, 1800, 1500, 1750]  # PWM values to send to Arduino within the 1100-1900 range
send_pwm_values(pwm_values)

# Wait a few seconds to see the result
time.sleep(2)

# Close the serial connection
ser.close()
