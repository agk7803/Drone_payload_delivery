#!/usr/bin/env python3

from pymavlink import mavutil
import time

PORT = "/dev/ttyAMA0"
BAUD = 921600

def set_mode(master, mode):
    master.set_mode_apm(mode)
    while True:
        hb = master.recv_match(type='HEARTBEAT', blocking=True)
        if mavutil.mode_string_v10(hb) == mode:
            break
    print(f"Mode set to {mode}")

print("Connecting to vehicle...")
master = mavutil.mavlink_connection(PORT, baud=BAUD)
master.wait_heartbeat()
print("Heartbeat received")

# Set GUIDED mode
set_mode(master, "GUIDED")

# Arm motors
print("Arming motors...")
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
    0,
    1, 0, 0, 0, 0, 0, 0
)

master.motors_armed_wait()
print("Motors armed")

# Hold armed for 5 seconds
time.sleep(5)

# Disarm motors
print("Disarming motors...")
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
    0,
    0, 0, 0, 0, 0, 0, 0
)

master.motors_disarmed_wait()
print("Motors disarmed")

print("Arm test complete")
