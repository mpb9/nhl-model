import numpy as np
import pandas as pd


def linear_coef(x, y, sample_size):
    if sample_size != len(y):
        return [np.nan, np.nan]

    mean_x = x.mean()
    mean_y = y.mean()

    # Calculate cross-deviation and deviation about x
    SS_xy = np.sum(y.copy() * x.copy()) - sample_size * mean_y * mean_x
    SS_xx = np.sum(x.copy() * x.copy()) - sample_size * mean_x * mean_x

    # Calculate regression coefficients
    b1 = SS_xy / SS_xx
    b0 = mean_y - b1 * mean_x

    return [b0, b1]


def linear_coefs_grouped(x, y_group, sample_size):
    B = pd.DataFrame(index=["b0", "b1"], columns=y_group.columns)
    if sample_size != len(y_group):
        return B
    for col in B:
        coefs = linear_coef(x, y_group[col].values, sample_size)
        B[col] = coefs
    return B
