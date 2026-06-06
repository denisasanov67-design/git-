import os
from fastapi import FastAPI, HTTPException

# Инициализация приложения
app = FastAPI(title="Product Service", version="1.0.0")

# Имитация базы данных
PRODUCTS_DB = {
    "1": {"id": "1", "name": "Ноутбук", "price": 999.99},
    "2": {"id": "2", "name": "Беспроводная мышь", "price": 25.50},
    "3": {"id": "3", "name": "Механическая клавиатура", "price": 120.00},
}

@app.get("/health")
def health_check():
    """Эндпоинт для проверки доступности сервиса (liveness probe)."""
    return {"status": "healthy"}

@app.get("/products")
def get_all_products():
    """Возвращает список всех продуктов."""
    return list(PRODUCTS_DB.values())

@app.get("/products/{product_id}")
def get_product(product_id: str):
    """Возвращает конкретный продукт по ID. 
    Именно этот эндпоинт, скорее всего, вызывал Order Service, получая 503 (Service Unavailable), 
    когда сервис был недоступен."""
    product = PRODUCTS_DB.get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product