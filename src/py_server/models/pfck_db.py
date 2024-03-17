from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

class Pfck(declarative_base()):
        __tablename__ = 'pfcks'
        id = Column(Integer, primary_key=True)
        protein = Column(Float)
        fat = Column(Float)
        carbohydrates = Column(Float)
        kcal = Column(Float)
        product_id = Column(Integer, ForeignKey('products.id'))
        product = relationship("Product", back_populates="pfck")

        def __repr__(self):
            return f"<Pfck(protein='{self.protein}', fat='{self.fat}')>"