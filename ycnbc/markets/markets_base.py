from typing import List, Dict, Optional
from .markets_utils import MarketUtils


class Markets:

    def __init__(self) -> None:
        self.market_utils: MarketUtils = MarketUtils()

    def quote_summary(self, symbol: str) -> Optional[Dict]:
        result: Optional[List[Dict]] = self.market_utils.fetch_data(symbol)
        if result:
            return result[0]
        return None

    def pre_markets(self) -> Optional[List[Dict]]:
        symbols: str = (".HSI|.N225|.STI|.AXJO|.SSEC|.FTSE|.GDAXI|.FCHI|.AEX|.STOXX50|@CL.1|@RB.1|@NG.1|@GC.1|@SI.1|EUR"
                        "=|JPY=|GBP=|CHF=|CAD=|.VIX|.VXN|.OVX|.OOI|.FTFCNBCG|US3M|US2Y|US5Y|US10Y|US30Y|.RUT|.DJT|.DJU"
                        "|.NDX|.NYA|.GSPT|.GSPS|.GSPD|.GSPE|.GSPF")
        return self.market_utils.fetch_data(symbols)

    def us_markets(self) -> Optional[List[Dict]]:
        symbols: str = (".DJI|.IXIC|.SPX|@GC.1|@CL.1|US10Y|EUR=|.VIX|.DJT|.DJU|.NDX|.MID|.RUT|.NYA|@RB.1|@NG.1|@HO.1|@SI.1"
                        "|@HG.1|@W.1|@S.1|@C.1|US1M|US3M|US6M|US1Y|US2Y|US30Y|.DXY|JPY=|GBP=|CAD=|AUD=|SEK=|CHF=")
        return self.market_utils.fetch_data(symbols)

    def europe_markets(self) -> Optional[List[Dict]]:
        symbols: str = (".FTSE|.GDAXI|.FCHI|.STOXX|.AEX|.BFX|.FTMIB|.OMXS30|.SSMI|.OMXHPI|.PSI20|.IMOEX|EUR=|GBP"
                        "=|EURJPY=|EURGBP=|CHF=|EURAUD=|EURCHF=|EURCAD=|UK10Y-GB|DE10Y-DE|IT10Y-IT|FR10Y-FR|ES10Y-ES")
        return self.market_utils.fetch_data(symbols)

    def asia_markets(self) -> Optional[List[Dict]]:
        symbols: str = (".SSEC|.N225|.HSI|.SZI|.KS11|.AXJO|.NSEI|.STI|.IECNCGP|.FTFCNBCA|.NZ50|.SETI|.KLSE|.TWII|JPY"
                        "=|EURJPY=|AUD=|CNY=|SGD=|NZD=|HKD=|INR=|@CL.1|@LCO.1|@NG.1|@HG.1")
        return self.market_utils.fetch_data(symbols)

    def currencies(self) -> Optional[List[Dict]]:
        symbols: str = ("EUR=|JPY=|GBP=|CAD=|CHF=|AUD=|EURCHF=|EURGBP=|"
                        "EURJPY=|AUDJPY=|MXN=|BRL=|ARS=|COP=|CLP=|NZD=|"
                        "GD=|HKD=|KRW=|INR=|SEK=|NOK=|RUB=|DKK=|PLN=")
        return self.market_utils.fetch_data(symbols)

    def cryptocurrencies(self) -> Optional[List[Dict]]:
        symbols: str = ("BTC.CM=|BTC.BS=|BTC.CB=|BTC.GM=|BTC.BF=|BCH.CM=|BCH.BS=|BCH.CB="
                        "BAT.CM=|BNB.CM=|EOS.CM=|ETH.CM=|ETC.CM=|ETH=|ETH.GM=|ETH.BF="
                        "LTC.CM=|LTC.BF=|LTC.CB=|LUNA.CM=|XRP.CM=|XRP.BS=|XTZ.CM=|XLM.CM="
                        "XLM.BF=|ZRX.CM=|ZRX.BF=|ZEC.CM=|DOGE.CM=|NEXO.CM=|ADA.CM=|LINK.CM="
                        "MATIC.CM=|ALGO.CM=|ATOM.CM=|SOL.CM=|DOT.CM=|AMP.CM=|SAND.CM="
                        "AXS.CM=|CRO.CM=|BUSD.CM=|USDC.CM=|UST.CM=|USDT.CM=|UNI.CM="
                        "DAI.CM=|SHIB.CM=|MANA.CM=|TRX.CM=")
        return self.market_utils.fetch_data(symbols)

    def futures_and_commodities(self) -> Optional[List[Dict]]:
        symbols: str = ("@CL.1|@LCO.1|@NG.1|@RB.1|@GC.1|@SI.1|@PL.1|@HG.1|@PA.1|@LBR.1|@W.1|@S.1|@C.1|@SB.1|@KC.1|@CT.1"
                        "|@RR.1|@CC.1|@DX.1|@URO.1|@JY.1|@BP.1|@XBT.1|@LC.1|@LH.1|@FC.1|@DJ.1|@SP.1|@ND.1|@MD.1|@US.1|@TY"
                        ".1|@FV.1|@TU.1|@GE.1")
        return self.market_utils.fetch_data(symbols)

    def bonds(self) -> Optional[List[Dict]]:
        symbols: str = ("US1M|US2M|US3M|US4M|US6M|US1Y|US2Y|US3Y|US5Y|US7Y|US10Y|US20Y|US30Y|UK2Y-GB|UK5Y-GB|UK10Y-GB"
                        "|UK30Y-GB|DE10Y-DE|DE20Y-DE|DE30Y-DE")
        return self.market_utils.fetch_data(symbols)

    def funds_and_etfs(self) -> Optional[List[Dict]]:
        symbols: str = (
            "TLT|SPY|QQQ|IWM|DIA|MDY|EEM|EFA|IVV|VTI|IJR|SSO|TQQQ|SQQQ|EDC|XLE|XLF|XLU|XLI|XLK|XLV|XLP|XLY|GDX|IYR"
            "|GLD|SLV|UNG|USO|IAU|DBC|UUP|FXE|FXY|FXB|EUO|YCS")
        return self.market_utils.fetch_data(symbols)
