# Software developer task for veri

## Getting started

- Create new python environment or use existing one
- Activate environment and install requirements by
``` pip install -r requirements.txt ```
- Install commandline version of stan
``` install_cmdstan ```

## Part 1: glucose data analysis
Everything for this project is inside glucose_data_analysis.ipynb notebook.

## Part 2: meal scoring tool
My aim was to develop scoring tool that is sufficiently simple, but which has sufficiently low absolute error from the given scoring data.

- meal_scoring_tool.ipynb shows the modelling workflow
- models/glucose_score.stan implements the ordered categorical regression model, from few basic statistics
- train.py is simple python executable for training the model
- run.py is simple python executable for generating predictions for new .csv datasets
