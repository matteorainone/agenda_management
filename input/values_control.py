import re

def contact_name_surname_check():
    """
    A function which checks the contact name and surname insert from the user.

    """
    pattern=r"^[A-Za-z]+$"
    check_name = False
    check_surname = False

    while not (check_name and check_surname):
        if not check_name:
            contact_name=input("Nome del contatto: ")
            if re.match(pattern,contact_name):
                print("Formato nome valido")
                check_name = True
            else:
                print('Inserire un nome valido, non sono ammessi numeri, caratteri speciali o campi vuoti')
                continue

        if not check_surname:
            contact_surname = input("Cognome del contatto: ")
            if re.match(pattern, contact_surname):
                print("Formato cognome valido")
                check_surname = True
            else:
                print('Inserire un nome valido, non sono ammessi numeri, caratteri speciali o campi vuoti')
                continue

    return [contact_name, contact_surname]

def cell_number_check():
    """
    A function which checks if the cell number insert by the user is correct.

    """
    while True:
        cell_number=input("Inserire numero di telefono: ")
        try:
            cell_number.replace(" ", "")
            #condizioni di verifica (ipotesi di rubrica di numeri di cellulare italiani senza prefissi internazionali):
            # 1. Verificare l'inserimento di caratteri numerici
            # 2. Verificare che la lunghezza del numero di cellulare sia pari a 10
            # 3. Verificare che il numero inserito inizi per 3
            if cell_number.isdigit() and len(cell_number) == 10 and cell_number.startswith("3"):
                break
            else:
                print("Inserire un numero di cellulare valido")
                print("Il formato accettato richiede:\n1. Inserimento di soli numeri\n2. Lunghezza del numero pari a 10 cifre\n3. Nessun prefisso internazionale")
        except ValueError:
            print("Inserire un numero intero")
    return cell_number

def email_check():
    """
    A function which checks if the email insert by the user is correct.

    """
    email_regex = r'^[a-zA-Z0-9_.-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    while True:
        email=input("Inserire indirizzo email: ")
        if re.match(email_regex, email):
                break
        else:
            print("Inserire un indirizzo email valido")
    return email

def keyword_validator():
    pattern = r"^[A-Za-z]+(_[A-Za-z]+)?$" #solo lettere, facoltativo un underscore centrale
    while True:
        keyword = input("Inserire identificativo (nome/cognome/nome_cognome) dell'utente da cercare: ")
        if re.match(pattern, keyword):
            break
        else:
            print("Inserire un identificativo valido (nome/cognome/nome_cognome)!")
    
    return keyword

def user_input_format(input:str):
    input_formatted = input.lower().capitalize()
    return input_formatted