import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def plot_density_distribution(x, saveto=None, logscale=False, dataname=""):
    """Plots a density distribution for visualizing how values are spread out"""
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.set_style('whitegrid')
    sns.kdeplot(x.flatten(), bw=0.5, ax=ax)

    fig.suptitle("Density disribution of {} dataset".format(dataname), fontsize=15)
    ax.set_xlabel("Values")
    ax.set_ylabel("Frequency")
    if logscale:
        ax.set_yscale('log')
    if saveto is not None:
        fig.savefig(saveto)
    else:
        plt.show()


# Usage
# plot_density_distribution(data["X_train"], logscale=True, dataname="train", saveto="/tmp/train_distribution.png")
