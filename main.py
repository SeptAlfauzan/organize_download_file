import os
import pathlib
from os import walk

home = os.path.expanduser("~")
directory_name = ""
download_dir = home + "/Downloads/"
path = os.path.join(download_dir, directory_name)

def get_list_files(path):
    files = []#array of files name
    if os.path.isdir(path):
        for (dirpath, dirnames, filesname) in walk(path):
            files.extend(filesname)
    return files

def move_file(home_path, path, format_file, file_name):
    dir_name = file_format + ' files'
    new_folder_path = home_path + dir_name
    is_dir = os.path.isdir(new_folder_path)
# is_directory = os.path.isdir(path)
    if is_dir == False:
        os.mkdir(new_folder_path)
        print("created new folder! " + new_folder_path)
    
    try:
        pathlib.Path(path).rename(new_folder_path + "/" +file_name)
        print('file moved successfully!')
    except Exception as error:
        print(error)

# get all list files
def remove_file(path):

    file_to_rem = pathlib.Path(path)
    file_to_rem.unlink()
    print('success remove file ' + path)

files = get_list_files(path)#array of files list

for f in files:
    file_path = path + f
    file_format = pathlib.Path(file_path).suffix

    if file_format == '.crdownload':#remove file when the format is .crdownload
        remove_file(file_path)
    else:
        file_format = file_format.replace('.', '')
        move_file(download_dir, file_path, file_format, f)
    