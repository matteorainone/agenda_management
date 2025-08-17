import os
import json

def handle_missing_file(file_path):
    """
    Handles the case when a JSON file is not found, giving the user the option
    to create a new empty file.
    
    Parameters:
    file_path (str): The path to the JSON file that was not found.
    
    Returns:
    dict: Returns an empty dictionary if the user chooses to create a new file,
    attesting to the desire to start with fresh data.
    
    Raises:
    FileNotFoundError: Raised if the user chooses not to create a new file,
    indicating that the operation cannot continue without the file.
    """
    print(f"Non trovo il file {os.path.basename(file_path)}, o è vuoto o non esiste.")
    new_file = input("Desideri crearne uno nuovo? (Y/n): ")
    if new_file.lower() == "y":
        return {}
    else:
        raise FileNotFoundError(f"File {file_path} non trovato e non creato dall'utente.")

def load_json_data(file_path):
    """
    Loads data from a specified JSON file. Handles cases where the file does not exist
    or contains malformed JSON, giving the user the option to create a new, empty file.
    
    Parameters:
    file_path (str): The path to the JSON file to be loaded.
    
    Returns:
    dict: A dictionary containing the data loaded from the JSON file. Returns an empty dictionary
    if the file does not exist and the user chooses to create a new one, otherwise it raises an exception
    if the file cannot be found or read and the user chooses not to create a new one.
    
    Raises:
    FileNotFoundError: If the specified file does not exist and the user chooses not to create a new one.
    """
    try:
        with open(file_path, "r") as json_file:
            try:
                data = json.load(json_file)
            except json.JSONDecodeError:
                return handle_missing_file(file_path)
    except FileNotFoundError:
        data = handle_missing_file(file_path)
    return data

def write_json_data(data, file_path):
    """
    Writes the supplied data to a specified JSON file. Creates the file if it does not exist,
    or overwrites existing data in the file.
    
    Parameters:
    data : A dictionary (or a list of dictionaries) containing the data to be saved in the JSON file.
    file_path (str): The path to the JSON file in which to save the data.
    """
    with open(file_path, "w") as json_file:
        json.dump(data, json_file, indent=4)