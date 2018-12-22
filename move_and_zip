import os
import shutil
from shutil import copyfile

old_dir_path = "/home/mohammad/Desktop/old/";
archive_dir_path = "/home/mohammad/Desktop/archive/";

def mod_date_generator(filename):
    dir_seprator = filename[4:13];
    return  dir_seprator;

def zip_func( new_dirname , dirname ):
       shutil.make_archive(archive_dir_path+ new_dirname +'_zip' ,   'zip'   , archive_dir_path+dirname)
       shutil.rmtree(archive_dir_path+dirname)

def new_dirname_func(archive_dir_path , dirname):
    i=1;
    dst_path = str(archive_dir_path + dirname) +str('_zip'+'.zip');
    while (os.path.isfile(dst_path) == True):
          new_dirname = dirname+'_'+str(i);
          dst_path = str(archive_dir_path + new_dirname) + str('_zip'+'.zip');
          i=i+1;
    return new_dirname;

##########################################################
                                      #az  hame file ha list migirad va anha ra  dar poosheye jadid(poshe archive) , move mikonad
                                      #dar pooshe haye mojaza(bar asase rooz) ,  move (va  dastebandi ham) anjam mishavad
ls = os.listdir(old_dir_path)
for filename in ls:
    dir_seprator = mod_date_generator(filename)
    if os.path.isdir(archive_dir_path + dir_seprator) == False:
       os.mkdir(archive_dir_path + dir_seprator)
    shutil.move(old_dir_path + filename   ,   archive_dir_path +'/'+ dir_seprator +'/'+filename)


                                     #faghat directory haye daroone poosheye archive ra filter mokonad
                                     #yani be file haye zipi ke az ghabl ijad shodand kar nadarad
                                     #chon faghat directory haye ijad shode bayad zip shavand
ls = os.listdir(archive_dir_path)
dirlist=[]
for dir in ls:
       if os.path.isdir(archive_dir_path+dir ) == True:
          dirlist.append(dir)
#print(dirlist);

                                     #check mikonad be ezaye har directory , file zipe hamnam vojod darad ya na?
                                     #agar vojod dasht ---- > farkhani functione new_path anjam mishavad
                                     #ta name  jadid baraye file zip  ijad gardad
for dirname in dirlist:
    if os.path.isfile(str(archive_dir_path+dirname) +str('_zip'+'.zip')) == False:
        zip_func(dirname , dirname)
    else:
        new_dirname = new_dirname_func(archive_dir_path , dirname)
        zip_func(new_dirname , dirname)
