from config.load_config import load_config
from model.rubrica import Rubrica
from input.input_info import new_contact_generator, index_selector
from input.values_control import cell_number_check, email_check, keyword_validator

#inizializzazione delle configurazioni
config = load_config()
commands = config['command_list'].items()

def help_command():
    """
    A function used to list the commands avaible
    """
    print("I comandi disponibili sono i seguenti:")
    for command, description in commands:
        print(f"{command}: {description}")

def add_command(rubrica: Rubrica):
    """
    A function used to manage the add command required from the user.

    Args:
        inventor(y_path (str): the path of the inventory json file.
    """
    contact = new_contact_generator()
    rubrica.aggiungi_contatto(contatto=contact)

def modify_command(rubrica: Rubrica):
    index = index_selector(rubrica)
    new_info = {}
    print("Di seguito verranno richieste le informazioni da aggiornare.")
    
    cell_number_modify = input("Modificare numero di cellulare ? (Y/n) ")
    if cell_number_modify == 'Y':
        new_phone = cell_number_check()
        new_info["telefono"] = new_phone
    
    email_modify = input("Modificare email ? (Y/n) ")
    if email_modify == 'Y':
        new_email = email_check()
        new_info["email"] = new_email

    if new_info:
        rubrica.modifica_contatto(index, **new_info)
    else:
        print("Nessun aggiornamento effettuato")
    
def delete_command(rubrica: Rubrica):
    index = index_selector(rubrica)
    if index is not None:
        rubrica.elimina_contatto(index=index)
    else:
        print("Nessun contatto eliminato")

def research_command(rubrica: Rubrica):
    keyword = keyword_validator()
    results = rubrica.ricerca_contatto(keyword)
    if results:
        for c in results:
            print(c)

def list_command(rubrica: Rubrica):
    rubrica.visualizza_contatti()