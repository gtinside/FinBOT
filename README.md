>  [!WARNING]
This project is under active development. Requirements and code are subject to change and may be updated or modified as needed. 

# FinBOT: AI-Powered Financial Data Platform
FinBot is an innovative financial data platform that leverages natural language processing (NLP) to provide users with seamless access to a wide array of financial data through a chatbot interface. Designed for analysts, researchers, and quant developers, FinBot simplifies the way users interact with complex datasets by allowing them to ask questions and retrieve data in real-time, using everyday language.

### Key Features:
- **NLP-Powered Data Queries:** Users can ask natural language questions like "What was Apple's stock price on October 22, 2024?" or "Show me the top 5 companies by market cap" to instantly get accurate and real-time data.
- **Access to Multiple Data Sources:** FinBot integrates structured and unstructured financial data sources, such as stock prices, SEC filings, market news, and social media sentiment, offering a comprehensive view for decision-making.
- **Data Enrichment and Analysis:** The platform provides enriched datasets by cleaning, validating, and normalizing data, allowing users to focus on insights rather than data wrangling.
- **Real-Time Alerts:** Users can set real-time alerts for significant events like earnings reports, filings, or price movements, and be notified instantly through the chatbot.
- **Customizable Data Outputs:** FinBot can deliver data in multiple formats, including CSV, JSON, or even custom backtesting formats, tailored to user needs.
## Types of Data
1. Market Data:
    - Stock Prices: Daily close, open, high, low prices.
    - Tick Data: Trade-by-trade records with timestamps, useful for high-frequency trading.
    - Volume Data: Number of shares or contracts traded.
    - Order Book Data: Bid-ask prices and order quantities.
    - Market Indices: Aggregate indices such as the S&P 500, NASDAQ.
    - Options Data: Strike prices, implied volatility, open interest, and Greeks.
2. Fundamental Data:
    - Financial Statements: Balance sheets, income statements, cash flow statements (quarterly or annually).
    - Ratios: Price-to-Earnings (P/E), Price-to-Book (P/B), Debt-to-Equity (D/E).
    - Earnings Reports: EPS (earnings per share), revenue figures, profit margins.
    - Company Guidance: Forecasts provided by the company for future performance.
3. Alternative Data:
    - Satellite Data: Shipping patterns, crop yields.
    - Social Media: Sentiment analysis on platforms like Twitter, Reddit, and news.
    - Web Traffic: Tracking visits to company websites for gauging customer interest.
    - Credit Card Data: Tracking consumer spending trends.
4. Macroeconomic Data:
    - Interest Rates: Treasury yields, Fed funds rate.
    - Inflation Rates: CPI (Consumer Price Index), PPI (Producer Price Index).
    - Economic Indicators: GDP growth, unemployment rates, PMI (Purchasing Managers’ Index).

<!-- eraser-additional-content -->
## System Architecture
<!-- eraser-additional-files -->
<a href="/README-FinBOT-1.eraserdiagram" data-element-id="uX6l4CRAWcZ4hrTwH_DJP"><img src="/.eraser/cw8qIpoQ11eLn0LkpTla___SR7BTmeEhFeSBhI5mbknU0jkoKK2___---diagram----fdac31668082e999123f6182b2a10176-FinBOT.png" alt="" data-element-id="uX6l4CRAWcZ4hrTwH_DJP" /></a>
<!-- end-eraser-additional-files -->
<!-- end-eraser-additional-content -->
<!--- Eraser file: https://app.eraser.io/workspace/cw8qIpoQ11eLn0LkpTla --->

## Local Setup
1. Set ```OPENAI_API_KEY``` env variable 
2. Run timescaledb in a continer 
    ```
        podman run -d --name market-data-db -p 5432:5432 -e POSTGRES_PASSWORD=password timescale/timescaledb:latest-pg16
    ```
3. Run Apache Kafka in a container 
    ```
    podman run -d -p 9092:9092 --name broker apache/kafka:latest
    ```
4. Create a topic in Kafka Broker 
    ```
    a) podman exec --workdir /opt/kafka/bin/ -it broker sh

    b) ./kafka-topics.sh --bootstrap-server localhost:9092 --create --topic quotes-data
    ```
5. Start the producer
6. To listen to Kafka messages
    ```
    ./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic quotes-data --from-beginning
    ```
7. Connect to timescaledb 
    ```
    podman run -it --net=host -e PGPASSWORD=password --rm timescale/timescaledb:latest-pg16 psql -h localhost -U postgres
    ```
8. Create a new table 
    ```
    CREATE TABLE market_quotes (
    id SERIAL PRIMARY KEY,
    event_type TEXT NOT NULL,
    ticker TEXT NOT NULL,
    
    -- Bid data
    bid_exchange_id INT NOT NULL,
    bid_price DOUBLE PRECISION NOT NULL,
    bid_size INT NOT NULL,

    -- Ask data
    ask_exchange_id INT NOT NULL,
    ask_price DOUBLE PRECISION NOT NULL,
    ask_size INT NOT NULL,

    -- Market metadata
    timestamp BIGINT NOT NULL,
    sequence_number INT NOT NULL,
    tape INT NOT NULL CHECK (tape IN (1, 2, 3)) -- Enum constraint for TapeEnum)
    ```
