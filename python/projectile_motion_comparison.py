import vpython as vp

earth_center = vp.vector(50., 50., 0.)
earth_dimensions = vp.vector(50., 50., 0.)
earth = vp.box(
    pos=earth_center,
    size=earth_dimensions,
    color=vp.color.green
)

Earth = vp.text(text="EARTH",
                pos=vp.vector(50, 50, -20),
                align='center',
                height=15,
                color=vp.color.green,
                axis=vp.vector(1, 1, 0),
                up=vp.vector(0, 0, 1)
                )

mars_center = vp.vector(0., 0., 0.)
mars_dimensions = vp.vector(50., 50., 0.)
mars = vp.box(
    pos=mars_center,
    size=mars_dimensions,
    color=vp.color.red
)

Mars = vp.text(text="MARS",
               pos=vp.vector(-0, -0, -20),
               align='center',
               height=15,
               color=vp.color.red,
               axis=vp.vector(1, 1, 0),
               up=vp.vector(0, 0, 1)
               )

moon_center = vp.vector(-50., -50., 0.)
moon_dimensions = vp.vector(50., 50., 0.)
moon = vp.box(
    pos=moon_center,
    size=moon_dimensions,
    color=vp.color.gray(.8)
)

Moon = vp.text(text="MOON",
               pos=vp.vector(-50, -50, -20),
               align='center',
               height=15,
               color=vp.color.gray(.8),
               axis=vp.vector(1, 1, 0),
               up=vp.vector(0, 0, 1)
               )

initial_position_earth = vp.vector(25., 25., 0.1)
initial_velocity_earth = vp.vector(10., 10., 10.)
grav_earth = -9.8
ball_earth = vp.sphere(
    pos=initial_position_earth,
    radius=1.,
    color=vp.color.blue,
    make_trail=True
)

initial_position_mars = vp.vector(-25., -25., 0.1)
initial_velocity_mars = vp.vector(10., 10., 10.)
grav_mars = -3.7
ball_mars = vp.sphere(
    pos=initial_position_mars,
    radius=1.,
    color=vp.color.yellow,
    make_trail=True
)

initial_position_moon = vp.vector(-75., -75., 0.1)
initial_velocity_moon = vp.vector(10., 10., 10.)
grav_moon = -1.6
ball_moon = vp.sphere(
    pos=initial_position_moon,
    radius=1.,
    color=vp.color.white,
    make_trail=True
)

animation_time_step = 0.01  # seconds
rate_of_animation = 1/animation_time_step
time_step = 0.005
stop_time = 2.

time = 0.
ball_velocity_earth = initial_velocity_earth
z_earth = initial_velocity_earth.z
while ball_earth.pos.z > 0:
    vp.rate(rate_of_animation)
    ball_velocity_earth.z = z_earth + grav_earth*time
    if ball_earth.pos.z <= 0:
        ball_velocity_earth.x = 0
        ball_velocity_earth.y = 0
        ball_velocity_earth.z = 0

    ball_earth.pos.x += ball_velocity_earth.x * time_step
    ball_earth.pos.y += ball_velocity_earth.y * time_step
    ball_earth.pos.z += ball_velocity_earth.z * time_step

    time += time_step

time = 0
ball_velocity_mars = initial_velocity_mars
z_mars = initial_velocity_mars.z
while ball_mars.pos.z > 0:
    vp.rate(rate_of_animation)
    ball_velocity_mars.z = z_mars + grav_mars*time
    if ball_mars.pos.z <= 0:
        ball_velocity_mars.x = 0
        ball_velocity_mars.y = 0
        ball_velocity_mars.z = 0

    ball_mars.pos.x += ball_velocity_mars.x * time_step
    ball_mars.pos.y += ball_velocity_mars.y * time_step
    ball_mars.pos.z += ball_velocity_mars.z * time_step

    time += time_step

time = 0
ball_velocity_moon = initial_velocity_moon
z_moon = initial_velocity_moon.z
while ball_moon.pos.z > 0:
    vp.rate(rate_of_animation)
    ball_velocity_moon.z = z_moon + grav_moon*time
    if ball_moon.pos.z <= 0:
        ball_velocity_moon.x = 0
        ball_velocity_moon.y = 0
        ball_velocity_moon.z = 0

    ball_moon.pos.x += ball_velocity_moon.x * time_step
    ball_moon.pos.y += ball_velocity_moon.y * time_step
    ball_moon.pos.z += ball_velocity_moon.z * time_step

    time += time_step
