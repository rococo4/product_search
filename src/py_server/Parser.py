from LxmlSoup import LxmlSoup
from bs4 import BeautifulSoup
import requests
from fp.fp import FreeProxy

proxies = {
            "http" : 'http://35.185.196.38',
            "https" : 'http://35.185.196.38'
        }
header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
        }
def get_all_urls_from_pages(link_to_type_of_product):
    res = []
    # link should be smth like this https://foodsprice.ru/catalog/products/449?sort=price&types=2499
    link_to_type_of_product += "&page="
    i = 1
    while(True):
        link_to_type_of_product += f"{i}"
        i += 1
        print(link_to_type_of_product)
        html = requests.get(link_to_type_of_product).text
        print(html)
        soup = BeautifulSoup(html)
        links = soup.find_all('a', class_="tile__ttl")
        #types = soup.find_all('div', class_="tile__catalog-link")
        if (len(links) == 0): 
            print("yes")
            break
        for link in links:
            url = "https://foodsprice.ru/" + link.get("href")
            #type = types.text()
            #print(type)
            print(url)
            res.append(url)
    return  res

def get_all_urls_by_prod_number(link_to_product):
    res = []
    # link should be smth like this https://foodsprice.ru/catalog/products/449?sort=price
    html = requests.get(link_to_product).text
    soup = BeautifulSoup(html)
    types_with_garbage = soup.find_all('input', class_ = 'hidden')
    values = []
    values_link_to_type_product = {}
    for type in types_with_garbage:
        value = type.get("value")
        values.append(value)
        name = soup.find('label', {'for': f'ptp_{value}'})#????
        values_link_to_type_product[value] = name

    # теперь кидаем ссылку в метод get_all_urls_from_pages
    # получаем на выход массив с ссылками на все продукты данного типа(рис басмати - три ссылки)
    # пишем в словарь типа name: array, где name - название типа продукта, а array - массив ссылок
    # возвращаем что-то типо рис -  {рис басмати:ссылки, рис круглозерновной:ссылки}
    type_of_product_links = {}
    all_dicts = []
    for value in values:
        link_array = get_all_urls_from_pages(link_to_product + f"&types={value}")
        type_of_product_links[values_link_to_type_product[value]] = link_array 
        all_dicts.append(type_of_product_links)
    return all_dicts


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
    for undercategory, link in undercategories_dict.items():
        undercategories_to_product_link[undercategory] = get_all_urls_by_prod_number(link)
    return undercategories_to_product_link


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



def test():
    all = get_all_links_for_products("https://foodsprice.ru/")
    for first, second in all.items():
        print(first)
        for first_1, second_1 in first.items():
            print(first_1)
            for first_2, second_2 in second_1.items():
                print(first_2)
                for first_3, second_3 in second_2.items():
                    print(first_3)

print(get_all_urls_from_pages("https://foodsprice.ru/catalog/products/449?sort=price&types=2499"))



