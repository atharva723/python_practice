import azure.functions as func
import datetime
import json
import logging



import azure.functions as func
import json, os

app = func.FunctionApp()
DATA_PATH = "data"

@app.route(route="get_order_status", auth_level=func.AuthLevel.ANONYMOUS)
def get_order_status(req: func.HttpRequest) -> func.HttpResponse:
    order_id = req.params.get("order_id")
    with open(os.path.join(DATA_PATH, "orders.json")) as f:
        orders = json.load(f)
    for order in orders:
        if order["order_id"] == order_id:
            return func.HttpResponse(json.dumps(order), mimetype="application/json")
    return func.HttpResponse("Not found", status_code=404)

@app.route(route="search_product_catalog", auth_level=func.AuthLevel.ANONYMOUS)
def search_product_catalog(req: func.HttpRequest) -> func.HttpResponse:
    query = req.params.get("query", "").lower()
    with open(os.path.join(DATA_PATH, "products.json")) as f:
        products = json.load(f)
    results = [p for p in products if query in p["name"].lower() or query in p["category"].lower()]
    return func.HttpResponse(json.dumps(results), mimetype="application/json")

@app.route(route="lookup_return_policy", auth_level=func.AuthLevel.ANONYMOUS)
def lookup_return_policy(req: func.HttpRequest) -> func.HttpResponse:
    product_type = req.params.get("product_type")
    if product_type == "electronics":
        policy = "Return within 30 days"
    else:
        policy = "Return within 15 days"
    return func.HttpResponse(json.dumps({"policy": policy}), mimetype="application/json")
