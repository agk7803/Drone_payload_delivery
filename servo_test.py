#!/usr/bin/env python3

from pymavlink import mavutil
import time

################ CONFIG ################
PORT = "/dev/ttyAMA0"
BAUD = 921600

SERVO_CHANNEL = 10      # AUX output number
PWM_OPEN = 800         # adjust as needed
PWM_CLOSE = 2470        # adjust as needed

################ CONNECT ################
print("Connecting to vehicle...")
master = mavutil.mavlink_connection(PORT, baud=BAUD)

master.wait_heartbeat()
print("Heartbeat received")
print(f"System ID: {master.target_system}, Component ID: {master.target_component}")

################ SERVO FUNCTION ################
def control_servo(servo, pwm):
    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_DO_SET_SERVO,
        0,
        servo,
        pwm,
        0, 0, 0, 0, 0
    )

################ MAIN LOOP ################
print("\nCommands:")
print("  open  → open servo")
print("  close → close servo")
print("  exit  → quit\n")

try:
    while True:
        cmd = input(">> ").strip().lower()

        if cmd == "open":
            print("Opening servo")
            control_servo(SERVO_CHANNEL, PWM_OPEN)

        elif cmd == "close":
            print("Closing servo")
            control_servo(SERVO_CHANNEL, PWM_CLOSE)

        elif cmd == "exit":
            print("Exiting")
            break

        else:
            print("Unknown command. Use: open / close / exit")

except KeyboardInterrupt:
    print("\nInterrupted by user")

print("Done")