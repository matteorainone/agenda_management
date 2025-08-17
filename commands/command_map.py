from .commands import *

command_map = {
    "Aggiungi": add_command,
    "Visualizza": list_command,
    "Modifica": modify_command,
    "Elimina": delete_command,
    "Ricerca contatto": research_command,
}