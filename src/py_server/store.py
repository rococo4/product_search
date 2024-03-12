class Store: 
    def __init__(self, name ,price, link_to_store):
        self.__name = name #string
        self.__price = price #double
        self.__link_to_store = link_to_store #string
    def get_link_to_store(self):
        return self.__link_to_store
    def get_price(self):
        return self.__price
    def get_name(self):
        return self.__name
    def __str__(self):
        return f"Store: {self.__name}, Price: {self.__price}, Link: {self.__link_to_store}"