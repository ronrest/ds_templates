import numpy as np
import matplotlib.pyplot as plt

def plot_label_frequencies(y, dataname="", logscale=False, saveto=None):
    """ Plots the frequency of each label in the dataset."""
    vals, freqs = np.array(np.unique(y, return_counts=True))
    freqs = freqs / float(len(y))

    fig, ax = plt.subplots(figsize=(6, 4))
    fig.suptitle("Distribution of Labels in {} dataset".format(dataname), fontsize=15)
    ax.bar(vals, freqs, alpha=0.5, color="#307EC7", edgecolor="b", align='center', width=0.8, lw=1)
    ax.set_xlabel("Labels")
    ax.set_ylabel("Frequency")
    if logscale:
        ax.set_yscale('log')
    if saveto is not None:
        fig.savefig(saveto)
    else:
        plt.show()
