import os
import shutil

def obter_diretorios(pasta):
    """
    Get the list of directories in the specified folder.

    Args:
        pasta (str): The path to the folder from which to list directories.

    Returns:
        set: A set containing the names of directories in the specified folder.
    """
    return set(os.listdir(pasta))

def mover_diretorios(origem, lead, destino):
    """
    Move directories from the lead folder to the final folder based on name matches.

    This function compares the names of directories in the lead folder with those
    in the source folder. If a name match is found, the directory is moved
    to the final folder.

    Args:
        origem (str): The path to the source folder.
        lead (str): The path to the lead folder.
        destino (str): The path to the final folder where matched directories will be moved.
    """
    diretorios_origem = obter_diretorios(origem)
    diretorios_lead = obter_diretorios(lead)
    
    for diretorio in diretorios_lead:
        if diretorio in diretorios_origem:
            origem_diretorio = os.path.join(lead, diretorio)
            destino_diretorio = os.path.join(destino, diretorio)
            print(f'Moving: {origem_diretorio} to {destino_diretorio}')
            shutil.move(origem_diretorio, destino_diretorio)
