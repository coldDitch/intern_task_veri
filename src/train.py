from stan_utility import glucose_model_fit
from utils import combined_data

def main():
    X, y = combined_data()
    fit = glucose_model_fit('glucose_score', X, y)
    print(fit.diagnose())


if __name__ == '__main__':
    main()