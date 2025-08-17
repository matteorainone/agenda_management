from .values_control import *
from model.contatti import Contact
from model.rubrica import Rubrica

def new_contact_generator():
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
