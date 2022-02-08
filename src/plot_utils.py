import numpy as np
import matplotlib.pyplot as plt
import arviz as az

def plot_glucose_ts(arr, color='b', alpha=1):
    t = np.arange(arr.shape[0])
    for i in range(arr.shape[1]):
        plt.plot(t, arr[:,i], c=color, alpha=alpha)
        
def plot_hist(arr, alpha=0.3, color='b'):
    plt.hist(arr, alpha=alpha, color=color, bins=np.arange(1,10))

def plot_post(fit, var_name):
    """Creates density plots for one dimensional posterior parameters 
    Args:
        fit CmdStanMCMC: the model object fit
    """
    az.plot_density(
        fit,
        var_names=var_name,
        shade=0.1,
        hdi_prob=1)
    
def plot_samples_grid(fit, var_name):
    """Creates a pairplot of posterior samples for one dimensional posterior parameters
    Args:
        fit CmdStanMCMC: the fitted model object
    """
    az.plot_pair(
        fit, var_names=var_name, divergences=True
    )