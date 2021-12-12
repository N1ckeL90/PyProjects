def convert_prices(prices_list):
    new_prices = []
    for i in range(len(prices_list)):
        new_prices.append(f'{round(prices_list[i])} руб {int(prices_list[i]*100%100):02d} коп')
    print(new_prices)


prices = [57.8, 46.51, 97, 105.4, 11.9, 44.6, 28.57, 151.51, 125.8, 200]
convert_prices(prices)
prices.sort()
convert_prices(prices)
desc_prices = sorted(prices, reverse=True)
convert_prices(desc_prices)
convert_prices(desc_prices[4::-1])
