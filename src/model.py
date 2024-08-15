from sklearn.mixture import BayesianGaussianMixture
import os
import joblib
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm

def train_and_plot_gmm(data: pd.Series, n_components=2, max_iter=500, init_params="k-means++",
                       model_path: str = "model/gmm.pkl") -> BayesianGaussianMixture:
    """ Train a GMM model and plot the result

    Args:
        data (pd.Series): Data to train the GMM model
        n_components (int, optional): Number of Gaussians to fit. Defaults to 2.
        max_iter (int, optional): Maximum iterations. Defaults to 500.
        init_params (str, optional): Parameter initialization method. Defaults to "k-means++".

    Returns:
        BayesianGaussianMixture: Trained GMM model
    """
    # If GMM is already trained, load it from file
    if os.path.exists(model_path):
        print("Loading GMM from file")
        gmm = joblib.load(model_path)
    else:
        print("Training GMM")
        gmm = BayesianGaussianMixture(n_components=n_components, max_iter=max_iter, init_params=init_params)
        gmm.fit(data.values.reshape(-1,1))
        joblib.dump(gmm, model_path)
        print("GMM trained and saved to file")
    # print gmm parameters
    print("Mean: ", gmm.means_)
    print("Covariance: ", gmm.covariances_)
    print("Weights: ", gmm.weights_)

    # plot gmm
    x = np.linspace(0,10,1000)
    y = np.exp(gmm.score_samples(x.reshape(-1,1)))
    plt.figure(figsize=(12,9))
    sns.kdeplot(data, shade=True, color="r")
    plt.plot(x,y)
    return gmm

def train_linear(X, y) -> sm.regression.linear_model.RegressionResultsWrapper:
    """Train a log-linear model on the data

    Args:
        df (pd.DataFrame): DataFrame containing data

    Returns:
        sm.regression.linear_model.RegressionResultsWrapper: Trained model
    """
    # Create a new column for total score
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()
    # Print the model summary
    print(model.summary())
    return model
