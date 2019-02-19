import os
import datetime
import shutil
from shutil import copyfile
#from datetime import datetime
#from os.path  import getctime



old_dir_path = input("pls enter old directory path: for EXP:/home/mohammad/Desktop/old/ :")
new_dir_path = input("pls enter new directory path: for EXP:/home/mohammad/Desktop/new/ :")
backup_path  = input("pls enter new directory path: for EXP:/home/mohammad/Desktop/backup/ :");

def move_func(filename):
    shutil.move(old_dir_path+filename , backup_path+filename )

def mod_date(filename):
    p=filename[4:13];
    return p;

def zip_func(direname):
  shutil.make_archive(new_dir_path+direname +'_zip',   'zip'   , new_dir_path+direname)
  shutil.rmtree(new_dir_path+direname)

##########################################################3

ls = os.listdir(old_dir_path)
for filename in ls:
    move_func(filename)



ls = os.listdir(backup_path)
for filename in ls:
    dir_seprator = mod_date(filename)
    if os.path.isdir(new_dir_path + dir_seprator) == False:
        os.mkdir(new_dir_path + dir_seprator)
    copyfile(backup_path + filename   ,   new_dir_path +'/'+ dir_seprator +'/'+filename)


ls = os.listdir(new_dir_path)
for direname in ls:
    zip_func(direname)
