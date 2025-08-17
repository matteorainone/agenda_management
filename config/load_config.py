import yaml

def load_config():
    with open(r".\config.yaml", "r") as file:
        config = yaml.safe_load(file)
        return config
    
