import os
import zipfile



def unzip_file(zip_src, dst_dir):
    if zipfile.is_zipfile(zip_src):
        fz = zipfile.ZipFile(zip_src, 'r')
        for file in fz.namelist():
            fz.extract(file, dst_dir)
    else:
        print('This is not zip')


def unzipfolders(zip_path):

    zip_name = os.path.basename(zip_path).split(".zip")[0]
    parent_folder = os.path.dirname(zip_path)
    unzipped_folder_path = os.path.join(parent_folder, zip_name)
    print("unzipping files to folder: " + unzipped_folder_path)
    unzip_file(zip_path, unzipped_folder_path)
    os.remove(zip_path)
    return unzipped_folder_path

