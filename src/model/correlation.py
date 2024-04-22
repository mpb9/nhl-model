import pandas as pd
import numpy as np


def corr_coef(data, x, target, desc=""):
    df_cor = pd.DataFrame()
    df_cor["target"] = pd.Series(target)
    df_cor["dataset"] = pd.Series(desc)
    y = data.target.copy()

    for col in x.columns:
        df_temp = df_cor.copy()
        df_temp[col] = data[col].copy().corr(y)
        df_cor = df_temp.copy()

    return df_cor


def covar(data, x, target, desc=""):
    df_cov = pd.DataFrame()
    df_cov["target"] = pd.Series(target)
    df_cov["dataset"] = pd.Series(desc)
    y = data.target.copy()

    for col in x.columns:
        df_temp = df_cov.copy()
        df_temp[col] = data[col].copy().cov(y)
        df_cov = df_temp.copy()

    return df_cov
