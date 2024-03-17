

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


class Store(declarative_base()):
        __tablename__ = 'stores'
        id = Column(Integer, primary_key=True)
        name = Column(String)
        price = Column(Float)
        link_to_store = Column(String)
        product_id = Column(Integer, ForeignKey('products.id'))
        product = relationship("Product", back_populates="stores")

        def __repr__(self):
            return f"<Store(name='{self.name}', price='{self.price}')>"