import os.path
import shutil

from playwright.sync_api import sync_playwright, Page, expect
from empty_directory import empty_directory
from unzipfolders import unzipfolders
from remove_100_in_csv import change_100_and_rename, return_lan_and_hours
from zip_folders import zip_main
import pandas as pd

page = sync_playwright().start()
default_download_path = r"C:\Skip_100_MTPE"

def get_atta_path(path):
    if not path.endswith("/attachments"):
        list = path.rsplit("/", 1)
        atta_path = list[0] + "/attachments"
        return atta_path
    else:
        return path

def download_atta(path):
    browser = page.chromium.launch(headless=False)
    p = browser.new_page()

    p.goto(path,wait_until="networkidle")
    # Start waiting for the download
    with p.expect_download() as download_info:
        # click "download only folders"
        p.locator('//*[@id="jobAttachmentsTable"]/div[1]/div[3]/button[2]').click()
    download = download_info.value
    # Wait for the download process to complete
    # Save downloaded empty folder
    download.save_as(os.path.join(default_download_path,"1.zip"))


    with p.expect_download() as download_info:
        # toggle "Internal"
        p.locator('//*[@id="jobAttachmentsTable"]/div[2]/div/div[2]/div[2]/div[2]').click()
        # toggle "Analysis"
        p.locator('//*[@id="jobAttachmentsTable"]/div[2]/div/div[2]/div[3]/div[2]/div[1]/div[2]').click()
        # select "MTPE Translation"
        p.locator(
            '//*[@id="jobAttachmentsTable"]/div[2]/div/div[2]/div[3]/div[2]/div[2]/div[2]/div[3]/div[1]/input').check()
        # select "Translation"
        # p.locator(
        #     '//*[@id="jobAttachmentsTable"]/div[2]/div/div[2]/div[3]/div[2]/div[2]/div[2]/div[16]/div[1]/input').check()
        #click "download"
        p.locator('//*[@id="jobAttachmentsTable"]/div[1]/div[3]/button[1]').click()
    download = download_info.value
    download.save_as(os.path.join(default_download_path,"2.zip"))

    browser.close()

path = input("type in the project path:\n")
atta_p = get_atta_path(path)

if os.path.exists(default_download_path):
    empty_directory(default_download_path)

download_atta(atta_p)
unzipfolders(os.path.join(default_download_path,"1.zip"))
unzipfolders(os.path.join(default_download_path,"2.zip"))



# create a list to store the ARR hour financials
# translation_arr_data = []
MTPE_arr_data = []


# # change the csv files in folder 2, copy to empty Sym folder
# #translation_directory = C:\Skip_100_MTPE\2\Internal\Analysis\Translation
# translation_directory = os.path.join(default_download_path, "2", "Internal\Analysis\Translation")
# for lan_folder in os.listdir(translation_directory):
#     #lan_path = C:\Skip_100_MTPE\2\Internal\Analysis\Translation\cs-CZ
#     lan_path = os.path.join(translation_directory, lan_folder)
#     for csv_file in os.listdir(lan_path):
#         csv_path = os.path.join(lan_path, csv_file)
#         # get hour financial for each language, should look like "German (Germany)	1.5"
#         lan_and_hour = return_lan_and_hours(csv_path)
#         translation_arr_data.append(lan_and_hour)
#
#         # remove 100% match from csv and rename the csv files
#         new_csv_name = change_100_and_rename(csv_path)
#         temp = os.path.join("Internal\Analysis\Translation", lan_folder, new_csv_name)
#         # copy_src = C:\Skip_100_MTPE\1\Internal\Analysis\Translation\cs-CZ
#         copy_src = os.path.join(default_download_path,"2", temp)
#         # copy_tgt = C:\Skip_100_MTPE\2\Internal\Analysis\Translation\cs-CZ
#         copy_tgt = os.path.join(default_download_path,"1",  temp)
#         shutil.copyfile(copy_src, copy_tgt)



# change the csv files in folder 2, copy to empty Sym folder
#translation_directory = C:\Skip_100_MTPE\2\Internal\Analysis\Translation
translation_directory = os.path.join(default_download_path, "2", "Internal\Analysis\MTPE Translation")
for lan_folder in os.listdir(translation_directory):
    #lan_path = C:\Skip_100_MTPE\2\Internal\Analysis\Translation\cs-CZ
    lan_path = os.path.join(translation_directory, lan_folder)
    for csv_file in os.listdir(lan_path):
        csv_path = os.path.join(lan_path, csv_file)
        # get hour financial for each language, should look like "German (Germany)	1.5"
        lan_and_hour = return_lan_and_hours(csv_path)
        MTPE_arr_data.append(lan_and_hour)

        # remove 100% match from csv and rename the csv files
        new_csv_name = change_100_and_rename(csv_path)
        temp = os.path.join("Internal\Analysis\MTPE Translation", lan_folder, new_csv_name)
        # copy_src = C:\Skip_100_MTPE\1\Internal\Analysis\Translation\cs-CZ
        copy_src = os.path.join(default_download_path,"2", temp)
        # copy_tgt = C:\Skip_100_MTPE\2\Internal\Analysis\Translation\cs-CZ
        copy_tgt = os.path.join(default_download_path,"1",  temp)
        shutil.copyfile(copy_src, copy_tgt)


print("updated csv files moved to the empty folder")
zip_tgt = zip_main(os.path.join(default_download_path,"1"))

# p1 = os.path.join(default_download_path,"1","translation_hours.xlsx")
p2 = os.path.join(default_download_path,"1","MTPE_hours.xlsx")

# # f.close()
# # add the translation ARR data of all languages to the dataframe
# df1 = pd.DataFrame(translation_arr_data, columns=['Language', 'hours'])
# df1_sorted = df1.sort_values(by = "hours")
# #write the excel to excel
# df1_sorted.to_excel(p1)


# add the MTPE ARR data of all languages to the dataframe
df2 = pd.DataFrame(MTPE_arr_data, columns=['Language', 'hours'])
df2_sorted = df2.sort_values(by = "hours")
#write the excel to excel
df2_sorted.to_excel(p2)
print("All process done!")
print("You can now upload the zip file from " + zip_tgt)








