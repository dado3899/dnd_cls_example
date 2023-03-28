from sqlalchemy import *
from sqlalchemy.orm import *
from classes.dm_table import DungeonMaster
from classes.player_table import Player
from classes.dnd_games import DndGame
from classes.base import Base

#Set up db file
engine = create_engine('sqlite:///dnd.db')
#Drop Tables
DndGame.__table__.drop(engine)
Player.__table__.drop(engine)
DungeonMaster.__table__.drop(engine)
#Create Tables
Base.metadata.create_all(engine)
#set up a session
with Session(engine) as session:
    #Set up base data
    dm1 = DungeonMaster(name = "David")
    dm2 = DungeonMaster(name = "Matthew")
    player1 = Player(name = "Alex")
    player2 = Player(name = "Seth")
    game1 = DndGame(game_name = "Curse of Strahd",player_class="Warlock",dm_id=1,player_id=1)
    game1_2 = DndGame(game_name = "Curse of Strahd",player_class="Cleric",dm_id=1,player_id=2)
    #Add to database
    everything = [dm1,dm2,player1,player2,game1,game1_2]
    session.add_all(everything)
    session.commit()
    

