from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from get_all_links import *
from product import *
from pfck import *
from store import *
def write_product_in_db():
    engine = create_engine('postgresql://username:password@localhost:5432/database_name')
    Base = declarative_base()

    class Product(Base):
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

    class Store(Base):
        __tablename__ = 'stores'
        id = Column(Integer, primary_key=True)
        name = Column(String)
        price = Column(Float)
        link_to_store = Column(String)
        product_id = Column(Integer, ForeignKey('products.id'))
        product = relationship("Product", back_populates="stores")

        def __repr__(self):
            return f"<Store(name='{self.name}', price='{self.price}')>"


    class Pfck(Base):
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


    Base.metadata.create_all(engine)


    Session = sessionmaker(bind=engine)
    session = Session()
    products = get_products(get_all_links_for_products("https://foodsprice.ru/"))
    for product_pd in products:
        pfck_pd = product_pd.get_pfck()
        pfck = Pfck(protein=pfck_pd.get_protein(), fat=pfck_pd.get_fat(), carbohydrates=pfck_pd.get_carbohydrates(), kcal=pfck_pd.get_kcal())

        product = Product(name=product_pd.get_name(), category=product_pd.get_category(), subcategory=product_pd.get_subcategoty(), subproduct=product_pd.get_subproduct(),
                    link_to_product=product_pd.get_link_to_product(), link_to_picture=product_pd.get_link_to_picture(),
                    brand=product_pd.get_brand(), weight=product_pd.get_weight(), pfck=pfck, information=product_pd.get_information())
        
        stores_pd = product_pd.get_stores()
        for store_pd in stores_pd:
            store = Store(name=store_pd.get_name(), price=store_pd.get_price(), link_to_store=store_pd.get_link_to_store())
            product.stores.append(store)
        session.add(product)
        session.commit()
    
    session.close()
