from classes.dm_table import DungeonMaster
from classes.player_table import Player
from classes.dnd_games import DndGame
from cli_paths.dm_logged_in import dm_logged_in
def run_in_dm(session):
    indm = True
    while indm:
        user_type = input("New or Existing:")
        if user_type == "New":
            DungeonMaster(name = input("What is your name? ")).add_to_db(session)
        elif user_type == "Existing":
            username = input("Type Username: ")
            currentUser=DungeonMaster.get_by_name(session,username)
            
            dm_logged_in(session,currentUser)
        else:
            print("Not valid input")