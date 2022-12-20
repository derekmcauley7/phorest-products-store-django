from requests.auth import HTTPBasicAuth 
import requests
from phorestproducts.settings import API_ENDPOINT, API_USERNAME, API_PASSWORD
import json

class PhorestApi():

    def get_products():
        res = requests.get(API_ENDPOINT + 'product', auth=HTTPBasicAuth(API_USERNAME, API_PASSWORD))
        return res.json().get('_embedded').get('products')

    def create_purchase(order):
        data = PhorestApi.create_purchase_request_data(order.order_items, order.total_price, str(order.id) + "new_order")
        headers = {'Content-type': 'application/json'}
        request = requests.post(API_ENDPOINT + 'purchase', data=json.dumps(data), 
        auth=HTTPBasicAuth(API_USERNAME, API_PASSWORD), headers= headers)
        return request


    def create_purchase_request_data(order_items, price, order_numer):
        return {"clientId":"QLbhb0lKCrKmQemqd6h7iA", "items" :PhorestApi.order_items_data(order_items),
            "number": order_numer,
            "payments":[{"amount":float(price),"type":"CREDIT"}]
            }

    def order_items_data(order_items):
        product_json = []
        for item in order_items:
            product_json.append({
                "branchProductId": item.product.product_id,
                "price" : float(item.price),
                "quantity": item.quantity
            })
        return product_json
