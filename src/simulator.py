import numpy as np

timestep = 0.01
end_time = 100
t = 0

# rocket parameters
mass = 100
thrust = 1000
burn_time = 10

# launch site parameters
tower_angle = 90
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

airspeed = 0

def init_rocket_state():
    # find the initial state of the rocket
    pass

def time_update():
    # update the state of the rocket
    # write to ground truth data file
    # generate sensor measurements
    # write to sensor data file
    pass

init_rocket_state()

while t < end_time:
    time_update()
    t += timestep