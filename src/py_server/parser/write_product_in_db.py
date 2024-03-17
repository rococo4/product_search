from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from get_all_links import *

from models.product import *
from models.pfck import *
from models.store import *
from models.product_db import *
from models.pfck_db import *
from models.store_db import *

def write_product_in_db():
    engine = create_engine('postgresql://username:password@localhost:5432/database_name')
    Base = declarative_base()
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
