def maxProfit(self, prices: List[int]) -> int:
    max_profit_seen = 0 
    lowest_price_seen = prices[0]
    for price in prices:
        max_profit_seen = max(max_profit_seen, price-lowest_price_seen)
        lowest_price_seen = min(lowest_price_seen, price)
    return max_profit_seen
