import numpy as np
import pandas as pd
import impyute

def impute_metrics(df, null_df, file_name):
    metrics = {}
    imputes = [impyute.imputation.cs.mice, impyute.imputation.cs.mean,
               impyute.imputation.cs.fast_knn, impyute.imputation.ts.moving_window]
    for impute in imputes:
        df_imputed = impute(df_nulls)
        df.to_csv(file_name + '_' + impute.__name__)
        metrics[impute.__name__] = [total_rmse(df, df_imputed)]
    pd.DataFrame.from_dict(metrics).to_csv(file_name + '_results')

def total_rmse(df, df_imputed):
    return sum(sum((np.array(df_imputed) - np.array(df))**2))
