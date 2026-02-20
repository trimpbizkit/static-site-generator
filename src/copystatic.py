import os
import shutil

from logger_singleton import LoggerSingleton as logger

def copy_files_recursive(source_dir_path, dest_dir_path):
    '''
    Copy all files and subdirectories, nested files, etc.
    
    :param source: string representing directory to copy from
    :param dest: string representing directory to copy to
    '''
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        logger.info(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)
