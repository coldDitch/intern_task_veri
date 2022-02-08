import os
import cmdstanpy
import numpy as np

def glucose_model_fit(bayesname, glucose, score, progress='notebook'):
    bayespath = 'models/'+bayesname + '.stan'
    dat = {
        'n_score': 10,
        'n_time': 10,
        'n_sets': len(score),
        'time': np.arange(10),
        'glucose': glucose,
        'score': score.astype(int),
           }
    model = cmdstanpy.CmdStanModel(stan_file=bayespath, cpp_options={"STAN_THREADS": False})
    fit = model.sample(data=dat,
            seed=194838,
            chains=4,
            iter_warmup=1000,
            iter_sampling=1000,
            show_progress=progress,
            output_dir='logs'
            )
    fit.save_csvfiles("./posterior_data")
    return fit

def glucose_model_generate(bayesname, glucose):
    bayespath = 'models/'+bayesname + '.stan'
    dat = {
        'n_score': 10,
        'n_time': 10,
        'n_sets': glucose.shape[0],
        'time': np.arange(10),
        'glucose': glucose,
           }
    model = cmdstanpy.CmdStanModel(stan_file=bayespath)
    posterior_path = "posterior_data/"
    dirs = os.listdir(posterior_path)
    last_fit = sorted(dirs)[-4:]
    last_fit = [posterior_path + l for l in last_fit]
    fit = model.generate_quantities(data=dat,
            mcmc_sample=last_fit,
            gq_output_dir='logs')
    return fit

