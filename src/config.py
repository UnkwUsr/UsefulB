from configparser import ConfigParser
from pathlib import Path

CONFIG_FOLDER_PATH = Path.home() / ".config//usefulB"
CONFIG_FILE_PATH = CONFIG_FOLDER_PATH / "config.ini"
# create directory/file if does not exist
Path(CONFIG_FILE_PATH).parent.mkdir(parents=True, exist_ok=True)

config = ConfigParser()

def config_get(section, option, default_value):
    # this conversion is for case when config does not have entry
    # and function will return 'default_value', so this conversion
    # make function behavior like returning exist config value(i.e. string),
    # even then it's not. Makes debug easier
    default_value = str(default_value)

    config.read(CONFIG_FILE_PATH)

    if not config.has_section(section):
        config.add_section(section)
    if not config.has_option(section, option):
        config.set(section, option, str(default_value))
        with open(CONFIG_FILE_PATH, "w") as config_file:
            config.write(config_file)

        return default_value

    else:
        return config.get(section, option)

