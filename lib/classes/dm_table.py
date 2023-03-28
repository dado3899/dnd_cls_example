from sqlalchemy import Column, Integer, String, create_engine, func
from sqlalchemy.orm import Session, relationship,validates
from .base import Base

class DungeonMaster(Base):
    __tablename__ = "dungeon_masters"
    id = Column(Integer(),primary_key=True)
    name = Column(String())
    players = relationship('Player', secondary = 'dnd_games',back_populates='dungeon_masters')

    def add_to_db(self,session):
        session.add(self)
        session.commit()

    def add_player(self,session,player_name):
        from .player_table import Player
        from .dnd_games import DndGame
        filtered_player=session.query(Player).filter(Player.name==player_name).first()
        dnd_class = input("What Class? ")
        game_name = input("Name of Game? ")
        newgame = DndGame(game_name = game_name,player_class=dnd_class,dm_id=self.id,player_id=filtered_player.id)
        session.add(newgame)
        session.commit()
        print(self.players)

        # Take user inputted name
        # get that player from the player table
        # Create join table entry

    @classmethod
    def get_by_name(cls,session,name):
        filtereditem = session.query(DungeonMaster).filter(DungeonMaster.name==name).first()
        print(filtereditem.players)
        return filtereditem
    # @classmethod
    # def all_dm(cls,engine):
    #     with Session(engine) as session:
    #         dm_list = session.query(DungeonMaster).all()
    #     return dm_list