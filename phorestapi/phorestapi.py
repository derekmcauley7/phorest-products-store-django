from requests.auth import HTTPBasicAuth 
import requests
from phorestproducts.settings import API_ENDPOINT, API_USERNAME, API_PASSWORD

class PhorestApi():

    def getProduct():
        res = requests.get(API_ENDPOINT + 'product', 
        auth=HTTPBasicAuth(API_USERNAME, API_PASSWORD))
        return res.json().get('_embedded').get('products')

        
    def make_api_request_for_products():
        res = requests.post(API_ENDPOINT + 'purchase', 
        auth=HTTPBasicAuth(API_USERNAME, API_PASSWORD))
        return res.json()

    def create_purchase_request_data(order_items, price, order_numer):
        return { "items":[PhorestApi.order_items_data(order_items)],
            "number": order_numer,
            "payments":[{"amount":price,"type":"CREDIT"}]
            }

    def order_items_data(order_items):
        product_json = []
        for item in order_items:
            product_json.append({
                "branchProductId": item.product.productId,
                "price" : str(item.price),
                "quantity": item.quantity
            })
        return product_json
