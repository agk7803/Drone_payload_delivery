🚁 Autonomous Drone Payload Delivery Using Waypoints

This project implements an autonomous drone payload delivery system using GPS waypoints and a Raspberry Pi as a companion flight computer. The drone follows preplanned missions, deploys payloads accurately, and returns safely using MAVLink-based communication and custom Python scripts.

⸻

📌 Project Overview
	•	Flight Controller: Pixhawk (ArduPilot)
	•	Companion Computer: Raspberry Pi
	•	Communication: MAVLink (Serial/USB)
	•	Navigation: GPS Waypoints
	•	Payload System: Servo-based release mechanism

The Raspberry Pi handles mission logic, telemetry monitoring, and payload deployment while the Pixhawk manages flight stabilization and navigation.

⸻

⚙️ System Workflow
	1.	Waypoints are uploaded using Mission Planner.
	2.	Drone arms and takes off autonomously.
	3.	Raspberry Pi monitors mission progress.
	4.	Payload is released at the target waypoint.
	5.	Drone returns and lands automatically.

⸻

📂 Script Functionalities

1️⃣ arm_test.py

Purpose: Basic arming verification
	•	Tests communication with flight controller
	•	Checks if the drone can arm successfully
	•	Used for initial system validation

2️⃣ arm_indoors.py

Purpose: Indoor/bench testing
	•	Arms the drone without full mission execution
	•	Performs low-altitude or no-lift testing
	•	Useful for hardware and safety checks

3️⃣ takeoff.py

Purpose: Autonomous takeoff testing
	•	Arms the drone
	•	Commands automatic takeoff
	•	Reaches a predefined altitude
	•	Used to validate altitude control

4️⃣ servo_test.py

Purpose: Payload mechanism testing
	•	Controls servo motor manually
	•	Tests opening and closing of payload release
	•	Ensures reliable deployment mechanism

5️⃣ mission.py

Purpose: Final delivery mission
	•	Connects to flight controller via MAVLink
	•	Starts waypoint mission
	•	Monitors GPS and mission status
	•	Triggers payload release at target point
	•	Handles return and landing sequence

This script represents the complete autonomous delivery workflow.

⸻

✨ Key Features
	•	Fully autonomous flight and delivery
	•	Waypoint-based navigation
	•	Real-time telemetry monitoring
	•	Reliable servo-based payload drop
	•	Modular and testable script structure
	•	Scalable for future upgrades

⸻

🎯 Applications
	•	Medical supply delivery
	•	Campus logistics
	•	Remote area transportation
	•	Research and UAV development
	•	Competition projects

⸻

🚀 Future Improvements
	•	Obstacle avoidance
	•	Computer vision integration
	•	Live mission dashboard
	•	Cloud-based tracking
	•	Redundant safety systems

⸻

📄 License

This project is open-source and intended for educational and research purposes.
