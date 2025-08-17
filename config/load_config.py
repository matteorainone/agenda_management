import yaml

def load_config():
    with open(r".\Corso Python\progetto finale\config\config.yaml", "r") as file:
        config = yaml.safe_load(file)
        return config
    