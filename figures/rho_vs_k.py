import json
import os
from pathlib import Path

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

with open("parameters.json") as par_file:
    pars = json.load(par_file)

N = pars["N"]
# data_root = Path("data/raw/run_1701859364/")
data_root = Path("data/raw/run_1701859994/")

omegas = [file for file in os.listdir(data_root) if "err" in file]

_, ks, rhos = np.loadtxt(data_root / omegas[-1]).T


def gen_frames():
    start = 0
    while start < len(rhos):
        yield [rho for rho in rhos[start : start + N]]
        start += N


fig, ax = plt.subplots()

frames = gen_frames()

frame0 = next(frames)
(line,) = ax.plot(
    ks[:N],
    frame0
)


def animate(_):
    frame = next(frames)
    line.set_ydata(frame)  # update the data.
    return (line,)


ani = animation.FuncAnimation(
    fig, animate, frames=len(rhos // N), blit=True, save_count=50, interval=1
)

plt.show()
