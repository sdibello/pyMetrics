"""module to pull data from spring boot, and load it into a metric object."""
import pprint
import yamlconfig

print("load configuration")
with open("settings.yml", 'r') as stream:
    try:   
        print(yaml.load(stream))
    except yaml.YAMLError as exc:
        pprint(exc)



