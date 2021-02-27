import numpy as np

def get_dataset():
    np.random.seed(1)
    X = np.arange(0, 45).astype(int)
    X = X.reshape(X.shape[0], 1)
    Y = (1.1**X) + 1
    Y += np.random.randn(X.shape[0], X.shape[1]).astype(int)
    Y = [np.sum(Y[:i]) for i in range(len(Y))]
    return list(X), list(np.abs(Y))