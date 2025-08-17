from .values_control import *
from model.contatti import Contact
from model.rubrica import Rubrica

def new_contact_generator():
    """
    Genera un nuovo oggetto Contact chiedendo all'utente le informazioni necessarie.

    La funzione guida l'utente attraverso l'inserimento di nome, cognome,
    numero di telefono ed email, validando ogni input tramite le funzioni
    del modulo `values_control`.

    Returns:
        Contact: Un oggetto Contact appena creato con i dati inseriti.
    """
    contact_name, contact_surname = contact_name_surname_check()
    contact_info = {
        "nome": contact_name,
        "cognome": contact_surname,
        "telefono": cell_number_check(),
        "email": email_check()
    }
    contact=Contact.from_dict(contact_info)
    return contact

def index_selector(rubrica: Rubrica):
    """
    Permette all'utente di selezionare un contatto da una lista di ricerca.

    La funzione chiede all'utente una parola chiave per la ricerca. Se viene trovato
    un solo contatto, restituisce il suo indice. Se ne vengono trovati più di uno,
    li elenca e chiede all'utente di selezionare quello desiderato.

    Args:
        rubrica (Rubrica): L'istanza della rubrica su cui effettuare la ricerca.

    Returns:
        int: L'indice assoluto del contatto selezionato nella lista di contatti
             della rubrica.
    """
    #definizione del criterio di ricerca
    keyword = keyword_validator()
    search_results = rubrica.ricerca_contatto(keyword=keyword)

    while search_results:
        if len(search_results) == 1:
            contact_selected = search_results[0]
            absolute_index = rubrica.contatti.index(contact_selected)
            
            return absolute_index
        
        else:
            print("Contatti multipli trovati: ")
            for i, c in enumerate(search_results, 1):
                print(f"{i}. {c}")

            user_choice = int(input("Selezionare il numero del contatto desiderato: "))-1
            contact_selected = search_results[user_choice]
            absolute_index = rubrica.contatti.index(contact_selected)

            return absolute_index
