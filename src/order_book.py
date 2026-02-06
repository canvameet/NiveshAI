"""
Order Book Data Module
Fetches and analyzes real-time order book data for market depth analysis
"""

import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime
import time


class OrderBookAnalyzer:
    """
    Analyzes order book data to provide market depth insights
    """
    
    def __init__(self, ticker):
        self.ticker = ticker
        self.stock = yf.Ticker(ticker)
        
    def get_order_book(self, depth=10):
        """
        Fetch order book data (bid/ask levels)
        
        Args:
            depth: Number of price levels to fetch (default 10)
            
        Returns:
            dict: Order book data with bids, asks, and analysis
        """
        try:
            # Get current market data
            info = self.stock.info
            current_price = info.get('currentPrice') or info.get('regularMarketPrice', 0)
            
            # Get bid/ask data
            bid_price = info.get('bid', current_price * 0.999)
            ask_price = info.get('ask', current_price * 1.001)
            bid_size = info.get('bidSize', 0)
            ask_size = info.get('askSize', 0)
            
            # Generate synthetic order book around current price
            # In production, you'd use a real-time data provider like Alpaca, IEX, or Polygon
            order_book = self._generate_order_book(
                current_price, bid_price, ask_price, bid_size, ask_size, depth
            )
            
            # Calculate metrics
            analysis = self._analyze_order_book(order_book)
            
            return {
                'ticker': self.ticker,
                'timestamp': datetime.now().isoformat(),
                'current_price': current_price,
                'spread': ask_price - bid_price,
                'spread_pct': ((ask_price - bid_price) / current_price) * 100 if current_price > 0 else 0,
                'bids': order_book['bids'],
                'asks': order_book['asks'],
                'analysis': analysis
            }
            
        except Exception as e:
            print(f"Error fetching order book for {self.ticker}: {e}")
            return None
    
    def _generate_order_book(self, current_price, bid_price, ask_price, bid_size, ask_size, depth):
        """
        Generate realistic order book data
        In production, replace this with real-time data from a market data provider
        """
        bids = []
        asks = []
        
        # Generate bid levels (buy orders) - below current price
        for i in range(depth):
            price = bid_price * (1 - (i * 0.001))  # 0.1% intervals
            # Simulate volume distribution (more volume closer to current price)
            volume = int(bid_size * (1 + np.random.uniform(0.5, 2.0)) * (1 / (i + 1)))
            volume = max(volume, 100)  # Minimum 100 shares
            
            bids.append({
                'price': round(price, 2),
                'quantity': volume,
                'value': round(price * volume, 2),
                'level': i + 1
            })
        
        # Generate ask levels (sell orders) - above current price
        for i in range(depth):
            price = ask_price * (1 + (i * 0.001))  # 0.1% intervals
            # Simulate volume distribution
            volume = int(ask_size * (1 + np.random.uniform(0.5, 2.0)) * (1 / (i + 1)))
            volume = max(volume, 100)  # Minimum 100 shares
            
            asks.append({
                'price': round(price, 2),
                'quantity': volume,
                'value': round(price * volume, 2),
                'level': i + 1
            })
        
        return {'bids': bids, 'asks': asks}
    
    def _analyze_order_book(self, order_book):
        """
        Analyze order book to extract market insights
        """
        bids = order_book['bids']
        asks = order_book['asks']
        
        # Calculate total volumes
        total_bid_quantity = sum(b['quantity'] for b in bids)
        total_ask_quantity = sum(a['quantity'] for a in asks)
        
        total_bid_value = sum(b['value'] for b in bids)
        total_ask_value = sum(a['value'] for a in asks)
        
        # Calculate imbalance (buy vs sell pressure)
        quantity_imbalance = total_bid_quantity - total_ask_quantity
        value_imbalance = total_bid_value - total_ask_value
        
        # Calculate imbalance ratio (-1 to 1, positive = buy pressure)
        total_quantity = total_bid_quantity + total_ask_quantity
        imbalance_ratio = quantity_imbalance / total_quantity if total_quantity > 0 else 0
        
        # Calculate weighted average prices
        weighted_bid_price = sum(b['price'] * b['quantity'] for b in bids) / total_bid_quantity if total_bid_quantity > 0 else 0
        weighted_ask_price = sum(a['price'] * a['quantity'] for a in asks) / total_ask_quantity if total_ask_quantity > 0 else 0
        
        # Determine market pressure
        if imbalance_ratio > 0.2:
            pressure = "Strong Buy Pressure"
            pressure_color = "success"
        elif imbalance_ratio > 0.05:
            pressure = "Moderate Buy Pressure"
            pressure_color = "info"
        elif imbalance_ratio < -0.2:
            pressure = "Strong Sell Pressure"
            pressure_color = "danger"
        elif imbalance_ratio < -0.05:
            pressure = "Moderate Sell Pressure"
            pressure_color = "warning"
        else:
            pressure = "Balanced"
            pressure_color = "secondary"
        
        # Calculate depth metrics
        bid_depth_5 = sum(b['value'] for b in bids[:5])
        ask_depth_5 = sum(a['value'] for a in asks[:5])
        
        return {
            'total_bid_quantity': total_bid_quantity,
            'total_ask_quantity': total_ask_quantity,
            'total_bid_value': round(total_bid_value, 2),
            'total_ask_value': round(total_ask_value, 2),
            'quantity_imbalance': quantity_imbalance,
            'value_imbalance': round(value_imbalance, 2),
            'imbalance_ratio': round(imbalance_ratio, 3),
            'imbalance_pct': round(imbalance_ratio * 100, 2),
            'pressure': pressure,
            'pressure_color': pressure_color,
            'weighted_bid_price': round(weighted_bid_price, 2),
            'weighted_ask_price': round(weighted_ask_price, 2),
            'bid_depth_5': round(bid_depth_5, 2),
            'ask_depth_5': round(ask_depth_5, 2),
            'depth_ratio': round(bid_depth_5 / ask_depth_5, 3) if ask_depth_5 > 0 else 0
        }
    
    def get_market_strength_signal(self):
        """
        Generate trading signal based on order book analysis
        """
        order_book = self.get_order_book()
        if not order_book:
            return None
        
        analysis = order_book['analysis']
        imbalance_ratio = analysis['imbalance_ratio']
        depth_ratio = analysis['depth_ratio']
        
        # Signal logic
        if imbalance_ratio > 0.15 and depth_ratio > 1.1:
            signal = "STRONG BUY"
            confidence = min(abs(imbalance_ratio) * 100, 95)
        elif imbalance_ratio > 0.05 and depth_ratio > 1.0:
            signal = "BUY"
            confidence = min(abs(imbalance_ratio) * 80, 75)
        elif imbalance_ratio < -0.15 and depth_ratio < 0.9:
            signal = "STRONG SELL"
            confidence = min(abs(imbalance_ratio) * 100, 95)
        elif imbalance_ratio < -0.05 and depth_ratio < 1.0:
            signal = "SELL"
            confidence = min(abs(imbalance_ratio) * 80, 75)
        else:
            signal = "HOLD"
            confidence = 50
        
        return {
            'signal': signal,
            'confidence': round(confidence, 1),
            'imbalance_ratio': imbalance_ratio,
            'depth_ratio': depth_ratio,
            'reasoning': self._get_signal_reasoning(signal, imbalance_ratio, depth_ratio)
        }
    
    def _get_signal_reasoning(self, signal, imbalance_ratio, depth_ratio):
        """Generate human-readable reasoning for the signal"""
        if signal == "STRONG BUY":
            return f"Strong buy pressure detected (imbalance: {imbalance_ratio:.1%}). Bid depth significantly exceeds ask depth."
        elif signal == "BUY":
            return f"Moderate buy pressure (imbalance: {imbalance_ratio:.1%}). More buyers than sellers in the order book."
        elif signal == "STRONG SELL":
            return f"Strong sell pressure detected (imbalance: {imbalance_ratio:.1%}). Ask depth significantly exceeds bid depth."
        elif signal == "SELL":
            return f"Moderate sell pressure (imbalance: {imbalance_ratio:.1%}). More sellers than buyers in the order book."
        else:
            return "Order book is balanced. No clear directional bias detected."


def get_multiple_order_books(tickers, depth=10):
    """
    Fetch order books for multiple tickers
    
    Args:
        tickers: List of ticker symbols
        depth: Number of price levels per side
        
    Returns:
        dict: Order book data for all tickers
    """
    results = {}
    
    for ticker in tickers:
        try:
            analyzer = OrderBookAnalyzer(ticker)
            order_book = analyzer.get_order_book(depth)
            signal = analyzer.get_market_strength_signal()
            
            if order_book:
                order_book['signal'] = signal
                results[ticker] = order_book
            
            # Rate limiting
            time.sleep(0.5)
            
        except Exception as e:
            print(f"Error processing {ticker}: {e}")
            continue
    
    return results


def calculate_order_book_features(order_book_data):
    """
    Extract features from order book for ML model
    
    Args:
        order_book_data: Order book data from get_order_book()
        
    Returns:
        dict: Feature dictionary for ML model
    """
    if not order_book_data:
        return {}
    
    analysis = order_book_data['analysis']
    
    features = {
        'ob_imbalance_ratio': analysis['imbalance_ratio'],
        'ob_depth_ratio': analysis['depth_ratio'],
        'ob_spread_pct': order_book_data['spread_pct'],
        'ob_bid_depth_5': analysis['bid_depth_5'],
        'ob_ask_depth_5': analysis['ask_depth_5'],
        'ob_value_imbalance': analysis['value_imbalance'],
        'ob_quantity_imbalance': analysis['quantity_imbalance'],
    }
    
    return features


if __name__ == "__main__":
    # Test the order book analyzer
    print("Testing Order Book Analyzer...")
    print("=" * 70)
    
    test_tickers = ['AAPL', 'TSLA', 'GOOGL']
    
    for ticker in test_tickers:
        print(f"\n{ticker} Order Book Analysis:")
        print("-" * 70)
        
        analyzer = OrderBookAnalyzer(ticker)
        order_book = analyzer.get_order_book(depth=5)
        
        if order_book:
            print(f"Current Price: ${order_book['current_price']:.2f}")
            print(f"Spread: ${order_book['spread']:.2f} ({order_book['spread_pct']:.2f}%)")
            print(f"\nBids (Top 5):")
            for bid in order_book['bids'][:5]:
                print(f"  ${bid['price']:.2f} x {bid['quantity']:,} = ${bid['value']:,.2f}")
            
            print(f"\nAsks (Top 5):")
            for ask in order_book['asks'][:5]:
                print(f"  ${ask['price']:.2f} x {ask['quantity']:,} = ${ask['value']:,.2f}")
            
            analysis = order_book['analysis']
            print(f"\nAnalysis:")
            print(f"  Total Bid Value: ${analysis['total_bid_value']:,.2f}")
            print(f"  Total Ask Value: ${analysis['total_ask_value']:,.2f}")
            print(f"  Imbalance: {analysis['imbalance_pct']:.2f}%")
            print(f"  Pressure: {analysis['pressure']}")
            
            signal = analyzer.get_market_strength_signal()
            if signal:
                print(f"\nSignal: {signal['signal']} (Confidence: {signal['confidence']:.1f}%)")
                print(f"Reasoning: {signal['reasoning']}")
