import vpython as vp
"""
from vpython import box, vector, color, sphere, cylinder
box(pos=vector(0, 0, 1), size=vector(0.3, 0.4, 0.5), color=color.blue)
sphere(pos=vector(1, 2, 1), radius=0.5, color=color.red)
cylinder(pos=vector(1, 0, 1), radius=0.5, color=color.green)
"""
"""
import vpython as vp

initial_position = vp.vector(-1., 0., 0.)
initial_velocity = vp.vector(1., 0., 0.)
ball = vp.sphere(pos=initial_position, radius=0.1, color=vp.color.red, make_trail=True)

animation_time_step = 0.1  # seconds
rate_of_animation = 1/animation_time_step
time_step = 0.05
stop_time = 10.

time = 0.
while time < stop_time:
    vp.rate(rate_of_animation)
    x = initial_position.x + initial_velocity.x * time
    y = initial_position.y + initial_velocity.y * time
    z = initial_position.z + initial_velocity.z * time
    ball.pos = vp.vector(x, y, z)
    time += time_step
"""

# import vpython as vp

initial_position = vp.vector(-10., 0., 0.)
initial_velocity = vp.vector(25., 0., 0.)
ball = vp.sphere(pos=initial_position, radius=0.5, color=vp.color.blue, make_trail=True)

wall_center = vp.vector(0., 0., 0.)
wall_dimensions = vp.vector(0.25, 10., 10.)
wall = vp.box(pos=wall_center, size=wall_dimensions, color=vp.color.red)

animation_time_step = 0.01  # seconds
rate_of_animation = 1/animation_time_step
time_step = 0.005
stop_time = 1.

time = 0.
ball_velocity = initial_velocity
while time < stop_time:
    vp.rate(rate_of_animation)
    if ball.pos.x > wall.pos.x:
        ball_velocity.x = -ball_velocity.x  # reverse ball velocity
    ball.pos.x += ball_velocity.x * time_step
    ball.pos.y += ball_velocity.y * time_step
    ball.pos.z += ball_velocity.z * time_step
    time += time_step
