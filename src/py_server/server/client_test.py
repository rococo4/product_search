import asyncio
import uvicorn
import grpc
from protos import product_grpc_pb2_grpc
from fastapi import Depends, FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
from protos import product_grpc_pb2
from product_service import *
import sys
sys.path.append('/home/rococo4/pg_service_template/src/py_server')
from models.product import Product
from models.pfck import Pfck
from models.store import Store
app = FastAPI()
# @app.get("/get_product")
# async def get_product(product_id: str)->JSONResponse:
#     channel = grpc.aio.insecure_channel("localhost:50051")
#     stub = product_grpc_pb2_grpc.ProductServiceStub(channel)
#     prd_request = product_grpc_pb2.ProductRequest("1")
#     prd_response = stub.GetProduct.future(prd_request)
#     print(prd_response)
#     return prd_response
async def main():
    # Create a gRPC channel
    channel = grpc.aio.insecure_channel("localhost:50051")
    
    # Create a stub for the ProductService
    stub = product_grpc_pb2_grpc.ProductServiceStub(channel)
    
    # Create a ProductRequest with the desired product_id
    prd_request = product_grpc_pb2.ProductRequest(product_id="1")
    
    # Make the gRPC call to get the product
    prd_response = await stub.GetProduct(prd_request)
    print(prd_response.product.name)
    
    # Access the product name from the response
    

asyncio.run(main()) 
