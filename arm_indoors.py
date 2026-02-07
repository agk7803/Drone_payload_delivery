#!/usr/bin/env python3

from pymavlink import mavutil
import time

PORT = "/dev/ttyAMA0"
BAUD = 921600
ARM_HOLD_TIME = 2  # seconds to stay armed

print("Connecting to vehicle...")
master = mavutil.mavlink_connection(PORT, baud=BAUD)
master.wait_heartbeat()
print("Heartbeat received")

print(f"System ID: {master.target_system}, Component ID: {master.target_component}")

# ------------------ SET STABILIZE MODE ------------------
print("Setting STABILIZE mode...")
master.set_mode_apm("STABILIZE")

# Confirm mode change
while True:
    hb = master.recv_match(type="HEARTBEAT", blocking=True)
    if mavutil.mode_string_v10(hb) == "STABILIZE":
        break

print("Mode confirmed: STABILIZE")

# ------------------ ARM ------------------
print("Arming motors...")
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
    0,
    1,  # ARM
    0, 0, 0, 0, 0, 0
)

master.motors_armed_wait()
print("Motors ARMED")

# ------------------ HOLD ------------------
print(f"Holding armed for {ARM_HOLD_TIME} seconds...")
time.sleep(ARM_HOLD_TIME)

# ------------------ DISARM ------------------
print("Disarming motors...")
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
    0,
    0,  # DISARM
    0, 0, 0, 0, 0, 0
)

master.motors_disarmed_wait()
print("Motors DISARMED")

print("Indoor STABILIZE arm test complete")