import json
import os
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from common import setup_pyplot

setup_pyplot()

with open("parameters.json") as par_file:
    pars = json.load(par_file)

N = pars["N"]

data_root = Path("data/processed")

fig, axs = plt.subplots(nrows=3, sharex=True)

for idx, n in enumerate([1, 4, 9]):
    omega, eps_max = np.loadtxt(
        data_root / f"eps_vs_omega_run_k=7_{n=}_1702462220"
    ).T
    axs[idx].plot(omega, eps_max, "-+")
    axs[idx].grid(True, axis="x")
    axs[idx].grid(False, axis="y")

    axs[idx].set_title(f"${n=}$")

    plt.xticks(
        ticks=omega[::2],
        labels=[f"${tick + 1}\\pi^2/2$" for tick in range(len(omega))[::2]],
        rotation="vertical",
    )

fig.suptitle(r"$\kappa=7$")
fig.supxlabel(r"$\omega$")
fig.supylabel(r"${\epsilon}_{\max}$")

plt.tight_layout()
plt.savefig("figures/resonance.pdf")
plt.show()
