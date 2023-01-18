import os.path
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from empty_directory import empty_directory




def go_to_Sym(sym_path):
    path = r"C:\Skip_100"
    if os.path.exists(path):
        empty_directory(path)
    else:
        os.mkdir(path)

    # 设置下载文件存放路径，这里要写绝对路径
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': r"C:\Skip_100"}
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', prefs)
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver_path = r'chromedriver.exe'
    wd = webdriver.Chrome(service=Service(driver_path), options=options)
    # go to Symfonie
    wd.get(sym_path)
    time.sleep(80)
    element = wd.find_element(by=By.XPATH, value='//*[@id="handoffTitleName"]')
    # get the name of the Sym job, which will also be the name of downloaded zip file
    project_name = element.text
    element = wd.find_element(by=By.XPATH, value='//*[@id="handoffAttachments"]')
    element.click()
    time.sleep(1)
    # click "download only folders"
    element = wd.find_element(by=By.XPATH, value='//*[@id="jobAttachmentsTable"]/div[1]/div[3]/button[2]')
    element.click()
    time.sleep(5)
    # download folders to put csv files
    element = wd.find_element(by=By.XPATH, value='//*[@id="jobAttachmentsTable"]/div[2]/div/div[2]/div[2]/div[2]')
    element.click()
    time.sleep(5)
    element = wd.find_element(by=By.XPATH,
                              value='//*[@id="jobAttachmentsTable"]/div[2]/div/div[2]/div[3]/div[2]/div[1]/div[2]')
    element.click()
    time.sleep(1)
    JS1 = 'document.querySelector("#jobAttachmentsTable > div.grid-scrollable > div > div.grid-body > div.grid-inner > div.grid-body > div.grid-inner > div.grid-header > div.grid-header-cell.grid-header-select-cell > input[type=checkbox]").click()'
    wd.execute_script(JS1)
    time.sleep(1)

    #click "download" button
    element = wd.find_element(by=By.XPATH, value='//*[@id="jobAttachmentsTable"]/div[1]/div[3]/button[1]')
    element.click()
    time.sleep(3)

    zip_name1 = project_name + ".zip"
    zip_name2 = project_name + " (1).zip"
    # return the downloaded zip path back to what called this python script
    filepath1 = os.path.join(path, zip_name1)
    filepath2 = os.path.join(path, zip_name2)
    ziplist = [filepath1, filepath2]
    for path in ziplist:
        print("downloaded zip files to: "+path)
    return ziplist
