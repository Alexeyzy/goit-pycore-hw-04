import sys

from pathlib import Path
from colorama import Fore, Style

def show_tree(directory, space):
    for item in directory.iterdir():
        if item.is_dir():
            print(space+Fore.BLUE + str(item.name + "/"),Style.RESET_ALL)
            show_tree(item, space + "  ")
        else:
            print(space + Fore.GREEN + str(item.name),Style.RESET_ALL)

space = "  " 
if len(sys.argv) > 1:
    directory = Path(sys.argv[1])
    if not directory.exists():
        print(f"Такого шляху \"{directory}\" не існує.")
    else:
        print(Fore.BLUE + str(directory.name + "/" ),Style.RESET_ALL)  
        show_tree(directory, space) 
else:
    print('No arguments')            


