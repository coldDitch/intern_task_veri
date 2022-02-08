import numpy as np
import pandas as pd
from stan_utility import glucose_model_generate
from metrics import model_acc, pred_from_samples

def main():
    filename = 'glucose_data_1.csv'
    X = pd.read_csv('data/' + filename, header=None).values
    fit_pred_train = glucose_model_generate('glucose_score_gq', X)
    X_pred = pred_from_samples(fit_pred_train)
    print(X_pred)
    np.savetxt('predictions/prediction_scores.csv', X_pred, delimiter=',')

if __name__ == '__main__':
    main()