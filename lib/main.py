from sqlalchemy import *
from sqlalchemy.orm import *
from classes.dm_table import DungeonMaster
from classes.player_table import Player
from classes.dnd_games import DndGame
from classes.base import Base
from cli_paths.in_dm import run_in_dm

if __name__ == '__main__':
    engine = create_engine('sqlite:///dnd.db')
    print( '''
                        \||/
                    |  @___oo
        /\  /\   / (__,,,,|
        ) /^\) ^\/ _)
        )   /^\/   _)
        )   _ /  / _)
    /\  )/\/ ||  | )_)
    <  >      |(,,) )__)
    ||      /    \)___)
    | \____(      )___) )___
    \______(_______;;; __;;;
  '''
    )
    
    with Session(engine) as session:
        inprogram = True
        while inprogram:
            # Checks for player or dm
            userinput1 = input("Are you a Player or DM: ")
            if userinput1 == "DM":
                run_in_dm(session)
            elif userinput1 == "Player":
                print("Hello Player")
                inprogram =False
            else:
                print("Not valid")
    # engine = create_engine('sqlite:///dnd.db')
    pass