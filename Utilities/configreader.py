from configparser import ConfigParser


# config = ConfigParser()
# config.read("config.ini") # configuration file name
# print(config.get("locator-userReg","firstname"))
# print(config.get("basic info","browser"))

def readConfig(header, key):
    config = ConfigParser()
    config.read("..//ConfigurationDataFile//conf.ini")
    return config.get(header, key)


print(readConfig("Basic Information", "testURL"))
