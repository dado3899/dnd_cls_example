from sqlalchemy import ForeignKey,Column, Integer, String, create_engine, func
from sqlalchemy.orm import Session, validates
from .base import Base

class DndGame(Base):
    __tablename__ = "dnd_games"
    id = Column(Integer(),primary_key=True)
    game_name = Column(String())
    player_class = Column(String())
    dm_id = Column(Integer(), ForeignKey('dungeon_masters.id'))
    player_id = Column(Integer(), ForeignKey('players.id'))

    # Validation documentation https://docs.sqlalchemy.org/en/20/orm/mapped_attributes.html
    @validates("player_class")
    def validate_email(self, key, dnd_class):
        classlist = ["Warlock","Warrior","Cleric","Bard","Wizard"]
        if dnd_class not in classlist:
            raise ValueError("Not valid class")
        else:
            return dnd_class