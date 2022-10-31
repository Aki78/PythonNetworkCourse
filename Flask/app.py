from flask import Flask, request

app = Flask(__name__)

stores = [
        {
            "items":[
                {
                "name":"Chair",
                "price": 15.99
                }
                ]
            }
        ]

@app.get("/store") #http://127.0.0.1:500/store
def get_stores():
    return {"stores": stores}

@app.post("/store") #http://127.0.0.1:500/store
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201

@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()

    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_date["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return nre_item, 201
    return {"message": "Store not found"}, 404

@app.get("/store/<string:name>/item")
def get_item(name):
    request_data = request.get_json()

    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_date["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return {"items": store["items"], "message": "you rock!"}
    return {"message": "Store not found"}, 404


app.run()
