import configparser

config = configparser.ConfigParser()
config.read("sample02.ini")

print(config) # <configparser.ConfigParser object at 0x7fed381b5fd0>
print(config.read("sample02.ini")) # ['sample02.ini']
print(config.defaults()) # {'serveraliveinterval': '45', 'compression': 'yes', 'compressionlevel': '9', 'forwardx11': 'yes'}
print(config.sections()) # ['bitbucket.org', 'topsecret.server.com']
print(config['bitbucket.org']) # <Section: bitbucket.org>
print(config['bitbucket.org']['User']) # hg


ServerAliveInterval = config["DEFAULT"].getint("ServerAliveInterval")
Compression = config["DEFAULT"].get("Compression")

print(ServerAliveInterval) # 45
print(type(ServerAliveInterval)) # <class 'int'>
print(Compression) # yes
print(type(Compression)) # <class 'str'>
