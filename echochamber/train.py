# Example of raw call
import requests

def example_lagged_values():
    return requests.get('https://api.microprediction.org/live/lagged_values::three_body_x.json').json()



