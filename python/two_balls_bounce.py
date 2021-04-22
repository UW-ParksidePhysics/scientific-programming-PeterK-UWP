import vpython as vp

initial_position = vp.vector(-10., 5., 0.)
initial_velocity = vp.vector(10., -10., 0.)
ball = vp.sphere(
    pos=initial_position,
    radius=0.5,
    color=vp.color.white,
    make_trail=True
)

initial_position2 = vp.vector(-10., -5., 0.)
initial_velocity2 = vp.vector(10., 10., 0.)
ball2 = vp.sphere(
    pos=initial_position2,
    radius=0.5,
    color=vp.color.cyan,
    make_trail=True
)

wall_center = vp.vector(0., 0., 0.)
wall_dimensions = vp.vector(0.25, 10., 10.)
wall = vp.box(pos=wall_center, size=wall_dimensions, color=vp.color.red)

animation_time_step = 0.01  # seconds
rate_of_animation = 1/animation_time_step
time_step = 0.05
stop_time = 5.

time = 0.
ball_velocity = initial_velocity
ball_velocity2 = initial_velocity2
while time < stop_time:
    vp.rate(rate_of_animation)
    if ball.pos.x > wall.pos.x - 0.75:
        ball_velocity.x = -ball_velocity.x
        ball_velocity2.x = -ball_velocity2.x  # reverse ball velocity

    ball.pos.x += ball_velocity.x * time_step
    ball.pos.y += ball_velocity.y * time_step
    ball.pos.z += ball_velocity.z * time_step
    ball2.pos.x += ball_velocity2.x * time_step
    ball2.pos.y += ball_velocity2.y * time_step
    ball2.pos.z += ball_velocity2.z * time_step

    time += time_step
