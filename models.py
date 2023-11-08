from dataclasses import dataclass
from typing import Any, List, Optional


@dataclass
class CoinMarketDataSchema:
    id: str
    symbol: str
    name: str
    image: str
    current_price: float
    market_cap: int
    market_cap_rank: int
    fully_diluted_valuation: int
    total_volume: int
    high_24h: int
    low_24h: int
    price_change_24h: float
    price_change_percentage_24h: float
    market_cap_change_24h: int
    market_cap_change_percentage_24h: int
    circulating_supply: int
    total_supply: int
    max_supply: int
    ath: float
    ath_change_percentage: float
    ath_date: str
    atl: float
    atl_change_percentage: float
    atl_date: str
    roi: Any
    last_updated: str


@dataclass
class APIResponse:
    results: List[CoinMarketDataSchema]

    def __post_init__(self):
        self.results = [CoinMarketDataSchema(**x) for x in self.results]


@dataclass
class APIParameters:
    vs_currency: Optional[str] = 'usd'
    ids: Optional[str] = None
    category: Optional[str] = None
    order: Optional[str] = None
    per_page: Optional[int] = 250
    page: Optional[int] = None
    sparkline: Optional[bool] = False
    locale: Optional[str] = None
    precision: Optional[str] = None
