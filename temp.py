import os.path
import shutil

from playwright.sync_api import sync_playwright, Page, expect
from empty_directory import empty_directory
from unzipfolders import unzipfolders
from remove_100_in_csv import change_100_and_rename, return_lan_and_hours
from zip_folders import zip_main
import pandas as pd
default_download_path = r"C:\Skip_100_MTPE"


df1 = pd.read_excel(r"C:\Skip_100_MTPE\1\MTPE_hours.xlsx")
df2 = pd.read_excel(r"C:\Skip_100_MTPE\1\translation_hours.xlsx")
df3 = pd.concat([df1,df2],axis=1)
df3.to_excel(r"C:\Skip_100_MTPE\1\sum.xlsx")




