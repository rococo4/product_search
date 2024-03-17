
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


class Product(declarative_base()):
        __tablename__ = 'products'
        id = Column(Integer, primary_key=True)
        name = Column(String)
        category = Column(String)
        subcategory = Column(String)
        subproduct = Column(String)
        link_to_product = Column(String)
        link_to_picture = Column(String)
        brand = Column(String)
        weight = Column(Integer)
        pfck_id = Column(Integer, ForeignKey('pfcks.id'))
        pfck = relationship("Pfck", back_populates="product")
        information = Column(String)
        stores = relationship("Store", back_populates="product")

        def __repr__(self):
            return f"<Product(name='{self.name}', brand='{self.brand}')>"