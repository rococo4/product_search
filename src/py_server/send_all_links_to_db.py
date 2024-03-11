import psycopg2

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
    
    for category, subcategories in categories_dict.items():
        category_id = insert_category(cur, category)
        for subcategory, subproducts in subcategories.items():
            subcategory_id = insert_subcategory(cur, subcategory, category_id)
            for subproduct, urls in subproducts.items():
                subproduct_id = insert_subproduct(cur, subproduct, subcategory_id)
                insert_urls(cur, urls, subproduct_id)
    
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
