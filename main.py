rom typing import List
from api import get_endpoint
from models import APIParameters, CoinMarketDataSchema

endpoint = 'markets'


def get_all_paginated_results(endpoint: str, params: APIParameters) -> List[CoinMarketDataSchema]:
    """Gets paginated results for defi coins, meme coins, and ai coins"""
    defi_results = []
    meme_results = []
    ai_results = []
    for page in range(1, 2):
        params.page = page
        params.category = 'decentralized_finance_defi'
        print(f'accessing defi results page {page}')
        response = get_endpoint(endpoint, params)
        defi_results.extend(response.results)
    print(defi_results)
    return defi_results


def paginated_results(endpoint: str, params: APIParameters) -> List[CoinMarketDataSchema]:
    meme_results = []
    page = params.page
    while True:
        params.category = 'decentralized_finance_defi'
        print(f'accessing meme results page {page}')
        response = get_endpoint(endpoint, params)
        data = response.results
        meme_results.extend(data)

        if not data:
            break

        page += 1


if __name__ == '__main__':
    params = APIParameters()
    response = get_endpoint(endpoint, params)
    results = paginated_results(endpoint, params)
    print(f'Total records: {len(results)}')
