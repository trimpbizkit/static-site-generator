from textnode import TextNode, TextType
import shutil
import os

import logging
logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename='info.log', level=logging.INFO)
    logger.info('Started')
    source = "./static"
    dest = "./public"
    logger.info(f"Copying from {source} to {dest}")
    copy_source_to_dest(source, dest)
    logger.info('Finished')

def copy_source_to_dest(source, dest):
    '''
    First, delete all the contents of the destination directory to ensure that the copy is clean.
    Then, copy all files and subdirectories, nested files, etc.
    
    :param source: string representing directory to copy from
    :param dest: string representing directory to copy to
    '''
    shutil.rmtree(dest, ignore_errors=True)
    if not os.path.exists(dest):
        os.mkdir(dest)
    dir_contents = os.listdir(source)
    for content in dir_contents:
        source_path = os.path.join(source, content)
        dest_path = os.path.join(dest, content)
        if os.path.isfile(source_path):
            result = shutil.copy(source_path, dest_path)
            logger.info(f"COPIED {result}")
        else:
            os.mkdir(dest_path)
            copy_source_to_dest(source_path, dest_path)

if __name__ == "__main__":
    main()
