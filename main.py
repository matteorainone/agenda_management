from commands.commands import config, help_command
from commands.command_map import command_map
from model.rubrica import Rubrica
from input.values_control import user_input_format

def main():
    commands_list = config["command_list"].keys()
    rubrica = Rubrica(file_path=config["datasource_path"])
    print("Benvenuto/a nella tua agenda")
    while True:
        try:
            user_command=input("Inserisci un comando: ")
            if user_command.lower() not in [c.lower() for c in commands_list]:
                print("Comando non valido")
                help_command()
            else:
                user_command_formatted = user_input_format(user_command)
                if user_command_formatted in command_map.keys():
                    command_map[user_command_formatted](rubrica)
                elif user_command_formatted == 'Aiuto':
                    help_command()
                elif user_command_formatted == 'Termina applicazione':
                    print("Bye bye")
                    break
                    
        except Exception as e:
            print("Si è verificato un errore", e)

if __name__ == "__main__":
    main()