from openai import OpenAI
from model.quotes import MarketQuote

class FuzzyDataConnector:
    def __init__(self):
        self.client = OpenAI()

    def get_quote_data(self):
         completion = self.client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {"role": "system", "content": "Extract the event information."},
                {"role": "user", "content": "Generate quote data for ticker AAPL"},
            ],
            response_format=MarketQuote,)
         print(completion.choices[0].message.parsed)
         

    def get_us_nbbo_data():
        pass