# gestione dei contatti

class Contact:
    """
    Una classe per rappresentare un singolo contatto.
    """
    def __init__(self, nome: str, cognome: str, telefono: str, email: str):
        """Inizializza un oggetto Contact.

        Args:
            nome (str): Il nome del contatto.
            cognome (str): Il cognome del contatto.
            telefono (str): Il numero di telefono del contatto.
            email (str): L'indirizzo email del contatto.
        """
        self.nome = nome
        self.cognome = cognome
        self.telefono = telefono
        self.email = email

    def codice_univoco(self):
        """
        Genera un codice univoco per il contatto.

        Il codice è formato dal nome e cognome in minuscolo, separati da un
        underscore.

        Returns:
            str: Il codice univoco del contatto.
        """
        return f"{self.nome.strip().lower()}_{self.cognome.strip().replace(" ","").lower()}"

    def to_dict(self):
        """
        Converte l'oggetto Contact in un dizionario.

        Returns:
            dict: Un dizionario che rappresenta l'oggetto.
        """
        return self.__dict__
    
    @staticmethod
    def from_dict(data):
        """
        Crea un oggetto Contact da un dizionario.

        Args:
            data (dict): Il dizionario contenente i dati del contatto.

        Returns:
            Contact: Un nuovo oggetto Contact.
        """
        return Contact(
            data["nome"],
            data["cognome"],
            data["telefono"],
            data["email"]
        )
    
    def __str__(self):
        """
        Restituisce una rappresentazione in stringa dell'oggetto Contact.
        
        Returns:
            str: Una stringa formattata con nome, cognome, telefono ed email.
        """
        return f"{self.nome} {self.cognome} | Cel: {self.telefono} | Email: {self.email}"