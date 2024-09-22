import os
from bot.filesreview import mover_diretorios

def main():
    """
    Main function to execute the directory moving process.

    This function defines the source, lead, and final directories. 
    It checks if the final directory exists and creates it if it does not. 
    Then, it calls the `mover_diretorios` function to move directories 
    from the lead folder to the final folder if they match the names 
    of directories in the source folder.
    """
    pasta_origem = 'origem'
    pasta_lead = 'lead'
    pasta_final = 'final'

    if not os.path.exists(pasta_final):
        os.makedirs(pasta_final)

    mover_diretorios(pasta_origem, pasta_lead, pasta_final)

if __name__ == "__main__":
    main()
