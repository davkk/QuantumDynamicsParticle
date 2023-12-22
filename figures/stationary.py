import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from common import setup_pyplot

setup_pyplot()

with open("parameters.json") as par_file:
    pars = json.load(par_file)

N = pars["N"]

data_root = Path("data/raw")

fig, axs = plt.subplots(nrows=3, ncols=3, sharex=True)

for idx, n in enumerate([1, 4, 9]):
    tau, norm, x, eps = np.loadtxt(data_root / f"run_k=0_{n=}_1702464508/{n}").T

    axs[0][idx].set_title(f"${n=}$")

    axs[0][idx].plot(tau, norm, ",")
    axs[0][idx].set_ylim(0.99, 1.01)

    axs[1][idx].plot(tau, x, linewidth=0.5)
    axs[1][idx].set_ylim(0.49, 0.51)

    axs[2][idx].plot(tau, eps, linewidth=0.5)

    axs[2][0].set_xlabel(r"$\tau$")
    axs[2][1].set_xlabel(r"$\tau$")
    axs[2][2].set_xlabel(r"$\tau$")
    axs[0][0].set_ylabel(r"$\mathcal{N}$")
    axs[1][0].set_ylabel(r"$x$")
    axs[2][0].set_ylabel(r"$\epsilon$")

    axs[idx][0].set_xlim(0, 5)
    axs[idx][1].set_xlim(0, 1)
    axs[idx][2].set_xlim(0, 0.75)

fig.suptitle(r"$\omega=0$, $\kappa=0$")

plt.tight_layout()
plt.savefig("stationary.pdf")
plt.show()
