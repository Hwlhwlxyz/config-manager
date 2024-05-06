import os
import platform


system = platform.system()
home = os.path.expanduser("~")

my_dict = {
    "config": {"temp_path": "ignore1"},
    "setting": {
        "setting-git": {
            "source_git": "https://github.com/XXXX/config",
            "destination": os.path.join(home, "config"),
        },
        "setting-url": {
            "source_url": "https://url.com/XXXX/config",
            "destination": os.path.join(home, "config"),
        },
    },
}


config_manager_setting = my_dict
