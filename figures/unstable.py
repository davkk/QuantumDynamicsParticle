import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from common import setup_pyplot

setup_pyplot()

with open("parameters.json") as par_file:
    pars = json.load(par_file)

N = pars["N"]

data_root = Path("data/processed")

fig, axs = plt.subplots(ncols=3)
dts = [0.01, 0.001, 0.0005]

for idx, dt in enumerate(dts):
    tau, _, _, eps = np.loadtxt(
        data_root / f"unstable_run_k=0_n=1_{dt=}_1703255572"
    ).T

    axs[idx].set_title(f"${dt=}$")

    axs[idx].plot(tau, eps, "-+", linewidth=0.5)

    axs[idx].set_xlabel(r"$\tau$")
    axs[idx].set_ylabel(r"$\epsilon$")

fig.suptitle(r"$\omega=0$, $\kappa=0$")

plt.tight_layout()
plt.savefig("figures/unstable.pdf")
plt.show()
