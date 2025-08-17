#gestione degli errori

class ContactLoadError(Exception):
    def __init__(self, messaggio):
        messaggio = f"Errore nel caricamento dei contatti in rubrica. Nessun contatto presente."
        super().__init__(messaggio)

class ContactAddError(Exception):
    def __init__(self, messaggio):
        messaggio = f"Errore nell'aggiunta del contatto in rubrica. Nessun contatto aggiunto."
        super().__init__(messaggio)

class ModifyContactError(Exception):
    def __init__(self, messaggio):
        messaggio = f"Errore durante la modifica del contatto"
        super().__init__(messaggio)

class DeleteContactError(Exception):
    def __init__(self, messaggio):
        messaggio = f"Errore durante l'eliminazione del contatto"
        super().__init__(messaggio)