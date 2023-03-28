# 6.15
"""
Note the <file name> may not coincide with your code.
my spelling is also amazing, I know.
"""
import numpy as np
import matplotlib.pyplot as plt
from numpy import exp, sin, pi
from matplotlib.animation import FuncAnimation

dist = np.linspace(-6, 6, 250)
t = np.linspace(-1, 1, 250)
ampletude = exp(-(dist - 3 * t) ** 2) * sin(3 * pi * ((dist - 3 * t)))

fig = plt.figure()
lines = plt.plot(dist, t)
plt.axis([dist[0], dist[-1], -1, 1])
plt.xlabel('Linear Distance')
plt.ylabel('Ampletude')


def frame(stills):
    t = stills
    y = exp(-(dist - 3 * t) ** 2) * sin(3 * pi * ((dist - 3 * t)))
    lines[0].set_ydata(y)
    return lines


anim = FuncAnimation(fig, frame, frames=t * 5, interval=50)
anim.save("wave.gif", "imagemagick")


def wave_packet(x, t):
    return np.exp(-(x - 3 * t) ** 2) * np.sin(3 * np.pi * (x - t))


xlist = np.linspace(-4, 4, 1001)
tlist = (-0.85, 0, 0.85)
for t in (-0.85, 0, 0.85):
    ylist = wave_packet(xlist, t)
    plt.plot(xlist, ylist)
    plt.xlabel('x')
    plt.ylabel('Amplitude')
    plt.title('One dimensional wave packet: t = %.2f s' % t)
    plt.savefig('wavepacket_report-t=%.2f.png' % t)
    plt.close()

outfile = open('wave_packet.html', 'w')
outfile.write('<html>\n<body bgcolor="#FFFAFA" style="margin: 20px 200px">\n')
outfile.write('<h1 style="color: #053061; font: 60pt Helvetica Neue; font-weight:100; text-align:center">\
Wavepacket Program Report\
</h1>\n')
outfile.write('<p style="color: #333; font: 20pt Helvetica Neue; font-weight:100;" > \
This report details the output of a wave_packet plotting function: wave_packet(x, t).\
The function is demonstrated in the following example: \
</p >\n')
outfile.write('<pre style="color: #333; font-size: 12pt; margin-left: 100px">\n')
infile = open('plot_wavepacket.py', 'r')
counter = 1
for line in infile:
    outfile.write('%-4s %s \n' % (str(counter), line))
    counter += 1
outfile.write('</pre>\n')
outfile.write('<hr>')
outfile.write('<h2 style="color: #053061; font: 50pt Helvetica Neue; font-weight:100; text-align:center">\
Example plots\
</h2>\n')
for t in tlist:
    outfile.write(
        '<div align="middle" style="margin-top: 20px"><img align="middle" src="wavepacket_report-t=%.2f.png"/></div>\n' % t)
outfile.write('<h2 style="color: #053061; font: 50pt Helvetica Neue; font-weight:100; text-align:center">\
Animated Gif\
</h2>\n')
outfile.write('<hr>')
outfile.write('<div align="middle" style="margin-top: 20px"><img align="middle" src="wavepacket_report.gif"/></div>\n')
outfile.write('</html>\n</body>\n')
