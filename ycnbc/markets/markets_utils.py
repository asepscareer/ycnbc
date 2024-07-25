import requests


class MarketUtils:
    def __init__(self):
        self.base_url = "https://quote.cnbc.com/quote-html-webservice/restQuote/symbolType/symbol"

    def fetch_data(self, symbols):
        params = {
            'symbols': symbols,
            'requestMethod': 'itv',
            'noform': '1',
            'partnerId': '2',
            'fund': '1',
            'exthrs': '1',
            'output': 'json',
            'events': '1'
        }

        try:
            response = requests.get(self.base_url, params=params)
            if response.status_code == 200:
                data = response.json()
                formatted_quote = data.get('FormattedQuoteResult', {}).get('FormattedQuote', [])

                if formatted_quote:
                    for item in formatted_quote:
                        keys_to_remove = [
                            'portfolioindicator', 'feedSymbol', 'issue_id',
                            'streamable', 'provider', 'code', 'symbolType', 'altSymbol'
                        ]
                        for key in keys_to_remove:
                            if key in item:
                                del item[key]
                    return formatted_quote
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
