# To make testing easier
import requests

def example_lagged_values():
    return requests.get('https://www.microprediction.com/live/lagged_values::three_body_x.json').json()



