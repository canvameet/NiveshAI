# 📊 Order Book Feature Guide

## Overview

The Order Book feature provides real-time market depth analysis showing buy and sell orders at different price levels. This helps identify:
- Market strength and direction
- Buy vs Sell pressure
- Short-term trend signals
- Liquidity at different price levels

---

## Features

### 1. **Real-Time Order Book Data**
- ✅ Bid levels (buy orders) with price, quantity, and value
- ✅ Ask levels (sell orders) with price, quantity, and value
- ✅ Configurable depth (number of price levels)
- ✅ Live updates every 5 seconds (optional)

### 2. **Market Analysis**
- ✅ Total bid volume and value
- ✅ Total ask volume and value
- ✅ Volume imbalance (buy vs sell pressure)
- ✅ Depth ratio (bid depth / ask depth)
- ✅ Market pressure indicator

### 3. **Trading Signals**
- ✅ STRONG BUY / BUY / HOLD / SELL / STRONG SELL
- ✅ Confidence score (0-100%)
- ✅ Signal reasoning
- ✅ Based on order book imbalance

---

## API Endpoints

### 1. Get Order Book for Single Ticker

**Endpoint:** `GET /api/order-book/<ticker>`

**Parameters:**
- `depth` (optional): Number of price levels (default: 10)

**Example:**
```bash
curl "http://localhost:5000/api/order-book/AAPL?depth=10"
```

**Response:**
```json
{
  "ticker": "AAPL",
  "timestamp": "2025-01-29T14:30:00",
  "current_price": 172.50,
  "spread": 0.05,
  "spread_pct": 0.03,
  "bids": [
    {
      "price": 172.48,
      "quantity": 1500,
      "value": 258720.00,
      "level": 1
    }
  ],
  "asks": [
    {
      "price": 172.53,
      "quantity": 1200,
      "value": 207036.00,
      "level": 1
    }
  ],
  "analysis": {
    "total_bid_quantity": 15000,
    "total_ask_quantity": 12000,
    "total_bid_value": 2587200.00,
    "total_ask_value": 2070360.00,
    "quantity_imbalance": 3000,
    "value_imbalance": 516840.00,
    "imbalance_ratio": 0.111,
    "imbalance_pct": 11.11,
    "pressure": "Moderate Buy Pressure",
    "pressure_color": "info",
    "weighted_bid_price": 172.48,
    "weighted_ask_price": 172.53,
    "bid_depth_5": 1293600.00,
    "ask_depth_5": 1035180.00,
    "depth_ratio": 1.250
  },
  "signal": {
    "signal": "BUY",
    "confidence": 75.0,
    "imbalance_ratio": 0.111,
    "depth_ratio": 1.250,
    "reasoning": "Moderate buy pressure (imbalance: 11.1%). More buyers than sellers in the order book."
  }
}
```

### 2. Get Order Books for Multiple Tickers

**Endpoint:** `POST /api/order-book`

**Request Body:**
```json
{
  "tickers": "AAPL,TSLA,GOOGL",
  "depth": 10
}
```

**Example:**
```bash
curl -X POST http://localhost:5000/api/order-book \
  -H "Content-Type: application/json" \
  -d '{"tickers": "AAPL,TSLA", "depth": 10}'
```

**Response:**
```json
{
  "order_books": {
    "AAPL": { /* order book data */ },
    "TSLA": { /* order book data */ }
  },
  "timestamp": "2025-01-29T14:30:00",
  "tickers": ["AAPL", "TSLA"],
  "depth": 10
}
```

---

## Frontend Integration

### 1. Add Order Book Component to Your HTML

Add this to your `index.html`:

```html
<!-- Order Book Container -->
<div id="orderBookContainer"></div>

<!-- Include the order book component -->
<script src="order_book_component.html"></script>
```

### 2. Fetch and Display Order Book

```javascript
// Fetch order book for a ticker
async function showOrderBook(ticker) {
    const data = await fetchOrderBook(ticker, 10);
    if (data) {
        renderOrderBook(data, 'orderBookContainer');
    }
}

// Example: Show order book for AAPL
showOrderBook('AAPL');
```

### 3. Enable Auto-Refresh

```javascript
// Auto-refresh every 5 seconds
toggleAutoRefresh('AAPL', 'orderBookContainer');
```

---

## Understanding the Metrics

### 1. **Imbalance Ratio**
- Range: -1.0 to +1.0
- **Positive**: More buy orders (bullish)
- **Negative**: More sell orders (bearish)
- **Near 0**: Balanced market

**Interpretation:**
- `> 0.2`: Strong buy pressure
- `0.05 to 0.2`: Moderate buy pressure
- `-0.05 to 0.05`: Balanced
- `-0.2 to -0.05`: Moderate sell pressure
- `< -0.2`: Strong sell pressure

### 2. **Depth Ratio**
- Bid depth (top 5 levels) / Ask depth (top 5 levels)
- **> 1.0**: More buying liquidity (bullish)
- **< 1.0**: More selling liquidity (bearish)
- **= 1.0**: Balanced liquidity

### 3. **Volume Imbalance**
- Total bid quantity - Total ask quantity
- **Positive**: More buyers waiting
- **Negative**: More sellers waiting

### 4. **Value Imbalance**
- Total bid value - Total ask value
- Shows dollar amount of imbalance
- More meaningful than quantity for large-cap stocks

---

## Trading Signals

### Signal Logic

| Signal | Conditions | Confidence |
|--------|-----------|------------|
| **STRONG BUY** | Imbalance > 15% AND Depth Ratio > 1.1 | 80-95% |
| **BUY** | Imbalance > 5% AND Depth Ratio > 1.0 | 60-75% |
| **HOLD** | Imbalance between -5% and 5% | ~50% |
| **SELL** | Imbalance < -5% AND Depth Ratio < 1.0 | 60-75% |
| **STRONG SELL** | Imbalance < -15% AND Depth Ratio < 0.9 | 80-95% |

### Example Signals

**Strong Buy Signal:**
```
Signal: STRONG BUY (Confidence: 85%)
Reasoning: Strong buy pressure detected (imbalance: 18.5%). 
Bid depth significantly exceeds ask depth.
```

**Sell Signal:**
```
Signal: SELL (Confidence: 68%)
Reasoning: Moderate sell pressure (imbalance: -8.2%). 
More sellers than buyers in the order book.
```

---

## Use Cases

### 1. **Scalping / Day Trading**
- Monitor order book for entry/exit points
- Look for sudden imbalances
- Trade in direction of pressure

### 2. **Swing Trading**
- Confirm trend direction with order book
- Avoid entering against strong pressure
- Use depth ratio for position sizing

### 3. **Risk Management**
- Check liquidity before large orders
- Avoid illiquid stocks (wide spreads)
- Monitor for sudden pressure changes

### 4. **Market Making**
- Identify profitable spread opportunities
- Balance inventory based on pressure
- Adjust quotes based on depth

---

## Integration with ML Model

### Extract Order Book Features

```python
from src.order_book import OrderBookAnalyzer, calculate_order_book_features

# Get order book
analyzer = OrderBookAnalyzer('AAPL')
order_book = analyzer.get_order_book(depth=10)

# Extract features for ML model
features = calculate_order_book_features(order_book)

# Features returned:
# - ob_imbalance_ratio
# - ob_depth_ratio
# - ob_spread_pct
# - ob_bid_depth_5
# - ob_ask_depth_5
# - ob_value_imbalance
# - ob_quantity_imbalance
```

### Combine with Technical Indicators

```python
# In your feature engineering pipeline
from src.order_book import calculate_order_book_features

# Add order book features to your dataframe
ob_features = calculate_order_book_features(order_book_data)
for key, value in ob_features.items():
    df[key] = value

# Now your ML model can use order book data!
```

---

## Testing

### Test Order Book Module

```bash
cd market-classifier-main
python src/order_book.py
```

**Expected Output:**
```
Testing Order Book Analyzer...
======================================================================

AAPL Order Book Analysis:
----------------------------------------------------------------------
Current Price: $172.50
Spread: $0.05 (0.03%)

Bids (Top 5):
  $172.48 x 1,500 = $258,720.00
  $172.31 x 1,200 = $206,772.00
  ...

Asks (Top 5):
  $172.53 x 1,200 = $207,036.00
  $172.70 x 1,000 = $172,700.00
  ...

Analysis:
  Total Bid Value: $2,587,200.00
  Total Ask Value: $2,070,360.00
  Imbalance: 11.11%
  Pressure: Moderate Buy Pressure

Signal: BUY (Confidence: 75.0%)
Reasoning: Moderate buy pressure (imbalance: 11.1%). More buyers than sellers.
```

---

## Limitations & Notes

### Current Implementation

⚠️ **Note:** The current implementation uses **simulated order book data** based on bid/ask prices from Yahoo Finance.

For **production use**, integrate with:
- **Alpaca Markets** (free real-time data)
- **IEX Cloud** (real-time order book)
- **Polygon.io** (Level 2 data)
- **Interactive Brokers** (TWS API)

### Data Frequency

- Yahoo Finance: Delayed quotes (15-20 minutes)
- Real-time providers: Live updates (milliseconds)

### Recommended Providers

| Provider | Cost | Data Quality | Latency |
|----------|------|--------------|---------|
| Alpaca | Free | Good | ~100ms |
| IEX Cloud | $9/mo | Excellent | ~50ms |
| Polygon.io | $29/mo | Excellent | ~10ms |
| Interactive Brokers | Free (with account) | Excellent | ~5ms |

---

## Next Steps

1. ✅ **Test the API**: Try the endpoints with curl or Postman
2. ✅ **Add to Frontend**: Integrate the order book component
3. ✅ **Enable Auto-Refresh**: Set up live updates
4. ✅ **Combine with ML**: Use order book features in predictions
5. ⚠️ **Upgrade Data Source**: Connect to real-time provider for production

---

## Support

For questions or issues:
- Check API logs: `python server.py`
- Test module: `python src/order_book.py`
- Review documentation: This file

---

**Built with ❤️ by Meet Ratwani & Jaimin Pansal**  
**Feature**: Real-Time Order Book Analysis
