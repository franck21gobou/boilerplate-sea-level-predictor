import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    df = pd.read_csv("epa-sea-level.csv")

    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    res_all = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_ext = np.arange(1880, 2051)
    plt.plot(
        years_ext,
        res_all.intercept + res_all.slope * years_ext,
    )

    df_2000 = df[df["Year"] >= 2000]
    res_2000 = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
    years_2000 = np.arange(2000, 2051)
    plt.plot(
        years_2000,
        res_2000.intercept + res_2000.slope * years_2000,
    )

    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    plt.savefig("sea_level_plot.png")
    return plt.gca()
