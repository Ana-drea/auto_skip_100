import argparse
import os.path
import shutil

from download_from_sym import go_to_Sym
from unzipfolders import unzipfolders
from remove_100_in_csv import change_100_and_rename
from zip_folders import zip_main

parser = argparse.ArgumentParser()
parser.add_argument('--path', type=str, default=None)
args = parser.parse_args()
sym_url = args.path


ziplist = go_to_Sym(sym_url)
#path of the folder without ' (1)', also the empty folder
zippedfolderpath1 = unzipfolders(ziplist[0])
#path of the file with ' (1)', also the folder with csv
zippedfolderpath2 = unzipfolders(ziplist[1])



# zippedfolderpath1 = r"C:\Skip_100\Bonsai-20220617-Thanh-SK7-Bus-edu-form-202206131701"
# zippedfolderpath2 = r"C:\Skip_100\Bonsai-20220617-Thanh-SK7-Bus-edu-form-202206131701 (1)"
#change the csv files in folder 2, copy to empty Sym folder
translation_directory = os.path.join(zippedfolderpath2,"Internal\Analysis\Translation")
for lan_folder in os.listdir(translation_directory):
    lan_path = os.path.join(translation_directory, lan_folder)
    for csv_file in os.listdir(lan_path):
        csv_path = os.path.join(lan_path, csv_file)
        new_csv_name = change_100_and_rename(csv_path)
        temp = os.path.join("Internal\Analysis\Translation", lan_folder, new_csv_name)
        copy_src = os.path.join(zippedfolderpath2, temp)
        copy_tgt = os.path.join(zippedfolderpath1, temp)
        shutil.copyfile(copy_src,copy_tgt)
print("updated csv files moved to the empty folder")
zip_main(zippedfolderpath1)

