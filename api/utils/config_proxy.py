import yaml


def load_config(env: str):
    config_file = get_config_file(env)
    with open(config_file) as f:
        return yaml.load(f, Loader=yaml.FullLoader)


def get_config_file(env: str):
    return "configs/" + env + ".yaml"
