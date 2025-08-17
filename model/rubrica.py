from utils.utils import *
from utils.errors import *
from .contatti import Contact

class Rubrica:
    """
    Una classe per gestire una rubrica di contatti.

    Gestisce il caricamento, il salvataggio e le operazioni sui contatti
    memorizzati in un file JSON.
    """
    def __init__(self, file_path: str):
        """
        Inizializza l'oggetto Rubrica.

        Args:
            file_path (str): Il percorso del file JSON in cui sono salvati i contatti.
        """
        self.master_file = file_path
        self.contatti = self._carica_contatti()
        self.codici = [c.codice_univoco() for c in self.contatti]
    
    def _verifica_esistenza(self, codice):
        """
        Verifica se un contatto con un dato codice univoco esiste già.

        Args:
            codice (str): Il codice univoco del contatto da verificare.

        Returns:
            bool: True se il contatto esiste, False altrimenti.
        """
        return codice in self.codici

    def _carica_contatti(self):
        """
        Carica i contatti dal file JSON.

        Returns:
            list: Una lista di oggetti Contact. Restituisce una lista vuota
                  se il file non esiste o non può essere caricato.
        """
        try:
            data = load_json_data(self.master_file)
            return [Contact.from_dict(d) for d in data]
        except ContactLoadError:
            return []
        
    def _salva_modifiche(self):
        """
        Salva lo stato attuale della rubrica nel file JSON.
        """
        data = [c.to_dict() for c in self.contatti]
        write_json_data(data, self.master_file)

    def _ricerca_per_codice(self, codice):
        """
        Cerca un contatto tramite il suo codice univoco e restituisce
        l'indice e l'oggetto.

        Args:
            codice (str): Il codice univoco del contatto da cercare.

        Returns:
            tuple: Una tupla contenente l'indice e l'oggetto Contact.
                   Restituisce (None, None) se il contatto non viene trovato.
        """
        #dato il codice univoco del contatto, si recupera l'indice dello stesso
        for i, c in enumerate(self.contatti):
            if c.codice_univoco() == codice:
                return i,c
            else:
                None, None
        
    
    def aggiungi_contatto(self, contatto: Contact):
        """
        Aggiunge un nuovo contatto alla rubrica.

        Se il contatto esiste già, chiede all'utente se desidera aggiornarlo.

        Args:
            contatto (Contact): L'oggetto Contact da aggiungere.
        """
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
        """
        Modifica un contatto esistente.

        Args:
            index (int): L'indice del contatto da modificare.
            **kwargs: Una o più coppie chiave-valore con le informazioni
                      da aggiornare (es. `telefono`, `email`).
        """
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
        """
        Cerca contatti per nome, cognome o codice univoco.

        Args:
            keyword (str): La parola chiave di ricerca.

        Returns:
            list: Una lista di oggetti Contact che corrispondono alla ricerca.
                  Restituisce None se non ci sono risultati.
        """
        risultati = [
            c for c in self.contatti
            if keyword.lower() in c.cognome.lower() or keyword.lower() in c.nome.lower() or keyword.lower() in self.codici
        ]
        if len(risultati) > 0:
            return risultati
        else:
            print("La ricerca non ha prodotto risultati")
    
    def elimina_contatto(self, index):
        """
        Elimina un contatto dalla rubrica dato il suo indice.

        Args:
            index (int): L'indice del contatto da eliminare.
        """
        try:
            if 0 <= index < len(self.contatti):
                del self.contatti[index]
                self._salva_modifiche()
                print("Contatto eliminato")
        except DeleteContactError:
            print("Nessun contatto eliminato.")


    def visualizza_contatti(self):
        """
        Stampa a console tutti i contatti presenti nella rubrica.
        """
        if self.contatti:
            for i, contatto in enumerate(self.contatti, start=1):
                print(f"{i}.{contatto}")
            print("Contatti elencati")
        else:
            print("Nessun contatto in rubrica")