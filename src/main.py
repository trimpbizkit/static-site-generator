import os
import sys
import shutil

from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive
from logger_singleton import LoggerSingleton as logger

DIR_PATH_STATIC = "./static"
DIR_PATH_PUBLIC = "./public" # for local testing only
DIR_PATH_CONTENT = "./content"
DIR_PATH_DOCS = "./docs"
PATH_TEMPLATE = "./template.html"

def main():
    basepath = "/"
    dest_path = DIR_PATH_PUBLIC
    if len(sys.argv) > 1:
        # Production mode
        basepath = sys.argv[1]
        dest_path = DIR_PATH_DOCS

    if os.path.exists(dest_path):
        logger.info(f"Deleting {dest_path[2:]} directory...")
        shutil.rmtree(dest_path)

    logger.info(f"Copying static files to {dest_path[2:]} directory...")
    copy_files_recursive(DIR_PATH_STATIC, dest_path)
    
    logger.info("Generating content...")
    generate_pages_recursive(DIR_PATH_CONTENT, PATH_TEMPLATE, dest_path, basepath)

    logger.info("Finished")


if __name__ == "__main__":
    main()
