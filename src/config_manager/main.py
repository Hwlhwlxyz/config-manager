import logging
import sys
import argparse
import os
import importlib
from pathlib import Path
import config_manager

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser()
parser.add_argument('--file', default='cm_setting.py', required=False,help="file path to the setting file")
# parser.add_argument('--name', default='', required=False) # run specific setting
parser.add_argument('--run', default="exe", choices=['exe', 'ls'])

args = parser.parse_args()


def find_setting_file(file_path):
    if (os.path.isfile(file_path)):
        sys.path.append(os.path.dirname(file_path))
        cm_module = importlib.import_module(Path(file_path).stem)
        return cm_module
    else:
        print("no such file")

def function_ls():
    cm_module=find_setting_file(args.file)
    print(cm_module.config_manager_setting)
    return

def function_exe():
    cm_module=find_setting_file(args.file)
    cm_module.config_manager_setting
    temp_path=cm_module.config_manager_setting['config']['temp_path']
    setting=cm_module.config_manager_setting['setting']
    for item in setting.items():
        item[1]['name'] = item[0]
        print(item)
        setting_item = item[1]
        config_manager.run_setting(temp_path, setting_item)
    return

if args.run=='ls':
    function_ls()
elif args.run=='exe':
    function_exe()
