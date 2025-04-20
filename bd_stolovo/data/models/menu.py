from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from ..db_session import SqlAlchemyBase


class MenuTable(SqlAlchemyBase):
    __tablename__ = 'menu_table'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Первичный ключ
    id_weekday = Column(Integer, ForeignKey('weekday.id'), nullable=False)  # Связь с таблицей weekday
    id_dish = Column(Integer, ForeignKey('dishes.id'), nullable=False)  # Связь с таблицей dishes

    # Опционально: добавление отношений (relationships)
    weekday = relationship("Weekday", back_populates="menu_items")
    dish = relationship("Dish", back_populates="menu_items")
