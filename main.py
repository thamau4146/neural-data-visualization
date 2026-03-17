import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Simulated neural signal
t = np.linspace(0, 1, 500)
freq = 5
signal = np.sin(2 * np.pi * freq * t)

# Plot setup
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)
line, = plt.plot(t, signal)
ax.set_title("Neural Signal Visualization")

# Slider for frequency
axfreq = plt.axes([0.2, 0.1, 0.65, 0.03])
slider = Slider(axfreq, 'Frequency', 1, 20, valinit=freq)

def update(val):
    f = slider.val
    new_signal = np.sin(2 * np.pi * f * t)
    line.set_ydata(new_signal)
    fig.canvas.draw_idle()

slider.on_changed(update)

plt.show()
