from pymavlink import mavutil
import time
import math

# =================================================
# CONFIG
# =================================================
PORT = "/dev/ttyAMA0"
BAUD = 921600

TAKEOFF_ALT = 4  # meters

# Servo config (as you specified)
SERVO_NUMBER = 10
SERVO_TRIGGER_PWM = 700
SERVO_NEUTRAL_PWM = 2470
SERVO_HOLD_TIME = 2 # seconds

# Waypoint
WP_LAT = 12.642533
WP_LON = 79.938915

# =================================================
# MAVLink HELPERS
# =================================================
def request_fast_position(master, rate_hz=5):
    print("[INFO] Requesting fast GLOBAL_POSITION_INT stream")
    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_SET_MESSAGE_INTERVAL,
        0,
        mavutil.mavlink.MAVLINK_MSG_ID_GLOBAL_POSITION_INT,
        int(1e6 / rate_hz),
        0, 0, 0, 0, 0
    )

def flush_messages(master):
    while master.recv_match(blocking=False):
        pass

def get_position(master):
    while True:
        msg = master.recv_match(type='GLOBAL_POSITION_INT', blocking=False)
        if msg:
            lat = msg.lat / 1e7
            lon = msg.lon / 1e7
            alt = msg.relative_alt / 1000.0
            return lat, lon, alt
        time.sleep(0.05)

def goto_location(master, lat, lon, alt):
    print(f"[NAV] Going to lat={lat}, lon={lon}, alt={alt}")
    master.mav.set_position_target_global_int_send(
        0,
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT_INT,
        0b110111111000,
        int(lat * 1e7),
        int(lon * 1e7),
        alt,
        0, 0, 0,
        0, 0, 0,
        0, 0
    )

def wait_until_altitude(master, target_alt):
    print(f"[WAIT] Climbing to {target_alt} m")
    flush_messages(master)
    while True:
        _, _, alt = get_position(master)
        print(f"[ALT] {alt:.2f} m")
        if alt >= target_alt - 0.5:
            print("[OK] Target altitude reached")
            break
        time.sleep(0.2)

def wait_until_arrival(master, target_lat, target_lon):
    print("[WAIT] Navigating to target position")
    flush_messages(master)
    while True:
        lat, lon, _ = get_position(master)
        dist = math.sqrt((lat - target_lat)**2 + (lon - target_lon)**2)
        print(f"[DIST] {dist}")
        if dist < 0.000005:
            print("[OK] Target position reached")
            break
        time.sleep(0.2)

def wait_until_landed(master):
    print("[WAIT] Waiting for landing")
    flush_messages(master)
    while True:
        _, _, alt = get_position(master)
        print(f"[ALT] {alt:.2f} m")
        if alt < 0.2:
            print("[OK] Touchdown detected")
            break
        time.sleep(0.2)

    print("[INFO] Waiting for motors to disarm")
    master.motors_disarmed_wait()
    print("[OK] Motors disarmed")

def set_servo_pwm(master, servo_num, pwm):
    print(f"[SERVO] SERVO{servo_num} → PWM {pwm}")
    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_DO_SET_SERVO,
        0,
        servo_num,
        pwm,
        0, 0, 0, 0, 0
    )

# =================================================
# CONNECTION
# =================================================
print("[INFO] Connecting to vehicle...")
master = mavutil.mavlink_connection(PORT, baud=BAUD)
master.wait_heartbeat()
print("[OK] Heartbeat received")

request_fast_position(master, 10)

# =================================================
# MODE: GUIDED
# =================================================
print("[MODE] Setting GUIDED")
master.set_mode_apm("GUIDED")
time.sleep(2)

# =================================================
# HOME POSITION
# =================================================
home_lat, home_lon, _ = get_position(master)
print(f"[HOME] lat={home_lat}, lon={home_lon}")

# =================================================
# ARM & TAKEOFF
# =================================================
print("[ACTION] Arming motors")
master.arducopter_arm()
master.motors_armed_wait()
print("[OK] Armed")

print("[ACTION] Takeoff")
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,
    0,
    0, 0, 0, 0,
    0, 0,
    TAKEOFF_ALT
)
wait_until_altitude(master, TAKEOFF_ALT)

# =================================================
# FLY TO WAYPOINT
# =================================================
goto_location(master, WP_LAT, WP_LON, TAKEOFF_ALT)
wait_until_arrival(master, WP_LAT, WP_LON)

# =================================================
# LAND AT WAYPOINT
# =================================================
print("[MODE] LAND at waypoint")
master.set_mode_apm("LAND")
wait_until_landed(master)

# =================================================
# SERVO TRIGGER
# =================================================
print("[ACTION] Servo trigger sequence START")
set_servo_pwm(master, SERVO_NUMBER, SERVO_TRIGGER_PWM)
time.sleep(SERVO_HOLD_TIME)

# =================================================
# RE-ARM & TAKEOFF AGAIN
# =================================================
print("[MODE] Back to GUIDED")
master.set_mode_apm("GUIDED")
time.sleep(1)

print("[ACTION] Re-arming")
master.arducopter_arm()
master.motors_armed_wait()
print("[OK] Armed again")

print("[ACTION] Takeoff again")
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,
    0,
    0, 0, 0, 0,
    0, 0,
    TAKEOFF_ALT
)
wait_until_altitude(master, TAKEOFF_ALT)

# =================================================
# RETURN HOME
# =================================================
goto_location(master, home_lat, home_lon, TAKEOFF_ALT)
wait_until_arrival(master, home_lat, home_lon)

# =================================================
# FINAL LAND
# =================================================
print("[MODE] Final LAND at home")
master.set_mode_apm("LAND")
wait_until_landed(master)

print("🎯 MISSION COMPLETE — NO ERRORS, NO RACE CONDITIONS")
 this is my servo activation code but it lands using waypoint co ords only, i want the drone to go to waypoint using same logic but when reachded waypoint it should start opencv and the rpi cam. it should do the precise landing algorithm- 
