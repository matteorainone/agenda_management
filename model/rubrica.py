from utils.utils import *
from utils.errors import *
from .contatti import Contact

class Rubrica:
    def __init__(self, file_path: str):
        self.master_file = file_path
        self.contatti = self._carica_contatti()
        self.codici = [c.codice_univoco() for c in self.contatti]
    
    def _verifica_esistenza(self, codice):
        return codice in self.codici

    def _carica_contatti(self):
        try:
            data = load_json_data(self.master_file)
            return [Contact.from_dict(d) for d in data]
        except ContactLoadError:
            return []
        
    def _salva_modifiche(self):
        data = [c.to_dict() for c in self.contatti]
        write_json_data(data, self.master_file)

    def _ricerca_per_codice(self, codice):
        #dato il codice univoco del contatto, si recupera l'indice dello stesso
        for i, c in enumerate(self.contatti):
            if c.codice_univoco() == codice:
                return i,c
            else:
                None, None
        
    
    def aggiungi_contatto(self, contatto: Contact):
        #verifica esistenza del contatto
        codice = contatto.codice_univoco()
        try:
            if not self._verifica_esistenza(codice=codice):
                self.contatti.append(contatto)
                self._salva_modifiche()
                # generazione del codice univoco per il nuovo contatto inserito
                self.codici.append(contatto.codice_univoco())
                print("Contatto aggiunto correttamente")
            else:
            #gestione dei contatti esistenti
                print(f"Il contatto {codice} è già presente in rubrica.")
                modifica = input("Aggiornare il contatto esistente ? (y/n) ")
                if modifica.lower() == "y":
                    index, _ = self._ricerca_per_codice(codice)
                    self.modifica_contatto(index, telefono = contatto.telefono, email = contatto.email)
                else:
                    print("Contatto non modificato")
        except ContactAddError:
            print("Aggiunta fallita")

    def modifica_contatto(self, index, **kwargs):
        
        try:
            contatto = self.contatti[index]
            for chiave, valore in kwargs.items():
                if hasattr(contatto, chiave):
                    setattr(contatto, chiave, valore)
                    print(f"Informazione {chiave} di contatto aggiornata")
                else:
                    print("Informazione non presente in agenda. Non salvata.")
            
            self._salva_modifiche()
        except ModifyContactError:
            print("Nessuna modifica effettuata")

    def ricerca_contatto(self, keyword):
        risultati = [
            c for c in self.contatti
            if keyword.lower() in c.cognome.lower() or keyword.lower() in c.nome.lower() or keyword.lower() in self.codici
        ]
        if len(risultati) > 0:
            return risultati
        else:
            print("La ricerca non ha prodotto risultati")
    
    def elimina_contatto(self, index):
        try:
            if 0 <= index < len(self.contatti):
                del self.contatti[index]
                self._salva_modifiche()
                print("Contatto eliminato")
        except DeleteContactError:
            print("Nessun contatto eliminato.")


    def visualizza_contatti(self):
        if self.contatti:
            for i, contatto in enumerate(self.contatti, start=1):
                print(f"{i}.{contatto}")
            print("Contatti elencati")
        else:
            print("Nessun contatto in rubrica")