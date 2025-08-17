from config.load_config import load_config
from model.rubrica import Rubrica
from input.input_info import new_contact_generator, index_selector
from input.values_control import cell_number_check, email_check, keyword_validator

#inizializzazione delle configurazioni
config = load_config()
commands = config['command_list'].items()

def help_command():
    """
    Stampa a console la lista dei comandi disponibili e la loro descrizione.
    """
    print("I comandi disponibili sono i seguenti:")
    for command, description in commands:
        print(f"{command}: {description}")

def add_command(rubrica: Rubrica):
    """
    Gestisce il comando per aggiungere un nuovo contatto.

    Richiede la generazione di un nuovo contatto tramite `new_contact_generator`
    e lo aggiunge all'istanza della rubrica.

    Args:
        rubrica (Rubrica): L'istanza della rubrica a cui aggiungere il contatto.
    """
    contact = new_contact_generator()
    rubrica.aggiungi_contatto(contatto=contact)

def modify_command(rubrica: Rubrica):
    """
    Gestisce il comando per modificare un contatto esistente.

    Permette all'utente di selezionare un contatto e aggiornare il numero di
    telefono o l'email.

    Args:
        rubrica (Rubrica): L'istanza della rubrica su cui effettuare la modifica.
    """
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
    """
    Gestisce il comando per eliminare un contatto.

    Permette all'utente di selezionare un contatto da eliminare dalla rubrica.

    Args:
        rubrica (Rubrica): L'istanza della rubrica da cui eliminare il contatto.
    """
    index = index_selector(rubrica)
    if index is not None:
        rubrica.elimina_contatto(index=index)
    else:
        print("Nessun contatto eliminato")

def research_command(rubrica: Rubrica):
    """
    Gestisce il comando per la ricerca di un contatto.

    Richiede una parola chiave e stampa i risultati della ricerca.

    Args:
        rubrica (Rubrica): L'istanza della rubrica su cui effettuare la ricerca.
    """
    keyword = keyword_validator()
    results = rubrica.ricerca_contatto(keyword)
    if results:
        for c in results:
            print(c)

def list_command(rubrica: Rubrica):
    """
    Gestisce il comando per visualizzare tutti i contatti.

    Args:
        rubrica (Rubrica): L'istanza della rubrica da visualizzare.
    """
    rubrica.visualizza_contatti()