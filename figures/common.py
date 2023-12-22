from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def setup_pyplot():
    SMALL_SIZE = 14
    MEDIUM_SIZE = 16
    BIGGER_SIZE = 22

    plt.style.use("rose-pine-dawn")

    plt.rcParams["figure.figsize"] = (12, 7)
    # plt.rcParams["figure.dpi"] = 300
    plt.rcParams["font.family"] = "serif"
    plt.rcParams["mathtext.fontset"] = "stix"
    plt.rcParams["xtick.direction"] = "in"
    plt.rcParams["ytick.direction"] = "in"

    plt.rcParams["axes.formatter.limits"] = -3, 3
    plt.rcParams["axes.grid"] = True
    plt.rcParams["grid.color"] = "gainsboro"
    plt.rcParams["figure.facecolor"] = "white"
    plt.rcParams["axes.facecolor"] = "white"
    plt.rcParams["savefig.facecolor"] = "white"

    plt.rc("font", size=SMALL_SIZE)  # controls default text sizes
    plt.rc("axes", titlesize=SMALL_SIZE)  # fontsize of the axes title
    plt.rc("axes", labelsize=MEDIUM_SIZE)  # fontsize of the x and y labels
    plt.rc("xtick", labelsize=SMALL_SIZE)  # fontsize of the tick labels
    plt.rc("ytick", labelsize=SMALL_SIZE)  # fontsize of the tick labels
    plt.rc("legend", fontsize=SMALL_SIZE)  # legend fontsize
    plt.rc("figure", titlesize=BIGGER_SIZE)  # fontsize of the figure title

    colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
    markers = ["*", "1", "+", "2", ".", "3"]
    return colors, markers
