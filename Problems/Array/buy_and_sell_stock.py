

def stockBuyAndSell(array):
    max_profit = 0
    min_price = float("inf")

    # Brute Force Solution
    # for i in range(n):
    #     value = 0
    #     for j in range(i+1, n):
    #         if array[j] > array[i]:
    #             value = array[j] - array[i]
    #             profit = max(profit, value)
    #         else:
    #             value = 0 
    #     profit = max(profit, value)  
    

    for i in array:
        min_price = min(min_price, i)
        max_profit = max(max_profit, i - min_price)     

    return max_profit

# -------------------------------------------------

print(stockBuyAndSell([7, 2, 1, 5, 6, 4, 8]))       

# -------------------------------------------------

print(stockBuyAndSell([7, 6, 4, 3, 1]))

# ------------------------------------------------