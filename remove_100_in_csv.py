import os.path

import pandas as pd


def change_100_and_rename(path):
    # reading the csv file
    df = pd.read_csv(path)
    col_num = len(df.index)
    #updating the column value/data
    for i in range(0, col_num):
        df.loc[i, '100%'] = '0'

    # writing into the file
    df.to_csv(path, index=False)
    old_name = os.path.basename(path).split('.csv')[0]
    print("file "+old_name+" updated!")
    new_name = old_name+"_update.csv"
    new_full_name = os.path.join(os.path.dirname(path), new_name)
    os.rename(path, new_full_name)
    return new_name

