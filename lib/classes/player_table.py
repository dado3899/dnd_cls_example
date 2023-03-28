from sqlalchemy import Column, Integer, String, create_engine, func
from sqlalchemy.orm import Session, relationship
from .base import Base

class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer(),primary_key=True)
    name = Column(String())
    dungeon_masters = relationship('DungeonMaster', secondary = 'dnd_games',back_populates='players')