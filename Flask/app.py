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
    pass

app.run()
