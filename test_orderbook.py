#!/usr/bin/env python3
"""Quick test script for order book endpoint"""

import requests

# Test the order book endpoint
try:
    response = requests.get('http://localhost:5000/api/orderbook/AAPL')
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print("\n✅ Order book endpoint working!")
        print(f"Ticker: {data['ticker']}")
        print(f"Current Price: ${data['currentPrice']:.2f}")
        print(f"Spread: ${data['spread']:.4f}")
        print(f"\nAsks (top 3):")
        for ask in data['asks'][:3]:
            print(f"  ${ask['price']:.2f} - {ask['size']} shares")
        print(f"\nBids (top 3):")
        for bid in data['bids'][:3]:
            print(f"  ${bid['price']:.2f} - {bid['size']} shares")
    else:
        print(f"\n❌ Error: {response.status_code}")
        print(response.text)
        
except requests.exceptions.ConnectionError:
    print("\n❌ Cannot connect to server!")
    print("Make sure the backend is running:")
    print("  python server.py")
except Exception as e:
    print(f"\n❌ Error: {e}")
