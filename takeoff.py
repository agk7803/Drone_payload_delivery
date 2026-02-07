from pymavlink import mavutil
import time

def set_param(master, name, value):
    master.mav.param_set_send(
        master.target_system,
        master.target_component,
        name.encode('utf-8'),
        float(value),
        mavutil.mavlink.MAV_PARAM_TYPE_REAL32
    )
    time.sleep(1)

print("Connecting to vehicle...")
master = mavutil.mavlink_connection(
    "/dev/ttyAMA0",
    baud=921600
)

master.wait_heartbeat()
print("Heartbeat received")

# Set GUIDED mode
print("Setting GUIDED mode...")
master.set_mode_apm("GUIDED")
time.sleep(2)

# Disable arming checks (SITL only)
print("Disabling arming checks...")
set_param(master, "ARMING_CHECK", 0)

# Arm
print("Arming...")
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
    0,
    1, 0, 0, 0, 0, 0, 0
)

master.motors_armed_wait()
print("Armed")

time.sleep(5)

# Takeoff to 5 meters
altitude = 5
print("Taking off...")
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,
    0,
    0, 0, 0, 0,
    0, 0,
    altitude
)

time.sleep(5)

# Hold at 5m
print("Holding at 5m...")
time.sleep(5)

# Land
print("Landing...")
master.set_mode_apm("LAND")

time.sleep(5)
print("Mission complete")