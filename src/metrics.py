import cmdstanpy
import numpy as np
from sklearn.metrics import accuracy_score

def pred_from_samples(fit, var='score_draws'):
    samples = fit.stan_variable(var)
    pred_shape = samples.shape[1]
    uniques = [np.unique(samples[:,i], return_counts=True) for i in range(pred_shape)]
    scores = [el[0][np.argmax(el[1])] for el in uniques]
    return np.array(scores)

def abs_acc_score(y_pred, y_true):
    return np.mean(np.abs(y_pred-y_true))

def model_acc(fit, y, var='score_draws'):
    ystar = pred_from_samples(fit, var=var)
    return accuracy_score(ystar, y), abs_acc_score(ystar, y)