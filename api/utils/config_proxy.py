import yaml


def load_config(env: str):
    config_file_path = get_config_file_path(env)
    with open(config_file_path) as f:
        return yaml.load(f, Loader=yaml.FullLoader)


def get_config_file_path(env: str):
    return "configs/" + env + ".yaml"
