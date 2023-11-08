import requests
from dataclasses import asdict
from models import APIResponse, APIParameters

# base_url = 'https://api.coingecko.com/api/v3/coins'
#
#
# def get_endpoint(endpoint: str, params: APIParameters) -> APIResponse:
#     """Return API response from coingecko markets endpoint"""
#     response = requests.get(url=f'{base_url}/{endpoint}', params=asdict(params))
#     response.raise_for_status()
#     response = APIResponse(response.json())
#
#     return response


url = 'https://api.coingecko.com/api/v3/coins/markets'
parameters = APIParameters(category='decentralized_finance_defi')
# r = requests.get(url, params=asdict(parameters))
# response = r.json()
# print(response)


def get_data(url: str, params: parameters):
    """ return api response from markets url"""
    response = requests.get(url, params=asdict(parameters))
    print(f'printing first response {response}')
    response = APIResponse(response.json())
    print(f'printing API response {response}')
    return response


get_data(url, parameters)
