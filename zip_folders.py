import os
import shutil
import zipfile
from empty_directory import empty_directory

# 创建zip压缩包
f = r"C:\test"
if not os.path.exists(f):
    os.mkdir()
else:
    empty_directory(f)

zip_file = zipfile.ZipFile(
    r'C:\test\test.zip', 'w', compression=zipfile.ZIP_DEFLATED
)


def zip_multi(p, extra =""):
    for subf in os.listdir(p):
        p2 = os.path.join(p, subf)
        p1 = os.path.join(extra, subf)
        zip_file.write(p2, p1, zipfile.ZIP_STORED)
        if os.path.isdir(p2):
            zip_multi(p2,p1)



def zip_main(path):
    zip_name = os.path.basename(path) + ".zip"
    zip_multi(path)
    zip_file.close()
    new_name = os.path.join(path, zip_name)
    shutil.move(r'C:\test\test.zip', new_name)
    os.startfile(path)
