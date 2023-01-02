from requests.auth import HTTPBasicAuth 
from django.http import Http404
import requests
from phorestproducts.settings import API_ENDPOINT, API_USERNAME, API_PASSWORD
import json

class PhorestApi():
    # uses this endopoint to get a list of products
    # https://developer.phorest.com/#!/Product/getProducts
    def get_products():
        try:
            res = requests.get(API_ENDPOINT + 'product', auth=HTTPBasicAuth(API_USERNAME, API_PASSWORD))
        except Exception as e:
            raise Http404("Exception when requesting Products from Phorest API" + e) 
        return res.json().get('_embedded').get('products')

    # creates a purchase for a prdoduct using this endpont 
    # https://developer.phorest.com/#!/Purchase/createPurchaseForBranch
    def create_purchase(order):
        data = PhorestApi.create_purchase_request_data(order.order_items, order.total_price, str(order.id) + "new_order")
        headers = {'Content-type': 'application/json'}
        request = requests.post(API_ENDPOINT + 'purchase', data=json.dumps(data), 
        auth=HTTPBasicAuth(API_USERNAME, API_PASSWORD), headers= headers)
        return request


    def create_purchase_request_data(order_items, price, order_numer):
        return {
                "clientId":"QLbhb0lKCrKmQemqd6h7iA", 
                "items" :PhorestApi.order_items_data(order_items),
                "number": order_numer,
                "payments":[{"amount":float(price),"type":"CREDIT"}]
                }

    def order_items_data(order_items):
        product_json = []
        for item in order_items:
            product_json.append(
                {
                "branchProductId": item.product.product_id,
                "price" : float(item.price),
                "quantity": item.quantity
                }
            )
        return product_json
