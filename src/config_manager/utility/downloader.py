from urllib.request import urlretrieve
from urllib.parse import urlparse
from zipfile import ZipFile
import subprocess
import os
from pathlib import Path

import logging
logger = logging.getLogger(__name__)

def download_to(url, dst):
    parsed_url = urlparse(url)
    path = parsed_url.path
    if path[:-1] == "/":
        path = path[0:-1]
    filename = parsed_url.path.rpartition("/")[2]
    file_path = os.path.join(dst, filename)
    if not os.path.exists(Path(file_path).parent):
        Path(file_path).parent.mkdir(parents=True)
    urlretrieve(url, file_path)


def unzip(path, unzip_files_path):
    with ZipFile(path, "r") as zObject:
        zObject.extractall(unzip_files_path)


def git_clone(url, dst):
    output = subprocess.Popen(
        ["git", "clone", url, dst],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ).communicate()
    logger.info("clone " + output[0].decode('utf8') + output[1].decode('utf8'))
    return output
