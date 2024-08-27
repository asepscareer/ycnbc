import requests
from lxml import html
from ..uri import _HEADERS_, _BASE_URL_


class StocksUtil:
    def __init__(self):
        self.base_url = _BASE_URL_
        self.headers = _HEADERS_
        self.request = requests.session()

    def _fetch_page(self, endpoint=""):
        """
        Fetches and parses the web page content.

        Args:
            endpoint (str): The specific endpoint to fetch data from.

        Returns:
            html.Element: Parsed HTML tree if successful, otherwise an error dictionary.
        """
        try:
            url = f"{self.base_url}/quotes/{endpoint}" if endpoint else self.base_url
            page = self.request.get(url, headers=self.headers)
            page.raise_for_status()
            return html.fromstring(page.content)
        except Exception as e:
            return {"error": str(e)}

    def summary(self, symbol):
        tree = self._fetch_page(symbol)
        data = {}

        for li in tree.xpath("//li[contains(@class, 'Summary-stat')]"):
            label = li.xpath(".//span[@class='Summary-label']/text()")[0]
            value = li.xpath(".//span[@class='Summary-value']/text()")[0]
            data[label] = value
        return data

    def news(self, symbol: str):
        tree = self._fetch_page(f"{symbol}?tab=news")
        data = []

        for item in tree.xpath("//li[contains(@class, 'LatestNews-item')]"):
            headline = item.xpath(".//a[@class='LatestNews-headline']/text()")[0]
            link = item.xpath(".//a[@class='LatestNews-headline']/@href")[0]
            posttime = item.xpath(".//time[@class='LatestNews-timestamp']/text()")[0]

            data.append({
                "headline": headline,
                "link": link,
                "posttime": posttime
            })
        return data

    def profile(self, symbol):
        tree = self._fetch_page(f"{symbol}?tab=profile")
        company_details = {}

        symbol_and_exchange = tree.xpath("//span[@class='QuoteStrip-symbolAndExchange']/text()")
        company_details.update(
            {
                'name': tree.xpath("//span[@class='QuoteStrip-name']/text()")[0].strip(),
                'symbol': symbol_and_exchange[0],
                'exchange': symbol_and_exchange[2],
                'shortDescription': tree.xpath("//div[@class='CompanyProfile-summary']/div/span/text()")[0].strip(),
                'officers': [
                    {
                        'Name': officer.xpath("./div[1]/text()")[0].strip(),
                        'Title': officer.xpath("./div[2]/text()")[0].strip()
                    }
                    for officer in tree.xpath("//div[@class='CompanyProfile-officer']")
                ],
                'address': ", ".join(tree.xpath("//div[@class='CompanyProfile-address']//div/text()")).strip(),
                'website': tree.xpath("//div[@class='CompanyProfile-websiteLink']/a/@href")[0].strip()
            }
        )
        return company_details
