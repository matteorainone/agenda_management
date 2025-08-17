# gestione dei contatti

class Contact:
    def __init__(self, nome: str, cognome: str, telefono: str, email: str):
        self.nome = nome
        self.cognome = cognome
        self.telefono = telefono
        self.email = email

    def codice_univoco(self):
        return f"{self.nome.strip().lower()}_{self.cognome.strip().replace(" ","").lower()}"

    def to_dict(self):
        return self.__dict__
    
    @staticmethod
    def from_dict(data):
        return Contact(
            data["nome"],
            data["cognome"],
            data["telefono"],
            data["email"]
        )
    
    def __str__(self):
        return f"{self.nome} {self.cognome} | Cel: {self.telefono} | Email: {self.email}"