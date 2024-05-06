import os
import shutil
from pathlib import Path
from utility import downloader
import logging

logger = logging.getLogger(__name__)


# src: source path, dst: destination path
def move_files(src, dst):
    if not os.path.exists(dst):
        Path(dst).mkdir(parents=True)
    # get list of files and folders in src
    files_and_folders = os.listdir(src)
    for f in files_and_folders:
        src_path = os.path.join(src, f)
        dst_path = os.path.join(dst, f)
        if os.path.isdir(src_path):
            shutil.copytree(src_path, dst_path)
        elif os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
        else:
            logger.warn("a special file")
    return

def run_setting_downloader(temp_path, input_setting):
    logger.info("start downloading")
    temp_path_w_name = os.path.join(temp_path, input_setting["name"])
    if "source_git" in input_setting:
        downloader.git_clone(input_setting["source_git"], temp_path_w_name)
    elif "source_path" in input_setting:
        move_files(input_setting["source_path"], temp_path_w_name)
    elif "source_url" in input_setting:
        downloader.download_to(input_setting["source_url"], temp_path_w_name)
    return

def run_setting_move(temp_path, input_setting):
    logger.info("move files to "+input_setting["destination"])
    temp_path_w_name = os.path.join(temp_path, input_setting["name"])
    move_files(temp_path_w_name, input_setting["destination"])
    return

def run_setting(temp_path, input_setting):
    run_setting_downloader(temp_path, input_setting)
    run_setting_move(temp_path, input_setting)
    return

