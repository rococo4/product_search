import sys
sys.path.append('/home/rococo4/pg_service_template/src/py_server')

from protos import product_grpc_pb2_grpc
from protos import product_grpc_pb2
from models.product_db import Product  
from models.product import Product
from grpc import aio
from models.pfck import Pfck
from models.store import Store
import asyncio

class ProductService(product_grpc_pb2_grpc.ProductServiceServicer):
    def SearchProduct(self, request, context):
        product = product_grpc_pb2.ProductResponse(
            product = product_grpc_pb2.Product(
            name='Примерный продукт для GetProduct',
            category='Категория',
            subcategory='Подкатегория',
            subproduct='Подпродукт',
            link_to_product='http://ссылка_на_продукт.com',
            link_to_picture='http://ссылка_на_картинку.com',
            brand='Бренд',
            weight=100,  # Вес в граммах
            pfck=product_grpc_pb2.Pfck(protein=1, fat=1, carbohydrates=1, kcal=1),
            information='Дополнительная информация о продукте',
            stores=[product_grpc_pb2.Store(name="name", price=123, link_to_store="123123123")]
        )
        )
        return product
    def GetProduct(self, request, context):
        print("runned get_product")
        product = product_grpc_pb2.ProductResponse(
            product = product_grpc_pb2.Product(
            name='Примерный продукт для GetProduct',
            category='Категория',
            subcategory='Подкатегория',
            subproduct='Подпродукт',
            link_to_product='http://ссылка_на_продукт.com',
            link_to_picture='http://ссылка_на_картинку.com',
            brand='Бренд',
            weight=100,  # Вес в граммах
            pfck=product_grpc_pb2.Pfck(protein=1, fat=1, carbohydrates=1, kcal=1),
            information='Дополнительная информация о продукте',
            stores=[product_grpc_pb2.Store(name="name", price=123, link_to_store="123123123")]
        )
        )
        return product
    def GetProducts(self, request, context):
        products = []
        product = product_grpc_pb2.Product(
            name='Примерный продукт для GetProduct',
            category='Категория',
            subcategory='Подкатегория',
            subproduct='Подпродукт',
            link_to_product='http://ссылка_на_продукт.com',
            link_to_picture='http://ссылка_на_картинку.com',
            brand='Бренд',
            weight=100,  # Вес в граммах
            pfck=product_grpc_pb2.Pfck(protein=1, fat=1, carbohydrates=1, kcal=1),
            information='Дополнительная информация о продукте',
            stores=[product_grpc_pb2.Store(name="name", price=123, link_to_store="123123123")]
        )
        product1 = product_grpc_pb2.Product(
            name='Примерный продукт для GetProduct',
            category='Категория',
            subcategory='Подкатегория',
            subproduct='Подпродукт',
            link_to_product='http://ссылка_на_продукт.com',
            link_to_picture='http://ссылка_на_картинку.com',
            brand='Бренд',
            weight=100,  # Вес в граммах
            pfck=product_grpc_pb2.Pfck(protein=1, fat=1, carbohydrates=1, kcal=1),
            information='Дополнительная информация о продукте',
            stores=[product_grpc_pb2.Store(name="name", price=123, link_to_store="123123123")]
        )
        products.append(product)
        products.append(product1)
        products_grpc = product_grpc_pb2.ProductResponses(product=products)
        return products_grpc

async def run():
    server = aio.server()
    product_grpc_pb2_grpc.add_ProductServiceServicer_to_server(server=server, servicer=ProductService())
    server.add_insecure_port("localhost:50051")
    print("server started")

async def serve():
    server = aio.server()
    product_grpc_pb2_grpc.add_ProductServiceServicer_to_server(server=server, servicer=ProductService())
    server.add_insecure_port("localhost:50051")
    await server.start()  # Запуск сервера
    await server.wait_for_termination()  # Ожидание завершения работы сервера
if __name__== "__main__":
    asyncio.run(serve())