from curl_cffi import requests
import logging
from typing import List, Dict, Any, Optional
 
from ..exceptions import DataNotFoundError

logger = logging.getLogger(__name__)


class MarketUtils:
    def __init__(self) -> None:
        self.base_url: str = "https://quote.cnbc.com/quote-html-webservice/restQuote/symbolType/symbol"
        self.request: requests.Session = requests.Session()

    def fetch_data(self, symbols: str) -> Optional[List[Dict[str, Any]]]:
        params: Dict[str, Any] = {
            'symbols': symbols,
            'requestMethod': 'itv',
            'noform': '1',
            'partnerId': '2',
            'fund': '1',
            'exthrs': '1',
            'output': 'json',
            'events': '1'
        }

        logger.info(f"Fetching market data for symbols: {symbols}")
        response: requests.Response = self.request.get(
            self.base_url, params=params, impersonate="chrome110")
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        data: Dict[str, Any] = response.json()
        formatted_quote: List[Dict[str, Any]] = data.get(
            'FormattedQuoteResult', {}).get('FormattedQuote', [])

        if not formatted_quote:
            logger.warning(
                f"No formatted quote data found for symbols: {symbols}")
            raise DataNotFoundError(
                f"No formatted quote data found for symbols: {symbols}")

        keys_to_remove: List[str] = [
            'portfolioindicator', 'feedSymbol', 'issue_id',
            'streamable', 'provider', 'code', 'symbolType', 'altSymbol'
        ]
        for item in formatted_quote:
            for key in keys_to_remove:
                if key in item:
                    del item[key]
        return formatted_quote
