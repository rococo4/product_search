import psycopg2
from get_all_links import *
# Функция для вставки данных в базу данных
def insert_data(categories_dict):
    conn = psycopg2.connect(
        dbname="all_links",
        user="postgres",
        password="1234",
        host="",
        port="5432"
    )
    cur = conn.cursor()
    create_pfck_table_query = '''
    CREATE TABLE IF NOT EXISTS pfck (
        id SERIAL PRIMARY KEY,
        protein FLOAT,
        fat FLOAT,
        carbohydrates FLOAT,
        kcal FLOAT
    )
    '''

    create_store_table_query = '''
    CREATE TABLE IF NOT EXISTS store (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        price FLOAT,
        link_to_store TEXT,
        product_id INTEGER REFERENCES product(id)
    )
    '''

    create_product_table_query = '''
    CREATE TABLE IF NOT EXISTS product (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        category VARCHAR(255),
        subcategory VARCHAR(255),
        subproduct VARCHAR(255),
        link_to_product TEXT,
        link_to_picture TEXT,
        brand VARCHAR(255),
        weight INTEGER,
        pfck_id INTEGER REFERENCES pfck(id),
        information TEXT
    )
    '''
    cur.execute(create_pfck_table_query)
    cur.execute(create_store_table_query)
    cur.execute(create_product_table_query)
    for category, subcategories in categories_dict.items():
       # category_id = insert_category(cur, category)
        category_name = category
        for subcategory, subproducts in subcategories.items():
            subcategory_name = subcategory
        #    subcategory_id = insert_subcategory(cur, subcategory, category_id)
            for subproduct, urls in subproducts.items():
             #   subproduct_id = insert_subproduct(cur, subproduct, subcategory_id)
                subproduct_name = subproduct
               # insert_urls(cur, urls, subproduct_id)
                for url in urls:
                    prd = get_product(url, category_name, subcategory_name, subproduct_name)

    
    
    conn.commit()
    cur.close()
    conn.close()

def insert_category(cur, category):
    cur.execute("INSERT INTO categories (name) VALUES (%s) RETURNING id", (category,))
    return cur.fetchone()[0]

def insert_subcategory(cur, subcategory, category_id):
    cur.execute("INSERT INTO subcategories (name, category_id) VALUES (%s, %s) RETURNING id", (subcategory, category_id))
    return cur.fetchone()[0]

def insert_subproduct(cur, subproduct, subcategory_id):
    cur.execute("INSERT INTO subproducts (name, subcategory_id) VALUES (%s, %s) RETURNING id", (subproduct, subcategory_id))
    return cur.fetchone()[0]

def insert_urls(cur, urls, subproduct_id):
    for url in urls:
        cur.execute("INSERT INTO urls (url, subproduct_id) VALUES (%s, %s)", (url, subproduct_id))
def insert_in_pfck(cur,protein, fats, carbohydrates,kcal):
    cur.execute("INSERT INTO pfck (protein, fat, carbohydrates, kcal) VALUES (%s, %s, %s, %s)", 
            (protein, fats, carbohydrates, kcal))
    return cur.fetchone()[0]
def insert_in_store(cur,name, price, link_to_store):
    cur.execute("INSERT INTO pfck (protein, fat, carbohydrates, kcal) VALUES (%s, %s, %s, %s)", 
            (name, price, link_to_store))
    return cur.fetchone()[0]
def insert_in_product(name, category, subcategory, subproduct, link_to_product, link_to_picture,brand, weight, pfck_id, information): {
    
}