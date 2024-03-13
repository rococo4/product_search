from LxmlSoup import LxmlSoup
from bs4 import BeautifulSoup
import requests
from fp.fp import FreeProxy
from time import sleep
from random import randint
from store import *
from product import *
from pfck import *
def get_all_urls_from_pages(link_to_type_of_product):
    res = []
    # link should be smth like this https://foodsprice.ru/catalog/products/449?sort=price&types=2499
    link_to_type_of_product += "&page="
    i = 1
    while(True):
        link_to_type_of_product += f"{i}"
        i += 1
        sleep(1)
        html = requests.get(link_to_type_of_product).text
        soup = BeautifulSoup(html)
        links = soup.find_all('a', class_="tile__ttl")
        if (len(links) == 0): 
            print("PIZEZ")
            break
        for link in links:
            url = "https://foodsprice.ru/" + link.get("href")
            res.append(url)
            print(url)
            print()
    return  res

def get_all_urls_by_prod_number(link_to_product):
    # link should be smth like this https://foodsprice.ru/catalog/products/449?sort=price
    sleep(1)
    html = requests.get(link_to_product).text
    soup = BeautifulSoup(html)
    filter_items = soup.find_all('div', class_='filter__bubble-inp')
    values = []

    values_link_to_type_product = {}

    for item in filter_items:
        input_element = item.find('input')
        value = input_element.get('value')
        name = item.find('label').get_text(strip=True)
        if (name != 'все типы') :
            values.append(value)
            values_link_to_type_product[value] = name
        

    print(values_link_to_type_product)
    print("123123123123123123123123123123123")
    # теперь кидаем ссылку в метод get_all_urls_from_pages
    # получаем на выход массив с ссылками на все продукты данного типа(рис басмати - три ссылки)
    # пишем в словарь типа name: array, где name - название типа продукта, а array - массив ссылок
    # возвращаем что-то типо рис -  {рис басмати:ссылки, рис круглозерновной:ссылки}
    type_of_product_links = {}
    for value in values:
        link_array = get_all_urls_from_pages(link_to_product + f"&types={value}")
        print(value)
        type_of_product_links[values_link_to_type_product[value]] = link_array 
    return type_of_product_links
# словарь: подвид продукта: ссылки


def get_all_links_undercategories(link_to_undercategory):
    # links shoul be smth like that https://foodsprice.ru/catalog/products/category/8
    html = requests.get(link_to_undercategory).text
    soup = BeautifulSoup(html)

    undercategories_dict = {}
    categories_container = soup.find('div', class_='categories-products')
    if categories_container:
        category_items = categories_container.find_all('div', class_='js-product-category-ff')
        for item in category_items:
            category_name = item.find('a', class_='categories-products__ttl').text.strip()
            category_link = item.find('a', class_='categories-products__ttl')['href']
            undercategories_dict[category_name] = category_link
            
    undercategories_to_product_link = {}
    print(undercategories_dict)
    for undercategory, link in undercategories_dict.items():
        undercategories_to_product_link[undercategory] = get_all_urls_by_prod_number(link + "?sort=price")
    return undercategories_to_product_link
# словарь {подкатергория продукта: {подвид продукта: ссыслки}}

def get_all_links_for_products(link_to_product):
    # link should be smth like that https://foodsprice.ru/
    html = requests.get(link_to_product).text
    soup = BeautifulSoup(html)
    categories_dict = {}

    categories_container = soup.find('div', class_='categories-products')
    if categories_container:
        categories = categories_container.find_all('a')
        for category in categories:
            category_name = category.find('span', class_='categories-products__ttl').text.strip() # ???
            category_link = category['href']
            if (category_name != "ПРОДУКТЫ СО СКИДКОЙ"):
                categories_dict[category_name] ="https://foodsprice.ru/" + category_link
    categories_to_product_link = {}
    for category, link in categories_dict.items():
        categories_to_product_link[category] = get_all_links_undercategories(link)
    return categories_to_product_link
# словарь {категория продукта: {подкатергория продукта: {подвид продукта: ссыслки}}}



def get_product(link_to_product, category, subcategory, subproduct):
    html = requests.get(link_to_product).text
    soup = BeautifulSoup(html)
    print("1")
    stores = []
    for row in soup.find_all('tr'):
        price_tag = row.find('b', class_='fz20')
        print("2")
        if price_tag:
            price = price_tag.text.strip()
            store_tag = row.find('b', class_='lsfw-fill-tbl__inline')
            if store_tag:
                store = store_tag.text.strip()
                link_tag = row.find('a', href=True)
                if link_tag:
                    link = 'https://foodsprice.ru' + link_tag['href']
                    stores.append(Store(store, price, link))
    print("3")
    name = soup.find('td', string='Название').find_next_sibling('td').text.strip()
    brand = soup.find('td', string='Бренд').find_next_sibling('td').text.strip()
    weight = soup.find('td', string='Масса нетто, грамм').find_next_sibling('td').text.strip()
    protein = soup.find('td', string='Белки (г/100г.)').find_next_sibling('td').text.strip()
    fats = soup.find('td', string='Жиры (г/100г.)').find_next_sibling('td').text.strip()
    carbohydrates = soup.find('td', string='Углеводы (г/100г.)').find_next_sibling('td').text.strip()
    kcal = soup.find('td', string='Энерг. ценность (ккал/100г.)').find_next_sibling('td').text.strip()
    description_text = soup.find('p', class_='js-description-txt').get_text()
    link_to_image = soup.find('img')['src']
    print("4")
    return Product(name = name, category=category, subcategory=subcategory, 
                   subproduct=subproduct, link_to_product=link_to_product, brand = brand,
                   weight=weight, pfck = Pfck(protein,fats, carbohydrates, kcal), 
                information=description_text, link_to_picture='https://foodsprice.ru' + link_to_image,stores=stores)
def get_products(categories_dict):
    prds = []
    for category, subcategories in categories_dict.items():
        category_name = category
        for subcategory, subproducts in subcategories.items():
            subcategory_name = subcategory
            for subproduct, urls in subproducts.items():
             #   subproduct_id = insert_subproduct(cur, subproduct, subcategory_id)
                subproduct_name = subproduct
               # insert_urls(cur, urls, subproduct_id)
                for url in urls:
                    prds.append(get_product(url, category_name, subcategory_name, subproduct_name))
    return prds

def test():
    all_urls = get_all_links_for_products("https://foodsprice.ru/")
    for first, second in all_urls.items():
        print(first)
        for first_1, second_1 in second.items():
            print(first_1)
            for first_2, second_2 in second_1.items():
                print(first_2)
                for first_3, second_3 in second_2.items():
                    print(first_3)
def test1():
    print(get_all_links_undercategories("https://foodsprice.ru/catalog/products/category/8"))
def test2():
    res = get_all_urls_by_prod_number("https://foodsprice.ru/catalog/products/449?sort=price")
    print(res)
def test3():
    a = get_product('https://foodsprice.ru/product/318209', '1', '2', '3')
    stores = a.get_stores()
    print(a)
    for i in stores:
        print(i)
def test4():
    res = get_all_links_undercategories("https://foodsprice.ru/catalog/products/category/8")
test3()