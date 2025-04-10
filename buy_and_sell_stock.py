'''
best time to buy and sell a stock


prices = [7,1,5,3,3,6,4] 
-> 5(6-1)

prices[0] -> 7 
prices[3:] -> [3,3,6,4] 
prices[:3] -> [7,1,5] 




price
profit

price - min price = profit

iterate through -> min price

compare price & min price


ensure the list is not empty

initialise min price = prices[0]
max profit = 0


second iteration
5
min_price = 1
profit = 5 - 1 -> 4
max_profit = 4,0 -> 4

profit = 1 - 1 = 0
for price in prices[1:]
   min_price = min(min_price, price) 

   profit = price - min_price

   max_profit = max(profit,max_profit)
   
return max_profit

'''


def max_profit(prices):
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        min_price = min(min_price, price) 
        profit = price - min_price
        max_profit = max(max_profit, profit)

    return max_profit


def main():

    prices1 = [7,1,5,3,3,6,4] 
    profit1 = max_profit(prices1)
    print(f"Example 1: prices = {prices1}, Max Profit = {profit1}")


    prices2 = [7,6,4,3,1] 
    profit2 = max_profit(prices2)
    print(f"Example 1: prices = {prices2}, Max Profit = {profit2}")


if __name__ == "__main__":
    main()
