import numpy as np
import pandas as pd
import impyute
from sys import argv

def main(file_name):
    '''
    Creates data with nulls based off the input file_name. Generates csv's
    of nulled data with various imputations and a csv of rmse for each method

    Input:
        file_name: (str) A directory path to the data file to be used
    '''
    df = pd.read_csv(file_name)
    df = df[df['Unit Number'] == 2]
    null_df = mute_data(df)
    impute_metrics(df, null_df, file_name[:-4])


def impute_metrics(df, null_df, file_name):
    '''
    Generates csv's with imputed data and a csv with rmse for each method

    Input:
        df: (DataFrame) Pandas DataFrame with no nulls
        null_df: (DataFrame) Same as df except with nulls
        file_name: (str) Base name of the files to be generated
    '''
    metrics = {}
    imputes = [impyute.imputation.cs.mice, impyute.imputation.cs.mean,
               impyute.imputation.cs.fast_knn, impyute.imputation.ts.moving_window]
    for impute in imputes:
        df_imputed = impute(null_df)
        df.to_csv(file_name + '_' + impute.__name__ + '.csv')
        metrics[impute.__name__] = [total_rmse(df, df_imputed)]
    pd.DataFrame.from_dict(metrics).to_csv(file_name + '_results' + '.csv')


def total_rmse(df, df_imputed):
    return sum(sum((np.array(df_imputed) - np.array(df))**2))


def mute_data(df):
    data_dict = {}
    subjects = df['Unit Number'].unique()
    for un in subjects:
        partition = df[df['Unit Number']==un]
        #for c in range(len(partition)):
        null_col_ix = sorted(np.random.randint(5,26,size=np.random.randint(21)))
        mute_start = np.random.randint(50,100)
        mute_range = np.random.randint(5,25)
        mute_end = mute_start + mute_range
        partition.iloc[mute_start:mute_end,null_col_ix] = np.nan
        if mute_end <100:
            mute_start2 = np.random.randint(mute_end,mute_end+50)
            mute_range2 = np.random.randint(10,50)
            mute_end2 = mute_start2+mute_range2
            partition.iloc[mute_start2:mute_end2,null_col_ix] = np.nan
        if partition.Time.max() >250:
            mute_start3 = np.random.randint(np.random.randint(200,250),500)
            mute_range3 = np.random.randint(25,50)
            mute_end3 = mute_start3 + mute_range3
            partition.iloc[mute_start3:mute_start3+mute_range3,null_col_ix] = np.nan
        data_dict[un] = partition
    muted_df = pd.concat([data_dict[un] for un in subjects ])
    return muted_df


def get_metrix(muted_df):
    sm_percents = {}
    for x in muted_df.columns[muted_df.columns.str.contains('SM')]:
        norm_val_counts = muted_df.groupby(['Unit Number'])[x].value_counts(normalize=True,
                                                                dropna=False)
        null_percents = []
        for un in subjects:
            if np.nan not in norm_val_counts[un].index:
                target_val=0
            else:
                target_val = round(norm_val_counts[un][np.nan],3)
            null_percents.append(target_val)
        sm_percents[x] = null_percents
        return pd.DataFrame(sm_percents)


def time_series(muted_df):
    sm_percents_over_time = {}
    for x in muted_df.columns[muted_df.columns.str.contains('SM')]:
        norm_val_counts = muted_df.groupby(['Time'])[x].value_counts(normalize=True,
                                                                dropna=False)
        null_percents = []


        for t in sorted(muted_df.Time.dropna().unique()):
            if np.nan not in norm_val_counts[t].index:
                target_val=0
            else:
                target_val = round(norm_val_counts[t][np.nan],3)
            null_percents.append(target_val)
        sm_percents_over_time[x] = null_percents
        time_df = pd.DataFrame(sm_percents_over_time)
        time_df.plot(figsize=(15,15))

if __name__ == '__main__':
    main(argv[1])
