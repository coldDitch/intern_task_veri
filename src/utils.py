import pandas as pd
import numpy as np

def new_dataset(gluc, scores):
    X = pd.read_csv('data/'+gluc, header=None).values
    y = pd.read_csv('data/'+scores, header=None).values
    return X, y.ravel()

def combined_data():
    X1, y1 = new_dataset('glucose_data_1.csv', 'scores_1.csv')
    X2, y2 = new_dataset('glucose_data_2.csv', 'scores_2.csv')
    X = np.concatenate([X1, X2])
    y = np.concatenate([y1, y2])
    return (X, y)