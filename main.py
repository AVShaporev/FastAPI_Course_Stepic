from fastapi import FastAPI
from fastapi.responses import JSONResponse


app = FastAPI()

sample_product_1 = {
    "product_id": 123,
    "name": "Smartphone",
    "category": "Electronics",
    "price": 599.99
}

sample_product_2 = {
    "product_id": 456,
    "name": "Phone Case",
    "category": "Accessories",
    "price": 19.99
}

sample_product_3 = {
    "product_id": 789,
    "name": "Iphone",
    "category": "Electronics",
    "price": 1299.99
}

sample_product_4 = {
    "product_id": 101,
    "name": "Headphones",
    "category": "Accessories",
    "price": 99.99
}

sample_product_5 = {
    "product_id": 202,
    "name": "Smartwatch",
    "category": "Electronics",
    "price": 299.99
}

sample_products = [sample_product_1, sample_product_2, sample_product_3, sample_product_4, sample_product_5]


@app.get("/")
# async def root():
#     return FileResponse('index.html')
def read_root():
    return {"message": "Hello World!!!"}

@app.get("/product/{product_id}")
def read_product(product_id: int):
    for product in sample_products:
        if product["product_id"] == product_id:
            return JSONResponse(product)
    return "Продукт с указанным id не найден!!!"

@app.get("/products/search")
def search_product(keyword, category=None, limit=10):
    # return "Поиск продуктапо критерием в процессе..."
    res_list = []
    for product in sample_products:
        if len(res_list) >= int(limit):
            if len(res_list) == 0:
                return "По указанным критериям поиска ни один продукт не подходит! Попробуйте изменить критерии поиска."
            return JSONResponse(res_list)
        if product["category"] == category and keyword in product["name"]:
            res_list.append(product)
    return JSONResponse(res_list)