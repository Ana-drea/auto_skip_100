import os.path
import math
import pandas as pd


def return_lan_and_hours(path):
    df = pd.read_csv(path)
    # row_num = len(df.index)
    # # updating the column value/data
    # for i in range(0, row_num):
    #     df.loc[i, '100%'] = '0'
    row_num = len(df.index)
    lan = df["Target Locale"][0]
    without_ICE = df["Total"][row_num - 1] - df["ICE Match"][row_num - 1]
    if "Japanese" in lan or "Chinese" in lan or "Korean" in lan:
        hour = without_ICE / 850
    else:
        hour = without_ICE / 1000
    hour_final = math.ceil(hour / 0.25) * 0.25
    result = [lan,hour_final]
    return result


def change_100_and_rename(path):
    # reading the csv file
    df = pd.read_csv(path)
    row_num = len(df.index)
    # updating the column value/data
    for i in range(0, row_num):
        df.loc[i, '100%'] = '0'

    # writing into the file
    df.to_csv(path, index=False)
    old_name = os.path.basename(path).split('.csv')[0]
    print("file " + old_name + " updated!")
    new_name = old_name + "_update.csv"
    new_full_name = os.path.join(os.path.dirname(path), new_name)
    os.rename(path, new_full_name)
    return new_name
