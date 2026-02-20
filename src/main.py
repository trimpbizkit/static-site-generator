import os
import shutil

from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive
from logger_singleton import LoggerSingleton as logger

DIR_PATH_STATIC = "./static"
DIR_PATH_PUBLIC = "./public"
DIR_PATH_CONTENT = "./content"
PATH_TEMPLATE = "./template.html"

def main():
    if os.path.exists(DIR_PATH_PUBLIC):
        logger.info("Deleting public directory...")
        shutil.rmtree(DIR_PATH_PUBLIC)

    logger.info("Copying static files to public directory...")
    copy_files_recursive(DIR_PATH_STATIC, DIR_PATH_PUBLIC)
    
    logger.info("Generating content...")
    generate_pages_recursive(DIR_PATH_CONTENT, PATH_TEMPLATE, DIR_PATH_PUBLIC)

    logger.info("Finished")


if __name__ == "__main__":
    main()
