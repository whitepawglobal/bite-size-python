"""
pip install yfinance
"""
import yfinance as yf


if __name__ == "__main__":

    nvidia = yf.Ticker("CRCL")
    print(nvidia.history(period="1d")['Close'])
