import json
from pathlib import Path

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

with open("parameters.json") as par_file:
    pars = json.load(par_file)

N = pars["N"]
n = 9

time_to_save = [
    0.1,
    2.5,
    5.0
]

# data_root = Path("./data/raw/run_k=7_n=1_1702462220/14.804407.err")
# data_root = Path("./data/raw/run_k=7_n=1_1702462220/74.022033.err")
# data_root = Path("./data/raw/run_k=7_n=4_1702462220/44.413220.err")
data_root = Path("./data/raw/run_k=7_n=9_1702462220/93.761242.err")

# omegas = [file for file in os.listdir(data_root) if "err" in file]

time, ks, rhos = np.loadtxt(data_root).T


def gen_frames():
    idx = 0
    while idx < len(rhos):
        yield time[idx], [rho for rho in rhos[idx : idx + N]]
        idx += N


fig, ax = plt.subplots()

frames = gen_frames()

t0, rhos0 = next(frames)
(line,) = ax.plot(ks[:N], rhos0)

time_text = ax.text(0, np.max(rhos0), f"$t={t0}$", fontsize=15)

def animate(frame):
    time, rhos = frame
    line.set_ydata(rhos)  # update the data.
    time_text.set_text(time)

    if time in time_to_save:
        plt.savefig(f"figures/frame_{n=}_{time=}.png")

    return (line, time_text)


ani = animation.FuncAnimation(
    fig,
    animate,
    frames=frames,
    blit=True,
    save_count=len(rhos) // N,
    repeat_delay=200,
    interval=10,
)

# plt.title(r"$n=1$, $\kappa=7$, $\omega=3\pi^2/2$")

plt.xlabel("$k$")
plt.ylabel(r"$\rho$")
plt.ylim(0, 4)

# writer = animation.PillowWriter(fps=120)
# ani.save("figures/rho_vs_k.gif", writer=writer)

plt.show()
