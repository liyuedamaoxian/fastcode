import json
import os


def load_json_config(config_path):
    with open(config_path, 'r') as infile:
        conf = json.load(infile)
        for key, item in conf.items():
            if isinstance(item, list):
                pass
            elif isinstance(item, str):
                if item.startswith('range'):
                    print(key)
                    start, stop, step = [int(val) for val in item[item.find("(") + 1:item.find(")")].split(',')]
                    conf[key] = list(range(start, stop, step))
                else:
                    raise (ValueError('String in config only allowed as "range(start, stop, step)".'))
        return conf


def store_json_config(config, dir_path, file_name):
    with open(os.path.join(dir_path, file_name), 'w') as outfile:
        json.dump(config, outfile, indent=4)
