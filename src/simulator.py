import numpy as np
from pyquaternion import Quaternion

timestep = 0.01
end_time = 100
t = 0

# rocket parameters
init_mass = 100
fin_mass = 90
thrust = 1000
burn_time = 10
area = 0.02
drag_coeff = 0.5

# launch site parameters
tower_angle = 0
launch_site_altitude = 0
local_magnetic_field = 0 # TODO: figure out what we need to actually store here

# sensor noise parameters
pressure_noise = 0
temp_noise = 0
accel_noise = 0
gyro_noise = 0
mag_noise = 0

# fixed angular velocities
roll_rate = 180 # deg/s
pitch_rate = 1
yaw_rate = 0

# current rocket state

position_E = 0
position_N = 0
altitude = 0

orientation_q0 = 0
orientation_q1 = 0
orientation_q2 = 0
orientation_q3 = 0

acceleration_x = 0
acceleration_y = 0
acceleration_z = 0

airspeed = 0
cur_mass = 100

drag = 0
gravity = 0

# environmental factors

temperature = 0
density = 1.225
accel_gravity = 9.81 

def init_rocket_state():
	orientation_q0 = np.cos(tower_angle * np.pi / 180 / 2)
	orientation_q1 = np.sin(tower_angle * np.pi / 180 / 2)
	orientation_q2 = 0
	orientation_q3 = 0
	cur_mass = init_mass

def time_update():
	drag = 1/2 * density * airspeed ** 2  * area * drag_coeff
	gravity = cur_mass * accel_gravity
	if t > burn_time:
		thrust = 0
	acceleration_z = (thrust - drag - GRAVITY)
    # update the state of the rocket
    # write to ground truth data file
    # generate sensor measurements
    # write to sensor data file

init_rocket_state()

while t < end_time:
    time_update()
    t += timestep
