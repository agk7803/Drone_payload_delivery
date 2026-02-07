<h1>🚁 Autonomous Drone Payload Delivery Using Waypoints</h1>

<p>
This project implements an autonomous drone payload delivery system using GPS waypoints and a Raspberry Pi as a companion flight computer. The drone follows preplanned missions, deploys payloads accurately, and returns safely using MAVLink-based communication and custom Python scripts.
</p>

<hr>

<h2>📌 Project Overview</h2>

<ul>
  <li><b>Flight Controller:</b> Pixhawk (ArduPilot)</li>
  <li><b>Companion Computer:</b> Raspberry Pi</li>
  <li><b>Communication:</b> MAVLink (Serial/USB)</li>
  <li><b>Navigation:</b> GPS Waypoints</li>
  <li><b>Payload System:</b> Servo-based release mechanism</li>
</ul>

<p>
The Raspberry Pi handles mission logic, telemetry monitoring, and payload deployment while the Pixhawk manages flight stabilization and navigation.
</p>

<hr>

<h2>⚙️ System Workflow</h2>

<ol>
  <li>Waypoints are uploaded using Mission Planner.</li>
  <li>Drone arms and takes off autonomously.</li>
  <li>Raspberry Pi monitors mission progress.</li>
  <li>Payload is released at the target waypoint.</li>
  <li>Drone returns and lands automatically.</li>
</ol>

<hr>

<h2>📂 Script Functionalities</h2>

<h3>1️⃣ arm_test.py</h3>
<p><b>Purpose:</b> Basic arming verification</p>
<ul>
  <li>Tests communication with flight controller</li>
  <li>Checks if the drone can arm successfully</li>
  <li>Used for initial system validation</li>
</ul>

<h3>2️⃣ arm_indoors.py</h3>
<p><b>Purpose:</b> Indoor/bench testing</p>
<ul>
  <li>Arms the drone without full mission execution</li>
  <li>Performs low-altitude or no-lift testing</li>
  <li>Useful for hardware and safety checks</li>
</ul>

<h3>3️⃣ takeoff.py</h3>
<p><b>Purpose:</b> Autonomous takeoff testing</p>
<ul>
  <li>Arms the drone</li>
  <li>Commands automatic takeoff</li>
  <li>Reaches a predefined altitude</li>
  <li>Used to validate altitude control</li>
</ul>

<h3>4️⃣ servo_test.py</h3>
<p><b>Purpose:</b> Payload mechanism testing</p>
<ul>
  <li>Controls servo motor manually</li>
  <li>Tests opening and closing of payload release</li>
  <li>Ensures reliable deployment mechanism</li>
</ul>

<h3>5️⃣ mission.py</h3>
<p><b>Purpose:</b> Final delivery mission</p>
<ul>
  <li>Connects to flight controller via MAVLink</li>
  <li>Starts waypoint mission</li>
  <li>Monitors GPS and mission status</li>
  <li>Triggers payload release at target point</li>
  <li>Handles return and landing sequence</li>
</ul>

<p>
This script represents the complete autonomous delivery workflow.
</p>

<hr>

<h2>✨ Key Features</h2>

<ul>
  <li>Fully autonomous flight and delivery</li>
  <li>Waypoint-based navigation</li>
  <li>Real-time telemetry monitoring</li>
  <li>Reliable servo-based payload drop</li>
  <li>Modular and testable script structure</li>
  <li>Scalable for future upgrades</li>
</ul>

<hr>

<h2>🎯 Applications</h2>

<ul>
  <li>Medical supply delivery</li>
  <li>Campus logistics</li>
  <li>Remote area transportation</li>
  <li>Research and UAV development</li>
  <li>Competition projects</li>
</ul>

<hr>

<h2>🚀 Future Improvements</h2>

<ul>
  <li>Obstacle avoidance</li>
  <li>Computer vision integration</li>
  <li>Live mission dashboard</li>
  <li>Cloud-based tracking</li>
  <li>Redundant safety systems</li>
</ul>

<hr>

<h2>📄 License</h2>

<p>
This project is open-source and intended for educational and research purposes.
</p>
