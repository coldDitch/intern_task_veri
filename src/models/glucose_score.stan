data {
  int n_score;
  int n_time;
  int n_sets;
  vector[n_time] time;
  vector[n_time] glucose[n_sets];
  int score[n_sets];
}
transformed data {
  real epsilon = 1e-6;
  vector[n_time-1] gluc_diff[n_sets];
  vector[n_time-2] gluc_diff2[n_sets];
  for (i in 1:n_sets) {
    for (j in 1:n_time-1) {
      gluc_diff[i][j] = glucose[i][j+1] - glucose[i][j];
    }
  }
  for (i in 1:n_sets) {
    for (j in 1:n_time-2) {
      gluc_diff2[i][j] = gluc_diff[i][j+1] - gluc_diff[i][j];
    }
  }
}
parameters {
  vector[4] beta;
  ordered[n_score-1] theta;
}
transformed parameters {
  vector[n_sets] eta;
  for (i in 1:n_sets) {
    eta[i] = beta[1] * sd(glucose[i])
    + beta[2] * (max(glucose[i])-glucose[i][1])
    + beta[3] * max(gluc_diff2[i])
    + beta[4] * mean(gluc_diff[i]);
  }
}
model {
  theta ~ normal(0, 10);
  beta ~ normal(0, 1);
  score ~ ordered_logistic(eta, theta);
}