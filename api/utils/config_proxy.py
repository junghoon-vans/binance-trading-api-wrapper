import yaml


def load_config(name: str):
    config_file = get_config_file(name)
    with open(config_file) as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        return config


def get_config_file(name: str):
    return "configs/" + name + ".yaml"
