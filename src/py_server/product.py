from pfck import Pfck
class Product:
    def __init__(self, name, category, subcategory, subproduct, 
                 link_to_product, link_to_picture, brand, weight, pfck, information,stores):
        self.__name = name #string
        self.__category = category #string
        self.__subcategory = subcategory#string
        self.__subproduct = subproduct#string
        self.__link_to_product = link_to_product#string
        self.__link_to_picture = link_to_picture#string
        self.__brand = brand#string
        self.__weight = weight#int
        self.__pfck = pfck # Pfck
        self.__information = information#string
        self.__stores = stores # vector<Store>
    
    def get_name(self):
        return self.__name
    
    def get_category(self):
        return self.__category
    
    def get_subcategory(self):
        return self.__subcategory
    
    def get_subproduct(self):
        return self.__subproduct
    
    def get_link_to_product(self):
        return self.__link_to_product
    
    def get_link_to_picture(self):
        return self.__link_to_picture
    
    def get_brand(self):
        return self.__brand
    
    def get_weight(self):
        return self.__weight
    
    def get_pfck(self):
        return self.__pfck
    def get_information(self): 
        return self.__information
    def get_stores(self):
        return self.__stores

    
    def __str__(self):
        return f"Name: {self.__name}\nCategory: {self.__category}\nSubcategory: {self.__subcategory}\nSubproduct: {self.__subproduct}\nLink to product: {self.__link_to_product}\nLink to picture: {self.__link_to_picture}\nBrand: {self.__brand}\nWeight: {self.__weight}\nPFCK: {str(self.__pfck)}\nInformation: {self.__information}\nStores: {str(self.__stores)}"
        
